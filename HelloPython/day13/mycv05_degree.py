import cv2

img = cv2.imread('coffee.jpg',cv2.IMREAD_COLOR)

height, width, channel = img.shape
rotateImg = cv2.getRotationMatrix2D((width/2, height/2),10,1)
dst = cv2.warpAffine(img, rotateImg, (width, height))

cv2.imshow('image', dst)
cv2.imwrite("coffee_rotate.jpg", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()