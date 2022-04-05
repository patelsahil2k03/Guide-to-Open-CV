

# importing cv2
import cv2

# path
path = r'/Users/neelpatel/Desktop/sem4/parrot.png'

# For reading image
src = cv2.imread(path)

# Output file name
window_name = 'reverse_parrot'


# Image will rotate by 270 degrees clockwise
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)

