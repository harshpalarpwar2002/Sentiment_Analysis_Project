import streamlit as st
from transformers import pipeline
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Interactive Sentiment Analyzer",
    page_icon="💬",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main-card {
    background: linear-gradient(135deg, #EEF2FF, #FFFFFF);
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    color: #4338CA;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #6B7280;
    margin-bottom: 25px;
}
.result {
    font-size: 26px;
    font-weight: bold;
    text-align: center;
}
.footer {
    text-align: center;
    color: #9CA3AF;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource(show_spinner=False)
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# ---------------- UI ----------------
st.markdown('<div class="title">💬 Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Type text and get instant emotional feedback</div>', unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

text = st.text_area(
    "✍️ Enter your text",
    placeholder="I don't like this product...",
    height=120,
    help="Supports English text for sentiment detection"
)

col1, col2 = st.columns(2)

with col1:
    analyze = st.button("🔍 Analyze")
with col2:
    clear = st.button("🧹 Clear")

if clear:
    st.experimental_rerun()

if analyze and text.strip():
    with st.spinner("Analyzing sentiment..."):
        time.sleep(0.8)
        result = model(text)[0]

    label = result["label"]
    confidence = round(result["score"] * 100, 2)

    st.markdown("---")

    if label == "POSITIVE":
        st.markdown(
            f'<div class="result" style="color:#16A34A;">😊 Positive</div>',
            unsafe_allow_html=True
        )
        st.progress(confidence / 100)
    else:
        st.markdown(
            f'<div class="result" style="color:#DC2626;">😞 Negative</div>',
            unsafe_allow_html=True
        )
        st.progress(confidence / 100)

    st.metric(label="Confidence Score", value=f"{confidence}%")

elif analyze:
    st.warning("⚠️ Please enter text to analyze")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown('<div class="footer">Built with Streamlit & 🤗 Transformers</div>', unsafe_allow_html=True)

