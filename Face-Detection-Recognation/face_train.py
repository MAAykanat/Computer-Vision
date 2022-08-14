import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

train_path = "Put train path here!"
people = ['ben_afflek', 'elton_john', 'jerry_seinfeld', 'madonna', 'mindy_kaling']

features=[]
labels=[]

# for i in os.listdir(train_path):
#     people.append(i)

def train():
    for person in people:
        path = os.path.join(train_path, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path, img)

            img_read = cv.imread(img_path)
            gray = cv.cvtColor(img_read, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for (x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

train()

print(f'# of features: {len(features)}')
print(f'# of labels: {len(features)}') 

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)