import cv2

img = cv2.imread('coffee.jpg',cv2.IMREAD_COLOR)
print(len(img))
print(len(img[0]))


crop_img = img[100: 500, 85: 350]
cv2.imshow('image', crop_img)
#cv2.imwrite("eeffoc.jpg", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()