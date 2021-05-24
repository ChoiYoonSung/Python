# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import numpy as np
import cv2

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

for i, img in enumerate(test_images):
    if i > 100:
        break
    cv2.imwrite('test/'+str(test_labels[i])+'_'+str(i)+'.jpg',img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
