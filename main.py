# pip install --force-reinstall --no-cache -U opencv-python==4.5.5.62
# pip install --force-reinstall --no-cache -U opencv-python==4.6.0.66
import cv2

if __name__ == '__main__':
    # Load image
    img = cv2.imread('test.jpg')

    if img is None:
        print('Bild nicht gefunden')

    # Show image
    cv2.imshow('image', img)

    cv2.waitKey()
