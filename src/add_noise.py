import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import sys
src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, src)

from src.dir import list_files_in_directory,list_subdirectories,output_directory

def noise(img_path,output_path):
    # img_path = "output/template1/image/0.png"
    img = cv2.imread(img_path)[...,::-1]/255.0
    noise =  np.random.normal(loc=0, scale=1, size=img.shape)
    # noise overlaid over image
    # noisy = np.clip((img + noise*0.2),0,1)
    # noisy2 = np.clip((img + noise*0.4),0,1)
    # noise multiplied by image:
    # whites can go to black but blacks cannot go to white
    noisy2mul = np.clip((img*(1 + noise*0.2)),0,1)
    # noisy4mul = np.clip((img*(1 + noise*0.4)),0,1)
    # noise multiplied by bottom and top half images,
    # whites stay white blacks black, noise is added to center
    img2 = img*2
    # n2 = np.clip(np.where(img2 <= 1, (img2*(1 + noise*0.2)), (1-img2+1)*(1 + noise*0.2)*-1 + 2)/2, 0,1)
    # n4 = np.clip(np.where(img2 <= 1, (img2*(1 + noise*0.4)), (1-img2+1)*(1 + noise*0.4)*-1 + 2)/2, 0,1)
    # # norm noise for viz only
    # noise2 = (noise - noise.min())/(noise.max()-noise.min())
    cv2.imwrite(output_path, 255*noisy2mul)


template_list = list_subdirectories("output")
for template in template_list:

    image_path = output_directory+"/"+template+"/image/"
    noise_img_path = output_directory+"/"+template+"/noise_img_path/"

    image_list = list_files_in_directory(image_path)
    if not os.path.exists(noise_img_path):
            os.makedirs(noise_img_path) 
    for imga in image_list:
        input_path = image_path+imga
        output_path = noise_img_path+template+"_"+imga
        print(output_path)
        noise(input_path,output_path)
        