import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.models import model_from_json

def predict(model, X):
    Y = model.predict(X)
    Y = np.argmax(Y, axis=1)
    Y = 'cat' if Y[0] == 0 else 'dog'
    return Y

if __name__ == '__main__':
    import sys
    img_dir = sys.argv[1]
    from get_dataset import get_img
    img = get_img(img_dir)
    import numpy as np

    X = np.zeros((1, 64, 64, 3), dtype='float64')
    X[0] = img
    # Getting model:
    model_file = open('Data/Model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)
    # Getting weights
    model.load_weights("Data/Model/weights.h5")
    Y = predict(model, X)
    print('It is a ' + Y + ' !')

image = cv2.resize(img, (200,200))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'',  (100,150), font, 3, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow(Y,image)

cv2.waitKey(0)