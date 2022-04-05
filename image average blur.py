import cv2
im = cv2.imread(r'C:\Users\CS3306TX\Downloads\kingfisher-2046453__340.webp')
cv2.imshow('Original Image',im)
cv2.imshow('Blurred Image', cv2.blur(im, (3,3)))
cv2.waitKey(0)
cv2.destroyAllWindows()