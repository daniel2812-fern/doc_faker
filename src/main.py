import shutil
import os
import glob
from pathlib import Path


def move_img():
    # Specify the source directories and the destination directory
    img_dirs = ['output/template1/noise_img_path',
                'output/template2/noise_img_path',
                'output/template3/noise_img_path',
                'output/template4/noise_img_path']
    destination_dir = 'output/dataset/img'
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    for source_dir in img_dirs:
        for file_path in glob.glob(os.path.join(source_dir, '*')):
            if os.path.isfile(file_path):
                shutil.copy(file_path, destination_dir)
def move_label():
    json_dirs = ['output/template1/label',
                'output/template2/label',
                'output/template3/label',
                'output/template4/label']
    destination_dir = 'output/dataset/label'
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    for source_dir in json_dirs:
        for file_path in glob.glob(os.path.join(source_dir, '*')):
            if os.path.isfile(file_path):
                destination_file = os.path.join(destination_dir, os.path.basename(os.path.dirname(os.path.dirname(file_path)))+"_"+ Path(file_path).stem+'_1.json')
                print(destination_file)
                shutil.copy(file_path, destination_file)
# move_img()
move_label()