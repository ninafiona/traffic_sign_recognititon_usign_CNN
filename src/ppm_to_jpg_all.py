from PIL import Image
import cv2
import numpy as np
import os

path_class = "C:/Users/ninaf/Desktop/GTSRB/Final_Training/Images/"
#path_class = "C:/Users/ninaf/Desktop/TrainIJCNN2013/"

for i_folder in range(33,34):
    # Read ground truth file
    folder_name = str(i_folder).zfill(5)
    gt_data = np.genfromtxt(path_class + folder_name + "/" + "GT-" + folder_name + ".csv", delimiter = ";", dtype=None, skip_header=1)

    if not os.path.exists(path_class + folder_name + "_jpg/"):
        os.makedirs(path_class + folder_name + "_jpg/")
    # save images signs to lists
    images = []
    for i_image in range(len(gt_data)):
        img = cv2.imread(path_class + folder_name + "/" + gt_data[i_image][0].decode('utf-8'))
        images.append(img)
        im = Image.open(path_class + folder_name + "/" + gt_data[i_image][0].decode('utf-8'))
        im.save(os.path.splitext(path_class + folder_name + "_jpg/" + gt_data[i_image][0].decode('utf-8'))[0]+'.jpg')