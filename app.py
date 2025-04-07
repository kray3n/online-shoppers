import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, jsonify

# Încarcă modelul Keras
model = keras.models.load_model("my_model.h5")

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my ML API!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # primește datele JSON
    # aici extragi feature-urile, creezi vector numeric
    input_vector = np.array([[data.get("Administrative", 0),
                              data.get("Administrative_Duration", 0),
                              data.get("Informational", 0),
                              ... ]])  # complet cu restul feature-urilor

    # model.predict -> prob
    prob = model.predict(input_vector)[0][0]
    pred = 1 if prob >= 0.5 else 0

    return jsonify({"probability": float(prob), "prediction": pred})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
