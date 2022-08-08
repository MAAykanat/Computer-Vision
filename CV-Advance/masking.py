### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
### https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

    ###NOTES###
    #  
    ###SOURCES###
    
import cv2 as cv
import numpy as np

def main():
    path = "put location to this string"

    img = cv.imread(path + "/cats.jpg")
    cv.imshow("Original-Image", img)

    blank = np.zeros(img.shape[:2], dtype="uint8")
    
    maskCircle = cv.circle(blank.copy(),center=(blank.shape[1]//2,blank.shape[0]//2),radius=120, color=255, thickness=-1)
    cv.imshow("Circle-Mask", maskCircle)

    masked_circle = cv.bitwise_and(img,img,mask=maskCircle)
    cv.imshow("C-Masked-Image", masked_circle)

    maskRectangle = cv.rectangle(blank.copy(), (100,100), (img.shape[1]-100,img.shape[0]-100), color=255, thickness=-1)
    cv.imshow("Rectangle-Mask", maskRectangle)

    masked_rectangle = cv.bitwise_and(img,img,mask=maskRectangle)
    cv.imshow("R-Masked-Image", masked_rectangle)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ =='__main__':
    try:
        main()
    except:
        pass