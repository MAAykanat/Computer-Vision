
import cv2 as cv
import os

def main():
    path = "D:/!!!MAAykanat Dosyalar/MAA_Own_Study/Usable Data"
    img = cv.imread(path + "/data/rubberwhale1.png")
    cv.imshow("Fruits-original", img) 

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray-Image", gray)

    # Simple Tresholding
    threshold, thresh = cv.threshold(gray, thresh=125 , maxval= 255, type=cv.THRESH_BINARY_INV)
    cv.imshow("Thresholding-Image", thresh)
    print("Threshold value is: ", threshold)

    # Adaptive Thresholding
    adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 3, 7)
    cv.imshow("Adaptive-Treshold", adaptive_thresh)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except:
        pass