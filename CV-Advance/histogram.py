
from turtle import title
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def plotGraph(figure, title, xlab, ylab, xlim):
    plt.figure()
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xlim)
    plt.plot(figure)
    plt.show()

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

    plotGraph(figure=gray_hist, title="Gray-Scale Histogram", xlab="Bins", ylab="# of pixels", xlim=[0,256])

    #BGR Histogram
    img_hist = cv.calcHist([img], [2], mask=None, histSize=[256], ranges=[0,256])

    plotGraph(figure=img_hist, title="BGR Histogram", xlab="Bins", ylab="# of pixels", xlim=[0,256])

    cv.waitKey()
    cv.destroyAllWindows()

if __name__=='__main__':
    try:
        main()
    except:
        pass