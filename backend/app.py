from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = Flask(__name__)
CORS(app)

# Load model and tokenizer
model = BertForSequenceClassification.from_pretrained("./fake-news-bert")
tokenizer = BertTokenizer.from_pretrained("./fake-news-bert")
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']

    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    
    # Predict
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()

    label = "Real" if prediction == 1 else "Fake"
    return jsonify({'prediction': label})

if __name__ == '__main__':
    app.run(debug=True)
