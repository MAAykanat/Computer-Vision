### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
### https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

import cv2 as cv
from cv2 import imshow
import numpy as np

def main():
    path = "put location to this string"
    
    #Original image is BGR 3 channel image
    img = cv.imread(path + "Background_Subtraction_Tutorial_frame.png")
    cv.imshow("Original Image", img)
    print("Shape of image is: ", img.shape) # Image height: 576, width: 768, channel:3

    blank = np.zeros(img.shape[:2], dtype="uint8")
    cv.imshow("Blank", blank)

    b,g,r = cv.split(img)

    merged = cv.merge([b,g,r])
    cv.imshow("Merged Image", merged)

    blue = cv.merge([b,blank,blank])
    green= cv.merge([blank,g,blank])
    red = cv.merge([blank,blank,r])

    imshow("Blue-Channel", blue)
    imshow("Green-Channel", green)
    imshow("Red-Channel", red)

    merged2original = cv.merge([blue, green ,red])
    imshow("Merged2Original", merged2original)

    cv.waitKey(0)
    cv.destroyAllWindows()
 
if __name__ == '__main__':
    try:
        main()
    except:
        pass