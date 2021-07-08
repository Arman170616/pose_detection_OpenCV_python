#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:38:25 2021

@author: pyarena
"""


import cv2
import time
import poseModule as pm

cap = cv2.VideoCapture('/home/pyarena/python/OpenCV/poseDetection/pose1.mp4')
pTime=0
detector = pm.poseDetection()
    
while True: 
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPostion(img, draw=False)
    print(lmList[14])
    cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0,0, 250), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
   
    cv2.imshow("pose detection", img)
        
    if cv2.waitKey(40) == ord("q"):
        break
