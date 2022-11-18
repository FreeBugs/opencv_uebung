# pip install --force-reinstall --no-cache -U opencv-python==4.5.5.62
# pip install --force-reinstall --no-cache -U opencv-python==4.6.0.66
import cv2

if __name__ == '__main__':
    # Load image
    img = cv2.imread('test.jpg')

    if img is None:
        print('Bild nicht gefunden')

    face_detector = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    if face_detector.empty():
        print('XML-Datei nicht geladen.')
        exit(1)

    faces = face_detector.detectMultiScale(img, 1.1, 4)

    for face in faces:
        x, y, w, h = face
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        rect_color = (0, 255, 255)  # B, G, R
        cv2.rectangle(img, top_left, bottom_right, rect_color, thickness=3)

    # Show image
    cv2.imshow('image', img)

    cv2.waitKey()
