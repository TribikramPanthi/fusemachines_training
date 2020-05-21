import cv2
import numpy as np
import re
import os
from tensorflow import keras
import base64

model = keras.models.load_model("model.h5")
OUTPUT = os.path.join(os.path.dirname(__file__), "output.jpeg")
POS_IMG = os.path.join(os.path.dirname(__file__), "pos.png")
NEG_IMG = os.path.join(os.path.dirname(__file__), "neg.png")

from PIL import Image
from io import BytesIO
import pickle

# from lime import lime_image
# from skimage.segmentation import mark_boundaries
# from skimage.color import gray2rgb, rgb2gray, label2rgb
# from lime.wrappers.scikit_image import SegmentationAlgorithm

# explainer = lime_image.LimeImageExplainer()

# segmenter = SegmentationAlgorithm("quickshift", kernel_size=1, max_dist=200, ratio=0.2)


def getI420FromBase64(codec):

    base64_data = re.sub("^data:image/.+;base64,", "", codec)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    img.save(OUTPUT)


def convertImage(imgData):
    getI420FromBase64(imgData)


def get_label(arr):
    encoder = None
    with open("encoder.pkl", "rb") as f:
        encoder = pickle.load(f)
    res = encoder.inverse_transform(arr)
    return res


# def explain_output(img_arr):

#     explanation = explainer.explain_instance(
#         img_arr,
#         classifier_fn=model.predict,
#         top_labels=10,
#         num_samples=1000,
#         segmentation_fn=segmenter,
#     )

#     temp, mask = explanation.get_image_and_mask(
#         explanation.top_labels[0],
#         positive_only=True,
#         num_features=10,
#         hide_rest=False,
#         min_weight=0.01,
#     )
#     cv2.imwrite(POS_IMG, label2rgb(mask, temp, bg_label=0) * 255)

#     temp, mask = explanation.get_image_and_mask(
#         explanation.top_labels[0],
#         positive_only=False,
#         num_features=10,
#         hide_rest=False,
#         min_weight=0.01,
#     )
#     cv2.imwrite(NEG_IMG, label2rgb(3 - mask, temp, bg_label=0) * 255)


def predict(data):

    imgData = data
    pos_img = None
    neg_img = None

    convertImage(imgData)
    x = cv2.imread(OUTPUT)
    x = cv2.resize(x, (150, 150))
    # explain_output(x)
    x = np.expand_dims(x, axis=0)

    res = model.predict(x)
    out = get_label(res)
    # with open("pos.png", "rb") as image_file:
    #     pos_img = base64.b64encode(image_file.read())
    # with open("neg.png", "rb") as image_file:
    #     neg_img = base64.b64encode(image_file.read())
    return out, pos_img, neg_img
