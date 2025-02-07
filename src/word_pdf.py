import os
import sys
import subprocess
import concurrent.futures
src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, src)
from src.dir import output_directory,list_subdirectories

def execute_command(command):
    subprocess.run(command, check=True)

def convert_docx_to_pdf(docx_directory, pdf_directory):
    docx_list = os.listdir(docx_directory)
    if not os.path.exists(pdf_directory):
        os.makedirs(pdf_directory)
    commands = []
    for docx in docx_list:
        docx_path = os.path.join(docx_directory, docx)
        command = [
                "soffice",
                "--headless",
                "--convert-to",
                "pdf",
                docx_path,
                "--outdir",
                pdf_directory,
            ]
        commands.append(command)
    return commands

def main():
    template_list = list_subdirectories(output_directory)
    total_commands = []
    for template in template_list:
        docx_directory = os.path.join(output_directory, template, "docx")
        pdf_directory = os.path.join(output_directory, template, "pdf")
        commandlist = convert_docx_to_pdf(docx_directory, pdf_directory)
        total_commands.extend(commandlist)

    for command in total_commands:
        execute_command(command)
if __name__ == "__main__":
    main()
