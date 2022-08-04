### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
###https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

    ###NOTES###
    # In this example it looks like canny is better contours compared to tresholding
    # However,in general view, for common cases tresholding is more usefull 
    ###SOURCES###
    #---------Contour Approximation Method--------#
    ## https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
    #-----------------------------------#

import cv2 as cv
import numpy as np

def main():
    path = "put location to this string"
    
    img = cv.imread(path + "Background_Subtraction_Tutorial_frame_1.png")
    cv.imshow("Original Image", img)

    print("Image height is: {}\nImage width is: {}".format(img.shape[0], img.shape[1]))

    blank = np.zeros(img.shape, dtype="uint8")
    cv.imshow("Blank", blank)

    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cv.imshow("Gray Image", gray)

    blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
    cv.imshow("Blur", blur)

    cv.destroyAllWindows()

    canny = cv.Canny(blur, 125, 200)
    cv.imshow("Edges of Image-Canny", canny)

    ret, tresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
    cv.imshow("Edge of Image-Tresh", tresh)

    contours_canny, hierarchies_canny = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print("\nCanny contours number is: ",len(contours_canny))

    contours_tresh, hierarchies_tresh = cv.findContours(tresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print("\nTresh contours number is: ",len(contours_tresh))

    cv.drawContours(blank, contours_canny, -1, (0,0,255), 1)
    cv.imshow("Canny-Draw", blank)

    cv.drawContours(blank, contours_tresh, -1, (0,255,0), 1)
    cv.imshow("Tresh-Draw", blank)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except:
        pass