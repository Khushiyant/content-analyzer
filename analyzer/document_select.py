import cv2
import numpy as np
import utlis


class perspective:
    def __init__(self, img):
        # utils.initialiseTrackbars()
        self.OriginalCopy = img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # thres = utils.valTrackbars()
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        canny = cv2.Canny(blur, 120, 120)
        kernel = np.ones((5, 5))
        dial = cv2.dilate(canny, kernel, iterations=2)
        canny = cv2.erode(dial, kernel, iterations=1)

        self.finalImg = self.getContours(canny, self.OriginalCopy)

    def returnImg(self):
        if self.finalImg.all() == self.OriginalCopy.all() :   # Checking for empty image
            return [self.finalImg, True]
        else:
            return [self.finalImg, False]

    def display(self, img):
        cv2.imshow("Output", img)

    def getContours(self, imgThreshold, img):

        ############################

        imgBigContour, imgContours, imgWarpGray = img.copy(), img.copy(), img.copy()
        widthImg = 640
        heightImg = 480

        ############################

        contours, _ = cv2.findContours(
            imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)
        biggest, maxArea = utlis.biggestContour(
            contours)  # FIND THE BIGGEST CONTOUR
        if biggest.size != 0:
            biggest = utlis.reorder(biggest)
            # DRAW THE BIGGEST CONTOUR
            cv2.drawContours(imgBigContour, biggest, -1, (0, 255, 0), 20)
            imgBigContour = utlis.drawRectangle(imgBigContour, biggest, 2)
            pts1 = np.float32(biggest)  # PREPARE POINTS FOR WARP
            pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [
                              widthImg, heightImg]])  # PREPARE POINTS FOR WARP
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgWarpColored = cv2.warpPerspective(
                img, matrix, (widthImg, heightImg))

            # REMOVE 20 PIXELS FORM EACH SIDE
            imgWarpColored = imgWarpColored[20:imgWarpColored.shape[0] -
                                            20, 20:imgWarpColored.shape[1] - 20]
            imgWarpColored = cv2.resize(imgWarpColored, (widthImg, heightImg))

            # APPLY ADAPTIVE THR ESHOLD
            imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
            imgAdaptiveThre = cv2.adaptiveThreshold(
                imgWarpGray, 255, 1, 1, 7, 2)
            imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
            imgAdaptiveThre = cv2.medianBlur(imgAdaptiveThre, 3)

        return imgWarpGray
