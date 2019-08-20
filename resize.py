import cv2
import numpy as np

print ("Please enter path to image")

imagePath = input()
img = cv2.imread(imagePath)

curr_width = img.shape[1]
curr_height = img.shape[0]

print("Current width is:",curr_width)
print ("Please enter new width")
new_width = int(input())

print ("Please enter new width")
print("Current height is:",curr_height)
new_height = int(input())

smaller = cv2.resize(img, (new_width, new_height), interpolation = cv2.INTER_AREA)
cv2.imwrite('resized.jpg',smaller)
print("Resized image has been saved under /home/pi")
