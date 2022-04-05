import cv2

image = cv2.imread(r'C:\Users\CS3306TX\Downloads\download (8).jpg')
edges = cv2.Canny(image, 100, 200)

cv2.imshow("Edge Detected Image", edges)
cv2.imshow("Original Image", image)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image