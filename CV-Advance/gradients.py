
import cv2 as cv
import numpy as np

def main():
    path ="D:/!!!MAAykanat Dosyalar/MAA_Own_Study/Usable Data"
    
    img = cv.imread(path + "/data/building.jpg")
    cv.imshow("Original-Image", img)

    img = cv.resize(img, (int(img.shape[1]*0.75), int(img.shape[0]*0.75)))

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)

    #Laplacian
    lap = cv.Laplacian(gray, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))
    cv.imshow("Laplacian",lap)

    #Sobel
    sobelx =cv.Sobel(gray, cv.CV_64F, 1, 0)
    sobely =cv.Sobel(gray, cv.CV_64F, 0, 1)
    combined_sobel = cv.bitwise_or(sobelx, sobely)
    cv.imshow("Combined Sobel", combined_sobel)

    #Canny
    canny= cv.Canny(gray, 200, 220)
    cv.imshow("Canny", canny)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__=='__main__':
    try:
        main()
    except:
        pass