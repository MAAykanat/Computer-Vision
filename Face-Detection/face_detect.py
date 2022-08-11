import cv2 as cv

path = "D:/!!!MAAykanat Dosyalar/MAA_Own_Study/CV-Data/Face-Detection"

img = cv.imread(path + '/foto.png')
cv.imshow('Original Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

haar_cascade = cv.CascadeClassifier('D:\!!!MAAykanat Dosyalar\MAA_Own_Study\Computer Vision\Face-Detection\haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)



cv.waitKey(0)