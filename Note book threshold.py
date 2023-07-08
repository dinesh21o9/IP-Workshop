import cv2

img_path='images/book_page.jpg'
img=cv2.imread(img_path)
book_page_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("IMAGE",img)

thresh_val,thresh_img=cv2.threshold(book_page_img,127,255,cv2.THRESH_OTSU)
print(thresh_val)
cv2.imshow("B/w Filter",thresh_img)
cv2.waitKey(0)