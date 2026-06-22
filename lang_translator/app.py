import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translator", page_icon="🌍", layout="centered")

st.markdown("""
            <style>
            .stApp{
                    background: linear-gradient(135deg, #020617, #0f172a, #1e3a8a, #2563eb );
            }

            #MainMenu {visibility:hidden;}
            footer{visibility:hidden;}
            header{visibility:hidden;}

            label, .stTextArea label, .stSelectbox label, [data-testid="stWidgetLabel"]{ color:white !important; font-size:18px !important; font-weight:600 !important; }

            .main-box{
                    background: rgba(255,255,255,0.7);
                    padding: 30px;
                    border-radius:20px;
                    backdrop-filter:blur(20px);
                    -webkit-backdrop-filter: blur(20px);
                    border: 1px solid rgba(255,255,255,0.1);
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
                background: linear-gradient( 135deg,#2563eb,#60a5fa);
                color:white;
                font-size:18px;
                font-weight:700;
                transition:all 0.3s ease;
            }

            .stButton>button:hover{
                transform:translateY(-2px)
                background-color:#5548d9;
                box-shadow: 0 0 20px rgba(59, 130, 246, 0.6)
            }

            textarea{
                border-radius:20px !important;
            }
            </style>
            """, unsafe_allow_html=True)
st.markdown('<div class="main-box">',unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;
color:white;
font-size:4rem;
font-weight:800;'>
🌍 Language Translation Tool
</h1>

<p style='text-align:center;
color:white;
font-size:1.2rem;'>
✨ Translate text instantly across languages ✨
</p>
""", unsafe_allow_html=True)

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

        st.markdown("""
        <div style="
            background:linear-gradient(135deg,#2563eb,#60a5fa);
            padding:18px;
            border-radius:18px;
            text-align:center;
            color:white;
            font-size:24px;
            font-weight:700;
            margin-top:20px;
            margin-bottom:20px;
            box-shadow:0 8px 20px rgba(37,99,235,0.4);
        ">
         Translation Completed!!
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Translated Text")
        st.info(translated)

       
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.12);
            backdrop-filter: blur(15px);
            padding:25px;
            border-radius:20px;
            border:1px solid rgba(255,255,255,0.15);
            box-shadow:0px 8px 20px rgba(0,0,0,0.2);
        ">
            <h3 style="color:white;">
                🌍 Translated Text
            </h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        
        tts = gTTS(
            text=translated,
            lang=languages[target_lang]
        )

        tts.save("translation.mp3")

        st.subheader("🔊 Listen to Translation")
        with open("translation.mp3", "rb") as audio_file:
            st.audio(audio_file.read())

        
        st.download_button(
            label="📥 Download Translation",
            data=translated,
            file_name="translation.txt",
            mime="text/plain"
        )

    else:
        st.warning("⚠️ Please enter some text!")
