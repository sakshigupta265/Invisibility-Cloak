import cv2

camera = cv2.VideoCapture(0)

while camera.isOpened():
    ret, back = camera.read()

    if ret:
        cv2.imshow("background",back)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite("background.jpg",back)
            break

camera.release()
cv2.destroyAllWindows