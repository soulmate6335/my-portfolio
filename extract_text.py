import pdfplumber
import os

folder = 'image'
for file in os.listdir(folder):
    if file.endswith('.pdf'):
        try:
            with pdfplumber.open(os.path.join(folder, file)) as pdf:
                text = pdf.pages[0].extract_text()
                print(f"File: {file}")
                print(text[:500])  # first 500 chars
                print("---")
        except Exception as e:
            print(f"Error with {file}: {e}")