from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from model import tokenizer, label_encoder, max_sequence_length, model

app = Flask(__name__)

# Load the trained model
model.load_weights('rnn_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']

    # Preprocess the input text
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length)

    # Make the prediction
    prediction = model.predict(padded_sequence)
    predicted_label = label_encoder.inverse_transform([np.argmax(prediction[0])])[0]

    return jsonify({'prediction': predicted_label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)