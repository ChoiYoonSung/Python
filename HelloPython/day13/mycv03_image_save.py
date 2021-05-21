import cv2

img = cv2.imread('coffee.jpg',cv2.IMREAD_COLOR)
print(img)
cv2.imwrite('eeffoc.jpg',img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()