### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
### https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

    ###NOTES###
    #------------1-------------#
    # OpenCv uses BGR as default and knows opened image as same as shown in folder
    # On the other hand matplotlib uses RGB thats why they show different.
    # Try= plt.imshow(img) \n plt.show()
    #------------2-------------#
    # There is no direct convert HSV2Gray or LAB2Gray,
    # First, Convert HSV2BGR then BGR2GRAY
    #--------------------------#
    ###SOURCES###
    #---------Color-Spaces Advantages-Disadvantages---------#
    # There are many research about this topic, please check Research-Source file to details.
    # Clarification table: Advantages-and-disadvantages-of-color-spaces.png
    # Referans: Garcia-Lamont, F., Cervantes, J., López, A., & Rodriguez, L. (2018). Segmentation of images by color features: A survey. Neurocomputing, 292, 1-27.
    # Doi number:10.1016/j.neucom.2018.01.091
    #-----------------------------------#


import cv2 as cv
import matplotlib.pyplot as plt
def main():
    path = "/home/maaykanat/Desktop/OwnStudy/Usable Data/data/"

    img = cv.imread(path + "starry_night.jpg")
    cv.imshow("Original Image", img)

    # plt.imshow(img)
    # plt.show() 

    #BGR to GrayScale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)

    #BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow("HSV", hsv)

    #BGR to L*a*b
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    cv.imshow("L*a*b", lab)

    # BGR to RGB
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow("RGB", rgb)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except:
        pass