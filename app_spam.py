from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)  # Streamlit connection fix

# Files Load Karo
try:
    # Root directory se files load ho rahi hain
    model = pickle.load(open('spam_model.pkl', 'rb'))
    tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
    print("✅ Model & Vectorizer Loaded Successfully!")
except Exception as e:
    print(f"❌ Error loading files: {e}")

@app.route('/', methods=['GET'])
def home():
    return "✅ Spam Detection API is Live! Use /predict_spam for predictions."

@app.route('/predict_spam', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided', 'status': 'Failed'}), 400
        
        message = data['message']
        
        # Transformation & Prediction
        vector_input = tfidf.transform([message])
        prediction = model.predict(vector_input)[0]
        
        # Result mapping (1 for Spam, 0 for Ham)
        result = "Spam" if int(prediction) == 1 else "Ham"
        
        return jsonify({
            'result': result, 
            'status': 'Success'
        })
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'Failed'}), 500

if __name__ == "__main__":
    # Render port binding fix
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
