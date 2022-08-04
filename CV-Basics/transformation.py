### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
###https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

    ###NOTES###

    ###SOURCES###
    #---------Image height-width---------#
    ##img.shape[1] is width img.shape[0] is height
    #---------Rotation-Tranlation---------#
    ## https://learnopencv.com/image-rotation-and-translation-using-opencv/
    #-----------------------------------#

import cv2 as cv
import numpy as np

def translate(img, x, y):
    #Translation means shifting pixels by using translation matrix M
    #       [ 1 0 tx
    # M =     0 1 ty ]
    # +x --> Right
    # -x --> Left
    # +y --> Up
    # -y --> Down
    transMat = np.float32([[1,0,x],[0,1,y]])    # Translation matrix
    dimensions = (img.shape[1], img.shape[0])   # Dimension of images
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint = None):
    # Rotation matrix is M defines generally as below
    #       [ cosΘ -sinΘ  
    # M =     sinΘ  cosΘ ]
    # α = scale * cosΘ
    # β = scale * sinΘ
    #       [ α β (1-α)*cx-β*cy
    #        -β α β*cx+(1-a)*cy ]
    # where cx and cy are rotation coordinates from rotPoint

    height, width = img.shape[0], img.shape[1]
    
    if rotPoint == None:
        rotPoint = (height//2,width//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

def main():
    path = "put location to this string"

    img = cv.imread(path + "Background_Subtraction_Tutorial_frame.png")
    cv.imshow("Original-Image", img)
    
    print("Image height is: {}\nImage width is: {}".format(img.shape[0], img.shape[1]))

    #Translation
    translate_img = translate(img, 100, 100)
    cv.imshow("Translated-Image", translate_img)
    #Rotation 
    rotate_img = rotate(img, 45)
    cv.imshow("Rotating Matrix", rotate_img)
    #Flipping
    flip = cv.flip(img, 1)
    cv.imshow("Flipping", flip)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except:
        pass