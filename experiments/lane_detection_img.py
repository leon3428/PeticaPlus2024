import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def find_lane_center(frame, detection_line, offset):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray, (15,15), 0)

    height, width, _ = frame.shape
    detection_line = 380
    offset = 20

    line_intensity = blur[detection_line - offset : detection_line + offset, :]
    line_intensity = np.mean(line_intensity, axis=0)

    kernel1_size = 15
    kernel1 = cv2.getGaussianKernel(kernel1_size, 8).squeeze()
    print(kernel1)
    smooth_line_intensity = np.correlate(line_intensity, kernel1)

    x = list(range(width))
    plt.plot(x, line_intensity)  
    plt.show()
    plt.plot(x[kernel1_size // 2:-(kernel1_size // 2)], smooth_line_intensity)
    plt.show()

    kernel2 = [-1, 0, 1]
    derivative = np.correlate(smooth_line_intensity, kernel2)

    plt.plot(x[kernel1_size // 2 + 1:-(kernel1_size // 2 + 1)], derivative)
    plt.show()

    right = np.argmin(derivative[ width // 2 : ]) + width // 2 + kernel1_size // 2 + 1
    left = np.argmax(derivative[ : width // 2 ]) + kernel1_size // 2 + 1
    middle = (left + right) // 2

    return left, middle, right

def main():
    matplotlib.use('TKAgg')

    detection_line = 380
    offset = 20

    image = cv2.imread('assets/cesta3.png')

    height, width, _ = image.shape

    left, middle, right = find_lane_center(image, detection_line, offset)

    cv2.line(image, (0, detection_line), (width, detection_line), (255, 0, 0), 5)
    cv2.line(image, (left, detection_line - 20), (left, detection_line + 20), (0, 255, 0), 3)
    cv2.line(image, (right, detection_line - 20), (right, detection_line + 20), (0, 255, 0), 3)
    cv2.circle(image, (int(middle), detection_line), 20, (0, 0, 255), -1)
    cv2.imshow('Frame', image)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()