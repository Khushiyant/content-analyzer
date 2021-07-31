import cv2
import numpy as np

class perspective:
    def __init__(self, img):
        # utils.initialiseTrackbars()
        OriginalCopy = img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # thres = utils.valTrackbars()
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        canny = cv2.Canny(blur, 120, 120)
        kernel = np.ones((5,5))
        dial = cv2.dilate(canny,kernel,iterations=2)
        canny = cv2.erode(dial,kernel,iterations=1)


        self.getContours(canny, OriginalCopy)
        self.display(canny)

    def display(self, img):
        cv2.imshow("Output", img)

    def getContours(self, img, imgShow):
        contours, _ = cv2.findContours(
            img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(imgShow,contours,-1,(0,255,0),10)
        # for c in contours:
            # area = cv2.contourArea(c)
            # if area > 500:
            #     peri = cv2.arcLength(c, True)
            #     approxDP = cv2.approxPolyDP(c, 0.02*peri, True)
            #     # print(len(approxDP))
            #     sides = len(approxDP)
            #     x, y, w, h = cv2.boundingRect(approxDP)
            #     cv2.rectangle(imgShow, (x, y), (x+w, y+h), (255, 0, 0), 2)
