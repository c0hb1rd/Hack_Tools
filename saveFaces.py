#!/usr/bin/env python
# coding=utf-8
import cv2
import os
import Image
import sys

def detectFaces(imageName):
    img = cv2.imread(imageName)
    faceCascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    result = []
    for (x, y, width, height) in faces:
        result.append((x, y, x+width, y+height))
    return result

def saveFacees(imageName):
    faces = detectFaces(imageName)
    if faces:
        saveDir = imageName.split('.')[0] + '_faces'
        os.mkdir(saveDir)
        count = 0
        for (x1, y1, x2, y2) in faces:
            fileName = os.path.join(saveDir, str(count) + ".jpg")
            Image.open(imageName).crop((x1 - 20, y1 - 20 , x2 + 20, y2 + 20)).save(fileName)
            count += 1


saveFacees(sys.argv[1])
if detectFaces(sys.argv[1]) == []:
    print 'Have not faces'
else:
    print 'Have faces.'
    print detectFaces(sys.argv[1])
