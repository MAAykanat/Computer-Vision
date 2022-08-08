### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
### https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

    ###NOTES###
    # Bitwise operation widely use in masking    
    ###SOURCES###
    
import cv2 as cv
import numpy as np

def main():

    blank = np.zeros((400,400), dtype="uint8")
    cv.imshow("Blank-Image", blank)

    rectangle = cv.rectangle(blank.copy(), (30,30), (250,250), color=255, thickness=-1)
    cv.imshow("Rectangle", rectangle)

    circle = cv.circle(blank.copy(), (200,200), radius=125, color=255, thickness=-1)
    cv.imshow("Circle", circle)

    #AND Opetaration --> Intersecting Areas
    bitwise_and = cv.bitwise_and(rectangle, circle)
    cv.imshow("Bw-AND", bitwise_and)

    #OR Operation --> Non-Intersecting and Intersecting Ares
    bitwise_or = cv.bitwise_or(rectangle, circle)
    cv.imshow("Bw-OR", bitwise_or)

    #XOR Opetation --> Non-Intersecting Areas
    bitwise_xor = cv.bitwise_xor(rectangle, circle)
    cv.imshow("Bw-XOR", bitwise_xor)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except:
        pass