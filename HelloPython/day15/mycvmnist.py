import cv2
import numpy as np

arr2d = [
            [0,255,255,255,0]
            , [255,0,0,0,255]
            , [255,0,0,0,255]
            , [255,0,0,0,255]
            , [0,255,255,255,0]
        ]

arr2d_np = np.array(arr2d,np.uint8)
print(arr2d_np)
cv2.imshow('Test image', arr2d_np)
cv2.waitKey(0)
cv2.destroyAllWindows()