from PIL import Image
import cv2
import numpy as np
import os

#path_class = "C:/Users/ninaf/Desktop/GTSRB/Final_Training/Images/"
path_class = "C:/Users/ninaf/Data/Uni_data/GTSDB_Training/"
#path_class = "C:/Users/ninaf/Desktop/TrainIJCNN2013/"


gt_data = np.genfromtxt(path_class + "gt.txt", delimiter = ";", dtype=None, skip_header=0)

# for i_folder in range(43):
#     # Read ground truth file
#     folder_name = str(i_folder).zfill(2)
#     #gt_data = np.genfromtxt(path_class + folder_name + "/" + "GT-" + folder_name + ".csv", delimiter = ";", dtype=None, skip_header=1)

#     if not os.path.exists(path_class + folder_name + "_jpg/"):
#         os.makedirs(path_class + folder_name + "_jpg/")
#     # save images signs to lists

#     for i_image in range(100):
#         image_name = str(i_image).zfill(5) + ".ppm"
#         try:
#             #img = cv2.imread(path_class + folder_name + "/" + image_name)
#             im = Image.open(path_class + folder_name + "/" + image_name)
#             im.save(os.path.splitext(path_class + folder_name + "_jpg/" + image_name)[0] + '.jpg')
#         except:
#             continue

    # Read ground truth file


if not os.path.exists(path_class + "JPG/"):
   os.makedirs(path_class + "JPG/")
    # save images signs to lists
images = []
for i_image in range(len(gt_data)):
    img = cv2.imread(path_class + gt_data[i_image][0].decode('utf-8'))
    images.append(img)
    im = Image.open(path_class + gt_data[i_image][0].decode('utf-8'))
    im.save(os.path.splitext(path_class + "JPG/" + gt_data[i_image][0].decode('utf-8'))[0]+'.jpg')