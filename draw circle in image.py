import numpy as np
import cv2
# for reading Image
img = cv2.imread(r"/Users/neelpatel/Desktop/sem4/panda.png",1)
# circle function to draw circle
cv2.circle(img,(80,80), 80, (0,255,0), -1)
# to show image
cv2.imshow('image',img)
cv2.waitKey(0)
# to destroy all windows
cv2.destroyAllWindows()