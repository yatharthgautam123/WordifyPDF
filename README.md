# WordifyPDF
# 📄 **Docx to PDF Converter**  
*A seamless tool to convert Word documents (.docx) into PDF with optional password protection.*

![Converter Banner](https://via.placeholder.com/1200x300.png?text=Docx+to+PDF+Converter)  

---

## 🚀 **Features**
✅ **Upload DOCX Files**: Simple interface to upload `.docx` files.  
✅ **PDF Conversion**: Converts Word documents into professional-looking PDFs.  
✅ **Password Protection**: Secure your PDF with an optional password.  
✅ **File Metadata**: Displays file name and size after upload.  
✅ **Download Link**: Instant access to your converted PDF.  
✅ **Error Handling**: Friendly error pages for a better user experience.  
✅ **Dockerized & Deployable**: Fully containerized application for scalable deployment.  
✅ **Kubernetes Ready**: Manifest files for effortless hosting on Kubernetes.  

---

## 🎨 **Screenshots**

### 📤 Upload Page:
![Upload Page](https://via.placeholder.com/800x400.png?text=Upload+Page)

### 📜 Metadata and Download:
![Result Page](https://via.placeholder.com/800x400.png?text=Conversion+Successful)

---

## 📂 **Flowchart**

Below is the high-level flowchart illustrating the application's workflow:

![Application Flowchart](https://via.placeholder.com/800x400.png?text=Flowchart)

*Steps:*  
1. User uploads a `.docx` file via the web interface.  
2. Backend processes the file and extracts metadata.  
3. Converts the `.docx` to a PDF (with optional password protection).  
4. Displays metadata and download link for the PDF.  

---

## 🛠️ **Technology Stack**
- **Backend**: Flask
- **Frontend**: HTML5, CSS3
- **File Conversion**: `python-docx`, `FPDF`, `PyPDF2`
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Orchestration**: Kubernetes

---

## 🧑‍💻 **Getting Started**

Follow these steps to run the application locally or deploy it on your favorite platform.

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/docx-to-pdf.git
cd docx-to-pdf
