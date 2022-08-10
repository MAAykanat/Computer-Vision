### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
### https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

    ###NOTES###
       
    ###SOURCES###

import cv2 as cv

def main():
    path = "D:/!!!MAAykanat Dosyalar/MAA_Own_Study/Usable Data"
    img = cv.imread(path + "/data/rubberwhale1.png")
    cv.imshow("Fruits-original", img) 

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray-Image", gray)

    blur = cv.GaussianBlur(img, ksize=(5,5),sigmaX=5,sigmaY=0, borderType=cv.BORDER_DEFAULT)
    cv.imshow("Blur-Image", blur)

    blur_gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # Simple Tresholding
    threshold, thresh = cv.threshold(gray, thresh=125 , maxval= 255, type=cv.THRESH_BINARY_INV)
    cv.imshow("Thresholding-Image", thresh)
    print("Threshold value is: ", threshold)

    threshold_blur, thresh_blur = cv.threshold(blur_gray, thresh=125 , maxval= 255, type=cv.THRESH_BINARY_INV)
    cv.imshow("Blur Thresholding-Image", thresh_blur)

    # Adaptive Thresholding
    adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 3, 7)
    cv.imshow("Adaptive-Treshold", adaptive_thresh)

    adaptive_thresh_blur = cv.adaptiveThreshold(blur_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 7, 7)
    cv.imshow("Blur Adaptive-Treshold", adaptive_thresh_blur)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except:
        pass