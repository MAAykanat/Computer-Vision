### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
### https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

    ###NOTES###
    
    ###SOURCES###
    ##Smoothing image OpencV##
    # https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
    #------------------------#
import cv2 as cv

def main():
    path = "put location to this string"

    img = cv.imread(path + "cats.jpg")
    cv.imshow("Original-Image", img)

    # Average Blur
    #             [ 1 1 1
    #   K = 1/9 *   1 1 1
    #               1 1 1 ]
    ## Taking average to m*m pixel by using (m,m) kernel 
    average_blur = cv.blur(img, (7,7))
    cv.imshow("Average-Blur", average_blur)

    # Gaussian Blur
    gaussian_blur = cv.GaussianBlur(img, (7,7), sigmaX=0)
    cv.imshow("Gaussian Blur", gaussian_blur)

    #Median Blur
    # It is very effective against salt-pepper noise
    # Takes median value of kernel 
    median_blur = cv.medianBlur(img, ksize=7)
    cv.imshow("Median-Blur", median_blur)

    #Bilateral Blur
    # Highly effective noise remove
    # Slower compared to others
    bilateral_filter = cv.bilateralFilter(img, 7, sigmaColor=40, sigmaSpace=40)
    cv.imshow("Bilateral-Filter", bilateral_filter)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except:
        pass    