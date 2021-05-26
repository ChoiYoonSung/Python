import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
 
cifar10 = datasets.cifar10 
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
 
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
 
train_images = train_images.reshape((50000, 32, 32, 3))
test_images = test_images.reshape((10000, 32, 32, 3))
# ((depth, x, y, color(color = 3)))
 
 
train_images = train_images/255.0
test_images = test_images/255.0
 
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
 
airplane = cv2.imread("boeing-737.jpg", cv2.IMREAD_COLOR)
airplane_32 = cv2.resize(airplane, dsize=[32,32])
airplane_32_refine = airplane_32 / 255.0
airplane_32_refine = airplane_32_refine.reshape((1,32,32,3))
 
model.fit(train_images, train_labels, epochs=5)
 
predictions = model.predict(airplane_32_refine)

print("result : " + class_names[np.argmax(predictions)])
cv2.imshow("airplane",airplane)
cv2.waitKey()
cv2.destroyAllWindows()