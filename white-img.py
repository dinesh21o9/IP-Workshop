import cv2
import numpy as np

img_path ="./images/sherlock_kid.png"
img = cv2.imread(img_path)

cv2.imshow("Image",img)
print(img.shape)

white_img=np.full(img.shape ,255, dtype=np.uint8)

# white_img = np.ones(img.shape)
# white_img=255*white_img


cv2.imshow("White Image",white_img)
# print(white_img.shape)
final=np.subtract(white_img,img)
# final= white_img - img
cv2.imshow("Sub Image",final)


cv2.waitKey(0)