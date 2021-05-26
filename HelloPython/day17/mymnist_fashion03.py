import tensorflow as tf
import numpy as np
import cv2
from keras.utils.np_utils import to_categorical


fashion_mnist = tf.keras.datasets.fashion_mnist
#tf.keras.datasets. ~~ imdb라던지. 
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images_refine = train_images / 255.0
test_images_refine = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images_refine, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

predictions = model.predict(test_images_refine)

cnt = 0

for idx, pred in enumerate(predictions):
    if not np.argmax(test_labels[idx]) == np.argmax(pred):
        cnt += 1
        cv2.imwrite('image_miss/'+str(cnt) + '_predict(' + str(np.argmax(pred)) + ')_test(' + str(np.argmax(test_labels[idx])) +').jpg', test_images[idx])

cv2.waitKey(0)
cv2.destroyAllWindows()