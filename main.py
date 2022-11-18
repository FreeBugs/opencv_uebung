# pip install --force-reinstall --no-cache -U opencv-python==4.5.5.62
# pip install --force-reinstall --no-cache -U opencv-python==4.6.0.66
import cv2

def create_detector(filename):
    detector = cv2.CascadeClassifier(filename)
    if detector.empty():
        print('XML-Datei nicht geladen:', filename)
        exit(1)
    return detector

def draw_rects(img, rects, color):
    for r in rects:
        x, y, w, h = r
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        cv2.rectangle(img, top_left, bottom_right, color, thickness=3)

if __name__ == '__main__':
    # Load image
    img = cv2.imread('old_guy.png')

    if img is None:
        print('Bild nicht gefunden')

    face_detector = create_detector('haarcascade_frontalface_default.xml')
    eye_detector = create_detector('haarcascade_eye.xml')

    faces = face_detector.detectMultiScale(img, 1.1, 4)
    eyes = eye_detector.detectMultiScale(img, 1.1, 4)

    yellow = (0, 255, 255)
    blue = (255, 0, 0)

    draw_rects(img, faces, color=yellow)
    draw_rects(img, eyes, blue)


    # Show image
    cv2.imshow('image', img)

    cv2.waitKey()
