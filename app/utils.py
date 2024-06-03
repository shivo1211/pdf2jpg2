import fitz  # PyMuPDF
import os

def pdf_to_jpg(pdf_path, output_dir):
    pdf_document = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap(dpi=300)
        output_file_path = os.path.join(output_dir, f'{os.path.splitext(os.path.basename(pdf_path))[0]}_{page_number + 1}.jpg')
        pix.save(output_file_path)
        print(f'Saved {output_file_path}')
