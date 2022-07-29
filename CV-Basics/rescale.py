### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
###https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

    ###NOTES###

    ###SOURCES###
    #---------cv.INTER_AREA---------#
    #https://medium.com/@wenrudong/what-is-opencvs-inter-area-actually-doing-282a626a09b3
    #-------------------------------#

from multiprocessing.connection import wait
import cv2 as cv
from cv2 import waitKey
from cv2 import imshow
from outcome import capture


def rescaleFrame(frame, scale= 0.75):
    #Rescale image function with 0.75 default
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (height, width)
    


    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def main():
    path = "D:/!!!MAAykanat Dosyalar/MAA_Own_Study/Usable Data/Computer Vision"

    img = cv.imread(path + "/WaldoBeach.jpg")    
    img_resized = rescaleFrame(img)

    imshow("WaldoBeach", img)
    imshow("WaldoBeach-Resized", img_resized) # Resized Image
    
    waitKey(0)
    
    capture = cv.VideoCapture(path + '/Background_Subtraction_Tutorial_frame.mp4')
    
    while True:
        isTrue, frame = capture.read()

        frame_resized = rescaleFrame(frame, 0.25)
        cv.imshow('Tutorial-Video', frame)
        cv.imshow('Tutorial-Video-Resized', frame_resized) # Resized Video

        if cv.waitKey(20) & 0xFF==ord('q'):
            #Wait till the and or press q to exit
            break
    
    capture.release() #Stop capturing video frames
    cv.destroyAllWindows() # Close all  windows


if __name__ == '__main__':
    try:
        main()
    except:
        pass