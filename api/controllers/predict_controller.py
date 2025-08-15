import base64
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import os
from api.functions.download_model import download_model, MODEL_NAME

# Classes do modelo
class_names = ['CIN1', 'CIN2', 'CIN3']
class_names_pt = ['CIN1', 'CIN2', 'CIN3']


if not os.path.exists(MODEL_NAME):
    download_model()

model = load_model(MODEL_NAME)


def predict_image(image_base64: str):
    img_data = base64.b64decode(image_base64)
    np_arr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (244, 244))
    img_array = np.expand_dims(img, axis=0)
    img_array = img_array / 255.0

    preds = model.predict(img_array)
    predicted_class = np.argmax(preds, axis=1)
    predicted_label = class_names[predicted_class[0]]
    predicted_label_pt = class_names_pt[predicted_class[0]]

    return {
        "prediction_en": predicted_label,
        "prediction_pt": predicted_label_pt
    }
