🛡️ AI Spam Detection System (End-to-End NLP)
An intelligent message classification system built using Natural Language Processing (NLP). The project features a production-ready Flask API and an interactive Streamlit Dashboard to predict whether a message is "Spam" or "Ham" (Safe) in real-time.

🚀 Live Links
Frontend (Streamlit): https://yz77ebsnrzs7kbcutqbfhh.streamlit.app/

Available at your primary URL https://spam-detection-model-lcsy.onrender.com

🛠️ Tech Stack & Workflow
1. Model Development
Language: Python

Algorithms: Multinomial Naive Bayes

Feature Extraction: TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization

Evaluation: Accuracy Score, Confusion Matrix, and Classification Report (Precision/Recall)

2. Backend & Deployment
Framework: Flask (REST API)

Server: Gunicorn

Persistence: Model and Vectorizer serialized using Pickle

Hosting: Render Cloud (Auto-deploy from GitHub)

3. Frontend
Library: Streamlit

Features: Custom CSS for dark-mode UI, input validation, and real-time API communication using requests

📂 Project Structure
Plaintext
├── app_spam.py           # Flask API script (Backend)
├── dashboard_spam.py     # Streamlit application (Frontend)
├── spam_model.pkl        # Trained Naive Bayes model
├── tfidf_vectorizer.pkl  # Saved TF-IDF vectorizer
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
👤 Author
Anmol

Aspiring AI/ML Engineer | BCA Graduate

LinkedIn: https://www.linkedin.com/in/anmol-panwar-4b7779324/


