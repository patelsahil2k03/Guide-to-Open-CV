import cv2
import numpy
# read image
img = cv2.imread(r'C:\Users\CS3306TX\Downloads\kingfisher-2046453__340.webp', 1)
# apply gaussian blur on src image
dst = median = cv2.medianBlur(img,5)
# display input and output image
cv2.imshow("Median Blurred image", numpy.hstack((img, dst)))
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image