import cv2
import numpy as np

def nothing(x):
    pass

def main():
    image = cv2.imread('assets/loptica.png')

    height, width, _ = image.shape
    blurred = cv2.GaussianBlur(image, (7, 7), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)

    cv2.createTrackbar('Hue Lower', 'image', 0, 179, nothing)
    cv2.createTrackbar('Hue Upper', 'image', 179, 179, nothing)
    cv2.createTrackbar('Saturation Lower', 'image', 0, 255, nothing)
    cv2.createTrackbar('Saturation Upper', 'image', 255, 255, nothing)
    cv2.createTrackbar('Value Lower', 'image', 0, 255, nothing)
    cv2.createTrackbar('Value Upper', 'image', 255, 255, nothing)


    while True:
        h_lower = cv2.getTrackbarPos('Hue Lower', 'image')
        h_upper = cv2.getTrackbarPos('Hue Upper', 'image')
        s_lower = cv2.getTrackbarPos('Saturation Lower', 'image')
        s_upper = cv2.getTrackbarPos('Saturation Upper', 'image')
        v_lower = cv2.getTrackbarPos('Value Lower', 'image')
        v_upper = cv2.getTrackbarPos('Value Upper', 'image')
        
        lower_color = np.array([h_lower, s_lower, v_lower])
        upper_color = np.array([h_upper, s_upper, v_upper])
        
        mask = cv2.inRange(hsv, lower_color, upper_color)
        
        res = cv2.bitwise_and(image, image, mask=mask)
        combined = np.hstack([image, res])
        cv2.imshow('image', combined)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()