import cv2
import numpy as np
img1 = cv2.imread('watch.jpg',1)
print(img1.shape)
print(img1[1][2])
#print(np.array(img1)[1])
#rimg = cv2.resize(img1, (1000,600))
#cv2.imshow('qweqwewq12',img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()