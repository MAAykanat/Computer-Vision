# Used dataset |
# Name: 5 Celebrity Faces Dataset
# Link: https://www.kaggle.com/datasets/dansbecker/5-celebrity-faces-dataset

import cv2 as cv
import numpy as np

def main():
    path = "D:\!!!MAAykanat Dosyalar\MAA_Own_Study\CV-Data\Face-Recognation\\val"

    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    people = ['ben_afflek', 'elton_john', 'jerry_seinfeld', 'madonna', 'mindy_kaling']

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('face_trained.yml')

    img = cv.imread(path + "\\ben_afflek\httpcsvkmeuadecafjpg.jpg")

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Person', gray)

    # Detect the face in the image
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h,x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')

        cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Face', img)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=='__main__':
    try:
        main()
    except:
        pass