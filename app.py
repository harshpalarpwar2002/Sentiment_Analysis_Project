import streamlit as st
from transformers import pipeline
import time

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(
    page_title="Interactive Sentiment Analyzer",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- REMOVE TOP WHITE BAR ----------------
st.markdown(
    """
    <style>
    header {visibility: hidden;}
    .block-container {
        padding-top: 1rem;
    }
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# ---------------- CUSTOM UI CSS ----------------
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
    font-size: 38px;
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

# ---------------- UI ----------------
st.markdown('<div class="title">💬 Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Type text and get instant emotional feedback</div>', unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

text = st.text_area(
    "✍️ Enter your text",
    placeholder="I don't like this product...",
    height=120
)

col1, col2 = st.columns(2)

with col1:
    analyze = st.button("🔍 Analyze")
with col2:
    clear = st.button("🧹 Clear")

if clear:
    st.rerun()

if analyze:
    if text.strip() == "":
        st.warning("⚠️ Please enter text to analyze")
    else:
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
        else:
            st.markdown(
                f'<div class="result" style="color:#DC2626;">😞 Negative</div>',
                unsafe_allow_html=True
            )

        st.progress(confidence / 100)
        st.metric("Confidence", f"{confidence}%")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Built with Streamlit & 🤗 Transformers</div>', unsafe_allow_html=True)
reamlit & 🤗 Transformers</div>', unsafe_allow_html=True)

