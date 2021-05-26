import numpy as np
from tensorflow.keras.models import load_model
model = load_model('models/20201213_202430.h5')

def getComIJ(arr2d):
    input = np.zeros((20,20))
    for i in range(20):
        for j in range(20):
            if arr2d[i][j] == 2:
                input[i][j] = -1
            elif arr2d[i][j] == 1:
                input[i][j] = 1
    
    input = input.reshape(1,20,20,1)
    
    output = model.predict(input).squeeze()
    output = output.reshape((20, 20))
    i, j = np.unravel_index(np.argmax(output), output.shape)
    return i,j
    
if __name__ == '__main__':
    arr2d = np.zeros((20,20))
    
    con_x, com_y = getComIJ(arr2d)