### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
###https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

#This code has some basics about Image Procesing from OpenCv link is below
#-----------------------------------------------------------------------------#
#https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html
#-----------------------------------------------------------------------------#

import cv2 as cv
import numpy as np
global kernel 
# kernel = np.ones((3,3),np.uint8)
kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
# kernel = np.array(kernel).reshape(3,3) 
# kernel = np.ones((5,5), dtype=np.uint8)

def main():
    path = "/home/maaykanat/Desktop/OwnStudy/Usable Data"

    print(kernel)
    img = cv.imread(path+ "/minions.jpg")
    cv.imshow("Board", img)
    
    # Resizing
    resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
    cv.imshow("Resized-board", resized)
    
    # Converting GrayScale
    gray = cv.cvtColor(resized, cv.COLOR_RGB2GRAY) 
    cv.imshow("Board-Gray", gray)

    # Blur
    blur =cv.GaussianBlur(resized, (5,5), cv.BORDER_DEFAULT) # It is bluring image before Canny
    cv.imshow("Blur-board", blur)

    #Edge Cascade
    canny = cv.Canny(blur, 0, 100) # Finding edges from image
    cv.imshow("Canny", canny)

    # Dialete
    dilated = cv.dilate(canny,(3,3), iterations=3) # Dilate the edges from Canny
    # dilated = cv.dilate(canny, kernel, iterations=3)
    cv.imshow("Dilated", dilated)

    #Eroding
    eroded = cv.erode(dilated, (5,5), iterations=3)
    # eroded = cv.erode(dilated, kernel, iterations=3)
    cv.imshow("Eroded", eroded)
    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except:
        pass