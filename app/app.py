from flask import Flask, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
import os
from docx import Document
from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader
import tempfile

from app import create_app

app = create_app()
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

def docx_to_pdf(docx_path, pdf_path, password=None):
    """
    Convert a DOCX file to a PDF, with optional password protection.
    """
    # Read the DOCX content
    doc = Document(docx_path)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)
    
    pdf.output(pdf_path)

    # Add password protection if specified
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
    """
    Homepage to upload DOCX files for conversion.
    """
    if request.method == 'POST':
        file = request.files['file']
        password = request.form.get('password')  # Optional password for the PDF
        
        if file:
            # Save uploaded file securely
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Generate the PDF path
            pdf_filename = f"{os.path.splitext(filename)[0]}.pdf"
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)
            
            # Perform the conversion
            docx_to_pdf(file_path, pdf_path, password)
            
            # Gather file metadata
            metadata = {
                "File Name": filename,
                "File Size (bytes)": os.path.getsize(file_path),
                "PDF File": pdf_filename
            }
            
            return render_template('result.html', metadata=metadata, pdf_path=pdf_path)
    
    return render_template('index.html')

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    """
    Endpoint to download the converted PDF.
    """
    return send_file(filename, as_attachment=True)

@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a friendly message.
    """
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
