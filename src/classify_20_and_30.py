import cv2
import numpy as np

path_detect = "C:/Users/ninaf/Desktop/TrainIJCNN2013/"
path_class = "C:/Users/ninaf/Desktop/GTSRB/Final_Training/Images/"

# Read ground truth file
gt_data = np.genfromtxt(path_detect + "gt.txt", delimiter = ";", dtype=None)

# Read and show images
for i_image in range(len(gt_data)):
    img = cv2.imread(path_detect + gt_data[i_image][0].decode('utf-8'))
    cv2.namedWindow("Images", cv2.WND_PROP_FULLSCREEN)
    cv2.imshow( "Images", img )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
