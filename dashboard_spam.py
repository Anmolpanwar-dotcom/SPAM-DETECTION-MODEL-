import streamlit as st
import requests
from datetime import datetime

# ---------------- CONFIGURATION ----------------
# Yaad rakhna: URL ke aakhir mein /predict_spam zaroor lagana
API_URL = "https://spam-detection-model-lcsy.onrender.com/predict_spam"
MAX_MESSAGE_LENGTH = 1000

# ---------------- CUSTOM CSS (Text Visibility Fix) ----------------
CUSTOM_CSS = """
<style>
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* FIX: Isse input text white aur saaf dikhega */
    .stTextArea textarea {
        color: #ffffff !important;
        background-color: #1e293b !important;
    }
    
    .stTextArea label {
        color: #94a3b8 !important;
    }

    .result-card {
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 1.5rem;
    }
    .spam-card {
        background-color: rgba(239, 68, 68, 0.1);
        border: 1px solid #ef4444;
        color: #fca5a5;
    }
    .ham-card {
        background-color: rgba(34, 197, 94, 0.1);
        border: 1px solid #22c55e;
        color: #86efac;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #64748b;
        font-size: 0.8rem;
    }
</style>
"""

# ---------------- MAIN UI ----------------
def main():
    st.set_page_config(page_title="AI Spam Detector", page_icon="🛡️", layout="centered")
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title'>🛡️ AI Spam Detector</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>NLP Powered Message Classification System</p>", unsafe_allow_html=True)

    # Input Section
    st.subheader("📩 Enter Message")
    message = st.text_area(
        "Paste the message you want to analyze",
        height=150,
        placeholder="Example: You've won a cash prize! Claim now...",
        key="message_input"
    )

    col1, col2 = st.columns([3, 1])
    with col1:
        analyze_btn = st.button("🔍 Analyze Message", use_container_width=True, type="primary")
    with col2:
        if st.button("🗑️ Clear", use_container_width=True):
            st.rerun()

    if analyze_btn:
        if not message.strip():
            st.warning("⚠️ Bhai, pehle message toh dalo!")
        elif len(message) > MAX_MESSAGE_LENGTH:
            st.error(f"⚠️ Message too long (Max {MAX_MESSAGE_LENGTH} chars).")
        else:
            with st.spinner("🧠 AI is analyzing..."):
                try:
                    # API Call
                    response = requests.post(API_URL, json={"message": message}, timeout=15)
                    data = response.json()

                    if data.get("status") == "Success":
                        result = data.get("result")
                        
                        st.markdown("### 📊 Prediction Result")
                        if result == "Spam":
                            st.markdown(f"<div class='result-card spam-card'><h2>🚨 Likely SPAM</h2><p>This message matches fraudulent patterns.</p></div>", unsafe_allow_html=True)
                        else:
                            st.markdown(f"<div class='result-card ham-card'><h2>✅ Appears SAFE</h2><p>No spam patterns detected.</p></div>", unsafe_allow_html=True)
                            st.balloons()
                    else:
                        st.error("❌ API returned an error.")
                except Exception as e:
                    st.error("🔌 Connection Error: Render server is waking up or URL is wrong. Please wait 30 seconds.")

    # Technical Details
    with st.expander("🔍 Technical Breakdown"):
        st.write("- **Model:** Multinomial Naive Bayes")
        st.write("- **Tech:** TF-IDF Vectorizer + Flask + Render")
        st.write("- **Dataset:** Kaggle SMS Spam Collection")

    # Footer
    st.markdown(f"<div class='footer'>Built by Anmol | BCA ML Portfolio Project | {datetime.now().year}</div>", unsafe_allow_html=True)

if __name__ == "__main__":

    main()
