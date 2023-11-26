import cv2
import numpy as np
import handtrackingmodule as H_M
import time
import autopy
wCam,Hcam=640,480
cap=cv2.VideoCapture(1)
cap.set(3,wCam)
cap.set(4,Hcam)
pTime=0
frameR=100
smoothening = 7
plocX, plocY = 0, 0
clocX, clocY = 0, 0
wScr, hScr = autopy.screen.size()
detector=H_M.Handdetector()


while True:
    success,img=cap.read();
    img = detector.drawhands(img)
    lmlist ,box= detector.Cord_with_box(img)
    if len(lmlist):
        xi, yi = lmlist[8][1:]
        xm, ym = lmlist[12][1:]
        fingers=detector.fingerspos()
        print(fingers)
        if fingers[1]==1 and fingers[2]==0:
            cv2.rectangle(img, (frameR, frameR), (wCam- frameR, Hcam-frameR),
                          (255, 0, 255), 2)
            xp=np.interp(xi,(frameR,wCam-frameR),(0,wScr))
            yp=np.interp(yi,(frameR,Hcam-frameR),(0,hScr))
            clocX = plocX + (xp- plocX) / smoothening
            clocY = plocY + (yp-plocY) / smoothening
            autopy.mouse.move(wScr-clocX, clocY)
            cv2.circle(img, (xi, yi), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        if fingers[1] == 1 and fingers[2] == 1:
            length,img,info=detector.findDistance(8,12,img)
            print(length)
            if length<30:
                cv2.circle(img, (info[4], info[5]),
                           10, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (40, 40), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
