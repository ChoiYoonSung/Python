import cv2
img = cv2.imread('coffee.jpg',cv2.IMREAD_GRAYSCALE)
print(img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()