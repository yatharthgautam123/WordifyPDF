from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from docx import Document
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import tempfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

def docx_to_pdf(docx_path, pdf_path, password=None):
    doc = Document(docx_path)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)
    pdf.output(pdf_path)
    
    if password:
        writer = PdfWriter()
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(password)
        with open(pdf_path, "wb") as f:
            writer.write(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        password = request.form.get('password')
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{os.path.splitext(filename)[0]}.pdf")
            docx_to_pdf(file_path, pdf_path, password)
            
            metadata = f"File Name: {filename}\nSize: {os.path.getsize(file_path)} bytes"
            return render_template('result.html', metadata=metadata, pdf_path=pdf_path)
    return render_template('index.html')

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
