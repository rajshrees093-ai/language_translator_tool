import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌍")

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

text=st.text_area("Enter Text")

source_lang=st.selectbox(
    "Source Language",
    list(languages.keys())
)

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

        st.success("Translation Complete!")
        st.text_area("Translated Text", translated, height=150)
    else:
        st.warning("Please enter some text!!!!!!!!")