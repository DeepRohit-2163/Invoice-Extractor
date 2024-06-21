<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Invoice PDF Processing Application</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    h1, h2, h3 {
      color: #333;
    }
    code {
      background-color: #f5f5f5;
      padding: 2px 4px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-family: Consolas, monospace;
    }
    pre {
      background-color: #f5f5f5;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      overflow-x: auto;
    }
    .section {
      margin-bottom: 30px;
    }
  </style>
</head>
<body>
  <h1>Invoice PDF Processing Application</h1>

  <div class="section">
    <h2>Overview</h2>
    <p>This application allows you to upload invoice PDFs, extract information using Google Generative AI, and display results with a consistent background image.</p>
  </div>

  <div class="section">
    <h2>Features</h2>
    <ul>
      <li>Upload invoice PDF files.</li>
      <li>Convert PDF pages to images using pdf2image.</li>
      <li>Extract sender, receiver, total amount, and VAT details using Google Generative AI (Gemini model).</li>
      <li>Display results on a stylish interface with consistent background images.</li>
    </ul>
  </div>

  <div class="section">
    <h2>Prerequisites</h2>
    <ul>
      <li>Python 3.6 or higher</li>
      <li>Flask (`pip install Flask`)</li>
      <li>pdf2image (`pip install pdf2image`)</li>
      <li>Google Generative AI API key (for Gemini model)</li>
      <li>Poppler for PDF processing (poppler or poppler-utils)</li>
    </ul>
  </div>

  <div class="section">
    <h2>Directory Structure</h2>
    <pre>
project_folder/
├── app.py
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   ├── background.png
│   ├── uploads/
│   └── output/
├── .env
└── poppler-24.02.0/
    </pre>
  </div>

  <div class="section">
    <h2>Setup and Configuration</h2>
    <ol>
      <li>Clone the repository: <code>git clone https://github.com/your/repository.git</code></li>
      <li>Navigate to the project directory: <code>cd project_folder</code></li>
      <li>Create a virtual environment (optional): <code>python -m venv venv</code></li>
      <li>Activate the virtual environment:
        <ul>
          <li>Windows: <code>venv\Scripts\activate</code></li>
          <li>Unix or MacOS: <code>source venv/bin/activate</code></li>
        </ul>
      </li>
      <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
      <li>Create a `.env` file and add your Google Generative AI API key: <code>GOOGLE_API_KEY=your_api_key</code></li>
      <li>Ensure Poppler is installed and set the path in `app.py` for PDF processing.</li>
    </ol>
  </div>

  <div class="section">
    <h2>Running the Application</h2>
    <ol>
      <li>Run the Flask application: <code>python app.py</code></li>
      <li>Open your web browser and go to: <code>http://127.0.0.1:5000/</code></li>
      <li>Upload an invoice PDF, and follow the on-screen instructions.</li>
    </ol>
  </div>

  <div class="section">
    <h2>Notes</h2>
    <ul>
      <li>Customize styles, background images, and functionality as per project requirements.</li>
      <li>Handle error scenarios such as invalid file uploads or API key issues gracefully in the application logic.</li>
    </ul>
  </div>

  <div class="section">
    <h2>Credits</h2>
    <ul>
      <li>Developed using Flask, pdf2image, Google Generative AI (Gemini model), and Bootstrap for styling.</li>
    </ul>
  </div>

  <div class="section">
    <h2>Support and Contact</h2>
    <ul>
      <li>Email: <a href="mailto:your_email@example.com">your_email@example.com</a></li>
      <li>Website: <a href="http://www.example.com">www.example.com</a></li>
    </ul>
  </div>

</body>
</html>
