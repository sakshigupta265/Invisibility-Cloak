import cv2
import numpy as np

camera = cv2.VideoCapture(0)
back = cv2.imread("background.jpg")

while camera.isOpened():
    # read each frame
    ret, frame = camera.read()

    if ret:
        # 1. convert the frame from bgr to hsv
        hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # 2. bgr value for red
        red = np.uint8([[[0,0,255]]])

        # 3. red in hsv
        red_hsv = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)

        # 4. determine threshold values to detect red color: detect shades
        # lower: hue - 10, 100, 100, higher: hue + 10, 255, 255

        lower_val_1 = np.array([0,100,100])
        higher_val_1 = np.array([100,255,255])

        lower_val_2 = np.array([155, 100, 100]) 
        higher_val_2 = np.array([180, 255, 255])

        #5. MASK: detecting red color only
        mask1 = cv2.inRange(hsv_frame, lower_val_1, higher_val_1) 
        mask2 = cv2.inRange(hsv_frame, lower_val_2, higher_val_2)

        mask = mask1 + mask2

        # 6. Refining the mask
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
        mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations = 1) 
        
        # 7. ANTI-MASK: detecting all colors except red
        anti_mask = cv2.bitwise_not(mask) 

        # 8. Let the magic begin
        part1 = cv2.bitwise_and(back,back,mask = mask)
        part2 = cv2.bitwise_and(frame,frame,mask = anti_mask)

        cloak = part1 + part2

        cv2.imshow("cloak",cloak)

        if cv2.waitKey(5) == ord('q'):
          break 

camera.release()
cv2.destroyAllWindows