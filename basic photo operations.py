import cv2 as cv

img_path ="./images/sherlock_kid.png"

img = cv.imread(img_path)

# cv.imshow('kid',img)

# print(img)
# print(img.shape)

img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)

#Have to put different title name else it wont work
# cv.imshow("Image",img)
# cv.imshow("Gray_Image",img_gray)
# cv.imshow("HSV_Image",img_hsv)

# cv.imwrite("./images/sherlock_kid_gray.png",img_gray)
# cv.imwrite("./images/sherlock_kid_HSV.png",img_hsv)
# print(img.shape)
# print(img_gray.shape)

# img_resized= cv.resize(img_gray, (500,500))
# cv.imshow("Resized image",img_resized)

# img_cropped = img[:,300:]
# cv.imshow("Cropped_Image",img_cropped)

cv.waitKey(0)