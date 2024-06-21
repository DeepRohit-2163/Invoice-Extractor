from flask import Flask, request, render_template, redirect, url_for
from pdf2image import convert_from_path
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai
import io

app = Flask(__name__)

def pdf_to_images(pdf_path, dpi=500, poppler_path=None):
    return convert_from_path(pdf_path, dpi, poppler_path=poppler_path)

def save_images(images, output_folder='static/output'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page{i}.jpg')
        image.save(image_path, 'JPEG')
        image_paths.append(image_path)
    return image_paths

def input_image_setup(image_path):
    with open(image_path, 'rb') as file:
        bytes_data = file.read()

    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": bytes_data
        }
    ]
    return image_parts

def get_gemini_response(image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([image[0], prompt])
    return response.text

def process_pdf(pdf_path):
    images = pdf_to_images(pdf_path, poppler_path="poppler-24.02.0/Library/bin")
    image_paths = save_images(images)

    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    input_prompt = """
                   You are an expert in understanding invoices.
                   You will receive input images as invoices and you will have to extract the following information:
                   - From:
                   - To:
                   - Total:
                   - VAT:
                   The invoices can be in multiple languages, so please handle accordingly.
                   """

    results = []
    for image_path in image_paths:
        image_data = input_image_setup(image_path)
        response = get_gemini_response(image_data, input_prompt)
        results.append((image_path, response))

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'pdf' not in request.files:
            return redirect(request.url)
        file = request.files['pdf']
        if file.filename == '':
            return redirect(request.url)
        if file:
            pdf_path = os.path.join('static/uploads', file.filename)
            file.save(pdf_path)
            results = process_pdf(pdf_path)
            return render_template('results.html', results=results)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
