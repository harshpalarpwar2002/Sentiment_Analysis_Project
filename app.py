import streamlit as st
from transformers import pipeline

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .main-box {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }
        .title-text {
            text-align: center;
            color: #4F46E5;
            font-size: 38px;
            font-weight: bold;
        }
        .sub-text {
            text-align: center;
            color: #6B7280;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .result-box {
            padding: 20px;
            border-radius: 12px;
            font-size: 22px;
            font-weight: bold;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# ---------------- UI ----------------
st.markdown('<div class="title-text">Sentiment Analysis App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Analyze whether text is Positive or Negative</div>', unsafe_allow_html=True)

st.markdown('<div class="main-box">', unsafe_allow_html=True)

text = st.text_area(
    "Enter your text below:",
    height=120,
    placeholder="Example: I don't like this product"
)

if st.button("Analyze Sentiment"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        result = model(text)[0]
        label = result["label"]
        score = round(result["score"] * 100, 2)

        if label == "POSITIVE":
            st.markdown(
                f'<div class="result-box" style="background-color:#DCFCE7;color:#166534;">'
                f'😊 POSITIVE <br> Confidence: {score}%</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="result-box" style="background-color:#FEE2E2;color:#991B1B;">'
                f'😞 NEGATIVE <br> Confidence: {score}%</div>',
                unsafe_allow_html=True
            )

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    "<hr><center>Made with ❤️ using Streamlit & Transformers</center>",
    unsafe_allow_html=True
)
