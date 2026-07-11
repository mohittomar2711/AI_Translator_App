import os
import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect
#----------------------------
#Page Configuration
#----------------------------
st.set_page_config(page_title = "AI Translator",
                   page_icon = "🌍",
                   layout = "wide",
                   initial_sidebar_state="expanded"
)
st.sidebar.title("🌍 AI Translator")
st.sidebar.markdown("""
## Features
✅ Translate Text
🌍 Multiple Languages
⚡ Fast Translation
🧑‍💻 Build Using Python & streamlit
""")

# -----------------------------
# Custom CSS Styling
# -----------------------------

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fb;
    }

    h1 {
        text-align: center;
    }

    .stButton button {
        width: 100%;
        border-radius: 10px;
        height: 40px;
    }

    .stTextArea textarea {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Title
# -----------------------------
st.title("🌍 AI Language Translator")

st.write(
    "Translate text into different languages instantly using AI."
)


col1, col2, col3 = st.columns(3)


with col1:
    st.info("🌎 Auto Language Detection")


with col2:
    st.success("⚡ Fast Translation")


with col3:
    st.warning("📜 Translation History")


#---------------------------------
#Input Text
#---------------------------------
text = st.text_area(
    "Enter text to translate",
    height = 150
)
# -----------------------------
# Text Analysis Function
# -----------------------------

def text_analysis(text):

    words = len(text.split())

    characters = len(text)

    sentences = text.count(".") + text.count("!") + text.count("?")

    return words, characters, sentences

# -----------------------------
# Text Statistics
# -----------------------------

if text.strip():

    words, characters, sentences = text_analysis(text)

    st.subheader("📊 Text Analysis")

    col1, col2, col3 = st.columns(3)

    col1.metric("Words", words)

    col2.metric("Characters", characters)

    col3.metric("Sentences", sentences)

#----------------------------------
#Language Dictionaries
#----------------------------------
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Urdu": "ur",
    "Arabic": "ar",
    "Japanese":"ja",
    "Chinese":"zh-cn"
}
code_to_language = {
   "en":"English",
   "hi":"Hindi",
   "fr":"French",
   "de": "German",
   "es": "Spanish",
   "ur": "Urdu",
   "ar":"Arabic",
   "ja":"Japanese",
   "zh-cn":"Chinese"

}
# -----------------------------
# Save Translation History
# -----------------------------
def save_history(original, detected, target, translated):
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(
            f"""
Original Text: {original}
Detected Language: {detected}
Target Language: {target}
Translated Text: {translated}
----------------------------------------
"""
        )
col1 , col2 = st.columns(2)
with col1:
    source = st.selectbox("Source Language", list(languages.keys()))
with col2:
    target = st.selectbox("Target Language",list(languages.keys()))

button_col1 , button_col2 = st.columns(2)

translate = button_col1.button("Translate")
clear = button_col2.button("Clear")

if clear:
   st.rerun()

if translate:
   if text.strip()=="":
       st.warning("Please enter some text.")
   elif source == target:
       st.info("Source and Target languages cannot be the same.")
   else:
       try:
          detected_code = detect(text)
          detected_language = code_to_language.get(detected_code , detected_code)
          st.info(f"Detected Language: {detected_language}") 
          with st.spinner("Translating...."):
            translated = GoogleTranslator(
               source = "auto",
               target=languages[target]
            ).translate(text)

          st.subheader("Translated Text")
          st.text_area("Output",translated,height = 150)
          # -----------------------------
          # Download Translation
          # -----------------------------

          download_file = st.download_button(
          label="📥 Download Translation",
          data=translated,
          file_name="translated_text.txt",
          mime="text/plain"
          )
          #Save history
          save_history(text,detected_language,target,translated)
          st.success("Translation saved successfully!")

       except Exception as e:
          st.error("Translation failed")
          st.write(e)

#------------------------------
#Translation History
#------------------------------
st.subheader("📕Translation History")

if os.path.exists("history.txt"):
   with open("history.txt","r",encoding = "utf-8")as file:
       history = file.read()
    
   if history:
       
       st.text_area(
          "Previous translation",
          history,
          height=300
       )
   else:
      
      st.info("No history available.")

else:
   
   st.info("No history available.")

