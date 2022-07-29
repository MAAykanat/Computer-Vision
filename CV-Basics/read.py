### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
###https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

import cv2 as cv
from cv2 import waitKey



def main():
    path = "put location to this string" # Give your dataset path location

    img = cv.imread(path + "/house.jpg") #Read images

    cv.imshow('house',img) # Show in window
    waitKey(0) #Wait to key to press

    capture = cv.VideoCapture(path + '/Background_Subtraction_Tutorial_frame.mp4')
    
    while True:
        isTrue, frame = capture.read()
        cv.imshow('Tutorial-Video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    
    capture.release()
    cv.destroyAllWindows()

if __name__=='__main__':
    try:
        main()
    except:
        pass