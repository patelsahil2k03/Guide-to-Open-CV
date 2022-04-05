import cv2
import numpy

# read image
src = cv2.imread(r'C:\Users\CS3306TX\Downloads\kingfisher-2046453__340.webp', 1)
# apply gaussian blur on src image
dst = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)

# display input and output image
cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image