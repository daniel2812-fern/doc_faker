import os 
import sys

src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, src)
from pdf2image import convert_from_path
from src.dir import list_subdirectories
from src.dir import output_directory

def convert_pdf_to_images(pdf_path, output_folder, file_name):
    images = convert_from_path(pdf_path)
    file_name = file_name.split('.')[0]
    for i, image in enumerate(images):
        image.save(f"{output_folder}/{file_name}_{i+1}.png", "PNG")

def process_pdf_directory(pdf_directory, image_directory):
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)

    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, pdf_file)
            convert_pdf_to_images(pdf_path, image_directory, pdf_file)

def main():
    template_list = list_subdirectories(output_directory)

    for template in template_list:
        pdf_directory = os.path.join(output_directory, template, "pdf")
        image_directory = os.path.join(output_directory, template, "image")
        process_pdf_directory(pdf_directory, image_directory)

if __name__ == "__main__":
    main()
