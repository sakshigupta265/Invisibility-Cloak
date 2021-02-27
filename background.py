# capture the background

import cv2  # import computer vision

camera = cv2.VideoCapture(0) # initialise your camera

while camera.isOpened():
    ret, back = camera.read()      
    # ret: return true if camera is able to read
    # back: gives the image read by the camera

    if ret:
        cv2.imshow("background",back) # show the input read by the camera
        if cv2.waitKey(5) == ord('x'): 
            # ord gives the unicode value of 'x'
            # when x is pressed an image is captured and after a wait time of 5ms

            cv2.imwrite("background.jpg",back) # save the image captured
            break 

camera.release()    # release the camera (dislinking the camera)
cv2.destroyAllWindows # close all windows