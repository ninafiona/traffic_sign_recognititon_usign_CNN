from PIL import Image
import cv2
import numpy as np
import os

path_class = "C:/Users/ninaf/Desktop/GTSRB/Final_Training/Images/"
#path_class = "C:/Users/ninaf/Desktop/TrainIJCNN2013/"

# Read ground truth file of c(lassification)
gt_data_20 = np.genfromtxt(path_class + "00000/" + "GT-00000.csv", delimiter = ";", dtype=None, skip_header=1)
gt_data_trucks = np.genfromtxt(path_class + "00010/" + "GT-00010.csv", delimiter = ";", dtype=None, skip_header=1)

# save images signs 20 (class 0) and trucks (class 10) to lists
images_20 = []
for i_image in range(len(gt_data_20)):
    img = cv2.imread(path_class + "00000/" + gt_data_20[i_image][0].decode('utf-8'))
    images_20.append(img)
    im = Image.open(path_class + "00000/" + gt_data_20[i_image][0].decode('utf-8'))
    im.save(os.path.splitext(path_class + "00000_jpg/" + gt_data_20[i_image][0].decode('utf-8'))[0]+'.jpg')
images_trucks = []
for i_image in range(len(gt_data_trucks)):
    img = cv2.imread(path_class + "00010/" + gt_data_trucks[i_image][0].decode('utf-8'))
    images_trucks.append(img)
    im = Image.open(path_class + "00010/" + gt_data_trucks[i_image][0].decode('utf-8'))
    im.save(os.path.splitext(path_class + "00010_jpg/" + gt_data_trucks[i_image][0].decode('utf-8'))[0]+'.jpg')