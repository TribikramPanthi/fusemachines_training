from tensorflow import keras
from numpy import asarray
import numpy as np
import os
from os import listdir
import cv2
import pickle


def load_images_from_folder(path, size=(150, 150)):
    images = []
    labels = []
    for folder in listdir(path):
        for image in listdir(os.path.join(path, folder)):
            img = cv2.imread(os.path.join(path, folder, image))
            if img is not None:
                img = cv2.resize(img, size)
                images.append(img)
                labels.append(asarray(os.path.basename(os.path.join(path, folder))))
    return asarray(images), asarray(labels)


X, y = load_images_from_folder("../data/processed/testset")

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

encoded_y = encoder.fit_transform(y)

model = keras.models.load_model("model.h5")
print(model.summary())

res = model.evaluate(X, encoded_y, batch_size=16)
print(res)
