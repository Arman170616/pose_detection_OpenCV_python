#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 07:23:38 2021

@author: pyarena
"""

import cv2
import mediapipe as mp
import time
   


class poseDetection():
    
    def __init__(self, mode=False, upBody=False, smooth=True, detectionConf=0.5, trackConf=0.5):
        
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionConf = detectionConf
        self.trackConf = trackConf
        


        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionConf, self.trackConf)
        
        
        
        #find pose
    def findPose(self, img, draw=True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
            
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        
        return img
                
          

            
            




    
    def  findPostion(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255,0, 150), cv2.FILLED)
        
        return lmList
    
    



def main():
    cap = cv2.VideoCapture('/home/pyarena/python/OpenCV/poseDetection/pose3.mp4')
    pTime=0
    detector = poseDetection()
    
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPostion(img, draw=False)
        #print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0,0, 250), cv2.FILLED)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
   
        cv2.imshow("pose detection", img)
        
        if cv2.waitKey(40) == ord("q"):
            break

    

if __name__ == '__main__':
    
    main()






cv2.destroyAllWindows()
#cap.release()

