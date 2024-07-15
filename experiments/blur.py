import cv2
import numpy as np

image = cv2.imread('assets/slika.jpg')

kernel = np.ones((25, 25), np.float32)
kernel /= np.sum(kernel)
blurred1 = cv2.filter2D(image, -1, kernel)

blurred2 = cv2.GaussianBlur(image, (25, 25), 10)

cv2.imshow('Box blur', blurred1)
cv2.imshow('Gaussian blur', blurred2)
cv2.waitKey(0)
cv2.destroyAllWindows()