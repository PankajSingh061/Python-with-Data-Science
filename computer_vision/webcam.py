import cv2
import numpy as np

#Create a vedioCapture object
webcam_idx=0
cam=cv2.VideoCapture(webcam_idx)
while cam.isOpened():
  #capture image from camera
  state,image=cam.read()
  if not state: break #if state is none thenbreak loop
  #show image
  cv2.imshow('image',image)
  #wait for the key press
  key=cv2.waitKey(10)
  #if ecs key is pressed, exit loop
  if key==27:
    break

#release camera
cam.release()
cv2.destroyAllWindows()