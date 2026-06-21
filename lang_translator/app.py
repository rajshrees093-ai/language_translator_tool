import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translator", page_icon="🌍", layout="centered")

st.markdown("""
            <style>
            .stApp{
                    background: linear-gradient(135deg, #99f6e4, #5eead4, #22d3ee );
            }

            .main-box{
                    background: rgba(255,255,255,0.7);
                    padding: 30px;
                    border-radius:20px;
                    backdrop-filter:blur(10px);
                    -webkit-backdrop-filter: blur(18px);
                    box-shadow: 0px 8px 32px rgba(0,0,0,0.5), 0 4px 12px rgba(255, 255, 255, 0.2);
            }

            h1{
                text-align:center;
                color:#0f766e;
                font-size: 3rem;
                font-weight:800;
            }

            .stButton>button{
                width:100%;
                border-radius:12px;
                background-color: #6c63ff;
                color:white;
                font-size:18px;
                font-weight:bold;
            }

            .stButton>button:hover{
                background-color:#5548d9;
            }

            textarea{
                border-radius:20px !important;
            }
            </style>
            """, unsafe_allow_html=True)
st.markdown('<div class="main-box">',unsafe_allow_html=True)

st.title("🌍 Language Translation Tool")

languages={
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japenese": "ja",
    "Chinese": "zh-CN"
}

text=st.text_area("Enter Text",
                  placeholder="Type something to translate..."
                )

col1, col2 =st.columns(2)

with col1:
    source_lang=st.selectbox(
    "Source Language",
    list(languages.keys())
)


with col2:
    target_lang= st.selectbox(
    "Target Language",
    list(languages.keys())
)

if st.button("Translate"):
    if text:
        translated=GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Complete!✅")
        st.text_area("Translated Text", translated, height=150)
    else:
        st.warning("⚠️Please enter some text!!!!!!!!")

st.markdown("</div>", unsafe_allow_html=True)