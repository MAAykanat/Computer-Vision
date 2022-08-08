
from turtle import title
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def main():
    path = "/home/maaykanat/Desktop/OwnStudy/Usable Data"

    img = cv.imread(path + "/data/fruits.jpg")
    cv.imshow("Original-Image", img)

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Gray-Image", gray)

    blank = np.zeros(img.shape[:2], dtype='uint8')
    cv.imshow("Blank", blank)

    #Gray-Scale Histogtam
    gray_hist = cv.calcHist([gray], [0], mask=None,histSize=[256],ranges=[0,256])

    plt.figure()
    plt.title("Gray-Scale Histogram"),
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    plt.xlim([0,256])
    plt.plot(gray_hist)
    plt.show()

    #BGR Histogram
    img_hist = cv.calcHist([img], [2], mask=None, histSize=[256], ranges=[0,256])

    plt.figure()
    plt.title("BGR Histogram"),
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    plt.xlim([0,256])
    plt.plot(img_hist)
    plt.show()    

    cv.waitKey()
    cv.destroyAllWindows()

if __name__=='__main__':
    try:
        main()
    except:
        pass