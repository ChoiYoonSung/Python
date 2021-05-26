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

for idx, img in enumerate(train_images):
    cv2.imwrite('cifar_train/' + str(train_labels[idx][0]) + '_' + str(idx) + '.png',train_images[idx])
    if idx > 100:
        break
    
for idx, img in enumerate(test_images):
    cv2.imwrite('cifar_test/' + str(test_labels[idx][0]) + '_' + str(idx) + '.png',test_images[idx])
    if idx > 100:
        break