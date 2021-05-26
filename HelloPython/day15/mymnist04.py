# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import numpy as np
import cv2

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images_refine = test_images.reshape((10000, 28 * 28))
test_images_refine = test_images_refine.astype('float32') / 255


# 레이블을 범주형으로 인코딩
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 모델 정의하기 (여기에서는 Sequential 클래스 사용)
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

# 모델 컴파일 하기
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# fit() 메서드로 모델 훈련 시키기
model.fit(train_images, train_labels, epochs=5, batch_size=128)

predictions = model.predict(test_images_refine)


cnt = 0
for idx, pred in enumerate(predictions):
    if not np.argmax(test_labels[idx]) == np.argmax(pred):
        cnt += 1
        cv2.imwrite('miss/'+str(cnt) + '_predict(' + str(np.argmax(pred)) + ')_test(' + str(np.argmax(test_labels[idx])) +').jpg', test_images[idx])

cv2.waitKey(0)
cv2.destroyAllWindows()