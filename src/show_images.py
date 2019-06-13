import cv2
import numpy as np

path_detect = "C:/Users/ninaf/Desktop/TrainIJCNN2013/"
path_class = "C:/Users/ninaf/Desktop/GTSRB/Final_Training/Images/00000/"

# Read ground truth file of d(etection) and c(lassification)
gt_data_d = np.genfromtxt(path_detect + "gt.txt", delimiter = ";", dtype=None)
gt_data_c = np.genfromtxt(path_class + "GT-00000.csv", delimiter = ";", dtype=None, skip_header=1)

# Read and show images
# for i_image in range(len(gt_data_d)):
#     img = cv2.imread(path_detect + gt_data_d[i_image][0].decode('utf-8'))
#     cv2.namedWindow("Images", cv2.WND_PROP_FULLSCREEN)
#     cv2.imshow( "Images", img )
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
for i_image in range(len(gt_data_c)):
    img = cv2.imread(path_class + gt_data_c[i_image][0].decode('utf-8'))
    cv2.namedWindow("Images", cv2.WND_PROP_FULLSCREEN)
    cv2.imshow( "Images", img )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
