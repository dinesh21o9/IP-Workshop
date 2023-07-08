import cv2
from matplotlib.pyplot import gray
import numpy as np

img_path='images/gray_scale.png'
img=cv2.imread(img_path)
gray_scale_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("IMAGE",img)

# _,thresh_img=cv2.threshold(gray_scale_img,127,255,cv2.THRESH_BINARY)
# cv2.imshow("Thresh Img",thresh_img)

thresh_img=np.full(img.shape ,255, dtype=np.uint8)
(h,w)=gray_scale_img.shape

for i in range(0,h):
    for j in range(0,w):
        if gray_scale_img[i,j]>127:
            thresh_img[i,j]=255
        else:
            thresh_img[i,j]=0

cv2.imshow("Thresh Img",thresh_img)

cv2.waitKey(0)