import streamlit as st
from transformers import pipeline

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Sentiment Analysis | Durgesh Borse",
    page_icon="💬",
    layout="centered"
)

# ---------------- Load Model (Cached) ----------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1f2937;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #6b7280;
    margin-bottom: 10px;
}
.author {
    text-align: center;
    font-size: 16px;
    color: #2563eb;
    margin-bottom: 30px;
}
.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}
.positive {
    background-color: #dcfce7;
    color: #166534;
}
.negative {
    background-color: #fee2e2;
    color: #991b1b;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown('<div class="title">💬 Sentiment Analysis App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">NLP Application using Hugging Face Transformers</div>', unsafe_allow_html=True)
st.markdown('<div class="author">Created by <b>Durgesh Borse</b></div>', unsafe_allow_html=True)

# ---------------- Input ----------------
text = st.text_area(
    "✍️ Enter your text below:",
    height=120,
    placeholder="Example: I don't like this product"
)

# ---------------- Button ----------------
if st.button("🔍 Analyze Sentiment"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        result = model(text)[0]
        label = result["label"]
        score = round(result["score"] * 100, 2)

        st.markdown("---")

        if label == "POSITIVE":
            st.markdown(
                f'<div class="result-box positive">😊 POSITIVE<br>Confidence: {score}%</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="result-box negative">😠 NEGATIVE<br>Confidence: {score}%</div>',
                unsafe_allow_html=True
            )

# ---------------- Footer ----------------
st.markdown("""
<hr>
<center>
© 2025 | Sentiment Analysis App by <b>Durgesh Borse</b>
</center>
""", unsafe_allow_html=True)
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

