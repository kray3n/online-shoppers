import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, jsonify

model = keras.models.load_model("my_model.h5")

app = Flask(__name__)

@app.route("/")
def home():
    return "Shopper prediciton!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    input_order = ["Administrative", "Administrative_Duration", "Informational",
                   "Informational_Duration", "ProductRelated", "ProductRelated_Duration",
                   "BounceRates", "ExitRates", "PageValues", "SpecialDay", "Weekend"
                  ]
    x_input = []
    for col in input_order:
        x_input.append(data.get(col, 0))

    x_input = np.array([x_input], dtype=float)

    prob = model.predict(x_input)[0][0]
    prediction = 1 if prob >= 0.5 else 0

    return jsonify({
        "probability": float(prob),
        "prediction": int(prediction)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
