import cv2
import numpy as np

img_path ="./images/sherlock_kid.png"
img = cv2.imread(img_path)

cv2.imshow("Image",img)
print(img.shape)

red_img=np.full(img.shape ,[0,0,50], dtype=np.uint8)

cv2.imshow("red Image",red_img)

final=np.add(red_img,img)

cv2.imshow("red+Image",final)
cv2.waitKey(0)