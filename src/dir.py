import os

def list_files_in_directory(directory_path):
    # List all files in the directory
    files = os.listdir(directory_path)
    # Filter out subdirectories, if any
    file_names = [filename for filename in files if os.path.isfile(os.path.join(directory_path, filename))]
    return file_names

def list_subdirectories(directory_path):
    try:
        subdirectories = [subdir for subdir in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, subdir))]
        return subdirectories
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

base_directory = os.getcwd()
output_directory = os.path.join(base_directory,'output')
templates_directory = os.path.join(base_directory,'templates')
template_list = list_files_in_directory(templates_directory)