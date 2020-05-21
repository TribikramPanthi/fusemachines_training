from tensorflow import keras
from numpy import asarray
import numpy as np
import os
from os import listdir
import cv2
import pickle


img = cv2.imread("output.jpeg")
img = cv2.resize(img, (150, 150))


with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# encoded_y = encoder.fit_transform(y)

model = keras.models.load_model("model.h5")

print(img.shape)
res = model.predict(np.expand_dims(img, axis=0))

print(encoder.inverse_transform(res))
