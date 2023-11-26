import cv2
import mediapipe as mp
import time
import handtrackingmodule as H_M
def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0
    detector = H_M.Handdetector()
    while True:
        success, img = cap.read()
        img = detector.drawhands(img)
        lmlist=detector.landmarks_cord(img)
        if len(lmlist)!=0:
            print(lmlist[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 0), 2)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()