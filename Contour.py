import numpy as np
import cv2

def nothing(x):
    pass

def createTrackbar():
    cv2.namedWindow("thresholding")
    cv2.resizeWindow('thresholding',720,400)
    cv2.createTrackbar("T","thresholding",0,255,nothing)
    cv2.createTrackbar("H_min","thresholding",0,255,nothing)
    cv2.createTrackbar("H_max","thresholding",0,255,nothing)
    cv2.createTrackbar("S_min","thresholding",0,255,nothing)
    cv2.createTrackbar("S_max","thresholding",0,255,nothing)
    cv2.createTrackbar("V_min","thresholding",0,255,nothing)
    cv2.createTrackbar("V_max","thresholding",0,255,nothing)

# def track1():
#     cv2.namedWindow("track1")
#     cv2.createTrackbar("t1","track1",0,255,nothing)

img = cv2.imread('images/hand.jpg')
cv2.imshow("original image",img)
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray scale img",gray_scale)


createTrackbar()
# track1()

while True:
    T=cv2.getTrackbarPos("T","thresholding")
    H_min=cv2.getTrackbarPos("H_min","thresholding")
    S_min=cv2.getTrackbarPos("S_min","thresholding")
    V_min=cv2.getTrackbarPos("V_min","thresholding")
    H_max=cv2.getTrackbarPos("H_max","thresholding")
    S_max=cv2.getTrackbarPos("S_max","thresholding")
    V_max=cv2.getTrackbarPos("V_max","thresholding")

    # print(T)
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lower=np.array([H_min,S_min,V_min])
    upper=np.array([H_max,S_max,V_max])
    
    thresh_img=cv2.inRange(img,lower,upper)
    
    cv2.imshow("thresh img",thresh_img)

    imgCopy=img.copy()
    contours,_=cv2.findContours(thresh_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgCopy,contours,-1,(255,0,0),2)

    cv2.imshow("original image",imgCopy)




    key=cv2.waitKey(1)
    if(key==ord('q')):
        break
# _,thresh_img = cv2.threshold(gray_scale,126,255,cv2.THRESH_BINARY)  
# cv2.imshow("thresh img",thresh_img)
cv2.destroyAllWindows()
# cv2.waitKey(0)