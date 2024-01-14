import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text

pdf_directory = r'D:\VIDEO\Belajar\Project\01\Parsing_PDF_Project\PDFs Folder'

for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        extracted_text = extract_text_from_pdf(pdf_path)
        print(f'Text extracted from {filename}:\n{extracted_text}\n{"="*50}\n')
