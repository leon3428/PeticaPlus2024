import cv2
import numpy as np

def main():
    image = cv2.imread('assets/loptica.png')

    height, width, _ = image.shape
    blurred = cv2.GaussianBlur(image, (7, 7), 0)

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
    h_lower = 10
    h_upper = 20
    s_lower = 205
    s_upper = 255
    v_lower = 205
    v_upper = 255

    lower_color = np.array([h_lower, s_lower, v_lower])
    upper_color = np.array([h_upper, s_upper, v_upper])
    
    mask = cv2.inRange(hsv, lower_color, upper_color)

    contours, hierarchy = cv2.findContours(mask, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, contourIdx=-1, color=(255, 0, 0), thickness=2)

    for c in contours:
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(image, (cX, cY), 3, (0, 0, 255), -1)

        (x, y), radius = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))
        radius = int(radius)

        cv2.circle(image, center, 3, (0, 255, 0), -1)
        cv2.circle(image, center, radius, (0, 255, 0), 2)


    cv2.imshow('mask', mask)
    cv2.imshow('image', image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()