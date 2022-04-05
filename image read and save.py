
import cv2

#imread() method for reading image
img = cv2.imread(r'/Users/neelpatel/Desktop/sem4/cat.png', 1)

# This will display the image
cv2.imshow('image', img)

cv2.waitKey(3)  # This is necessary to be required so that the image doesn't close immediately.

# for saving image
cv2.imwrite('/Users/neelpatel/Desktop/sem 1 to 3/cat_copy.png',img)


print("Image is being saved ")