
from turtle import title
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os


def plotGraph(figure, title, xlab, ylab, xlim, savePath):
    plt.figure()
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xlim)
    plt.plot(figure)
    plt.savefig(savePath)

def main():
    path = "/home/maaykanat/Desktop/OwnStudy/Usable Data"
    savePath= os.getcwd() + "/CV-Advance/Histogram-Results"

    img = cv.imread(path + "/data/fruits.jpg")
    cv.imshow("Original-Image", img)

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Gray-Image", gray)

    blank = np.zeros(img.shape[:2], dtype='uint8')
    cv.imshow("Blank", blank)

    mask = cv.circle(blank, center=(blank.shape[1]//2, blank.shape[0]//2), radius=120, color=255, thickness=-1)

    # masked = cv.bitwise_and(img,img, mask=mask)
    # cv.imshow("Masked", masked)

    #Gray-Scale Histogtam
    gray_hist = cv.calcHist([gray], [0], mask=None,histSize=[256],ranges=[0,256])
    gray_hist_mask = cv.calcHist([gray], [0], mask=mask,histSize=[256],ranges=[0,256])

    plotGraph(figure=gray_hist, title="Gray-Scale Histogram", xlab="Bins", ylab="# of pixels", xlim=[0,256], savePath=savePath+"/Gray-Scale Histogram.png")
    plotGraph(figure=gray_hist_mask, title="Masked Gray-Scale Histogram", xlab="Bins", ylab="# of pixels", xlim=[0,256], savePath=savePath+"/Masked Gray-Scale Histogram.png")

    #BGR Histogram
    img_hist = cv.calcHist([img], [2], mask=None, histSize=[256], ranges=[0,256])
    img_hist_mask = cv.calcHist([img], [2], mask=mask, histSize=[256], ranges=[0,256])

    plotGraph(figure=img_hist, title="BGR Histogram", xlab="Bins", ylab="# of pixels", xlim=[0,256], savePath=savePath+"/BGR Histogram.png")
    plotGraph(figure=img_hist_mask, title="Mask-BGR Histogram", xlab="Bins", ylab="# of pixels", xlim=[0,256], savePath=savePath+"/Masked BGR Histogram.png")
    
    cv.waitKey()
    cv.destroyAllWindows()

if __name__=='__main__':
    try:
        main()
    except:
        pass