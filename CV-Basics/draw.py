from tokenize import blank_re
import cv2 as cv
from cv2 import imshow
from cv2 import waitKey
from cv2 import FILLED
import numpy as np  


def main():
    path = "put location to this string"
    
    blank_img = np.zeros((500,500,3), dtype='uint8') #Create blank image default value 0
    blank_circle = np.zeros((500,500,3), dtype= 'uint8')
    blank_line = np.zeros((500,500,3), dtype='uint8')
    blank_opencv_basics = np.zeros((800,600,3), dtype='uint8')
    cv.imshow("Blank-Image", blank_img)

    img = cv.imread(path + "/house.jpg")
    cv.imshow("House-Image", img)
    #waitKey(0)

    #1. Paint the image a certain colour
    blank_img[200:300, 300:400] = 0,0,255 # Put red square to to blank image
    cv.imshow("Red-Blank", blank_img)
    #waitKey(0)

    #2. Draw a Rectangle
    # cv.rectangle(blank_img, (0,0), (250,500), (0,255,0), thickness=2) #Thickness is 2
    # cv.rectangle(blank_img, (0,0), (250,500), (0,255,0), thickness=cv.FILLED) # Fill the all rectangle
    cv.rectangle(blank_img, (0,0), (blank_img.shape[1]//2, blank_img.shape[0]//2), (0,255,0), thickness = FILLED) # Half of original blank image
    cv.imshow("Put a Rectangle",blank_img)

    #3. Draw a circle
    cv.circle(blank_circle, (blank_circle.shape[1]//2, blank_circle.shape[0]//2), 40, (0,0,255), thickness=5)
    cv.imshow("Put a Circle", blank_circle)
    
    #4. Draw a line
    cv.line(blank_line, (0,0), (blank_line.shape[1]//2, blank_line.shape[0]//2), (0,0,255) ,thickness= 3)
    cv.imshow("Put a Line", blank_line)

    #5. Put a Text
    cv.putText(blank_img, 'Hello', (255,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.imshow("Put text", blank_img)
    waitKey(0)

    cv.destroyAllWindows()# Close all windows before last work

    cv.putText(blank_opencv_basics, 'OpenCV Basics', (blank_opencv_basics.shape[1]//2-100,blank_opencv_basics.shape[0]//2-100), cv.FONT_HERSHEY_COMPLEX, fontScale=0.8, color=(125,255,125), thickness=2)
    cv.rectangle(blank_opencv_basics, (blank_opencv_basics.shape[1]//2-100,blank_opencv_basics.shape[0]//2-140), (blank_opencv_basics.shape[1]//2+100, blank_opencv_basics.shape[0]//2-80), (255,120,120), thickness=2)
    #Let's put target board :)
    cv.circle(blank_opencv_basics, (blank_opencv_basics.shape[1]//2, blank_opencv_basics.shape[0]//2), radius=10, color=(0,0,255), thickness=5)
    cv.circle(blank_opencv_basics, (blank_opencv_basics.shape[1]//2, blank_opencv_basics.shape[0]//2), radius=20, color=(255,255,255), thickness=5)
    cv.circle(blank_opencv_basics, (blank_opencv_basics.shape[1]//2, blank_opencv_basics.shape[0]//2), radius=30, color=(0,0,255), thickness=5)
    cv.circle(blank_opencv_basics, (blank_opencv_basics.shape[1]//2, blank_opencv_basics.shape[0]//2), radius=40, color=(255,255,255), thickness=5)
    cv.circle(blank_opencv_basics, (blank_opencv_basics.shape[1]//2, blank_opencv_basics.shape[0]//2), radius=50, color=(0,0,255), thickness=5)
    #Let's put some arrow :)
    cv.line(blank_opencv_basics, (0, 800), (150,600), color=(0,0,255), thickness=3)
    cv.line(blank_opencv_basics, (150,600), (100,600), color=(0,0,255), thickness=3)
    cv.line(blank_opencv_basics, (150,600), (150,650), color=(0,0,255), thickness=3)
    cv.imshow("OpenCV Basics",blank_opencv_basics)
    waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except:
        pass