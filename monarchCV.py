import cv2
import numpy as np

img = cv2.imread("/home/pi/Desktop/monarch.jpg",1)

print (img.size)

print ("Opening image...")

cv2.imshow("Catepillar",img)

cv2.waitKey(5000)

print ("Closing image...")
cv2.destroyAllWindows()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (27, 150, 150), (33,255,255))
print("Opening image...")

cv2.imshow("mask",mask)


M = cv2.moments(mask)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

mask = cv2.blur(mask,(5,5))

print("Opening image...")

cv2.imshow("blurred mask",mask)

cv2.waitKey(5000)



thresh = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('monarch_thresh.png',thresh)
M = cv2.moments(thresh)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

#print ("Center: (%s , %s)", (cX, cY))

cv2.imshow("With Theshold",thresh)

cv2.waitKey(5000)

top = thresh[1:60, 1:400]

cv2.imshow("Top",top)

print=("Closing image...")
#cv2.destroyAllWindows()
