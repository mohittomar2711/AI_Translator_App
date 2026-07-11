import streamlit as st


st.set_page_config(
    page_title="About AI Translator",
    page_icon="🌍"
)


st.title("🌍 About AI Language Translator")


st.write("""
## Project Description

AI Language Translator is a text-based language translation
application developed using Python and Streamlit.

The application detects the input language automatically and
translates the text into the selected target language using
AI-based translation services.
""")


st.subheader("🛠 Technologies Used")

st.write("""
- Python
- Streamlit
- Deep Translator Library
- Google Translator API
- LangDetect Library
""")


st.subheader("⚙️ Working Methodology")

st.write("""
1. User enters text.
2. System detects the input language.
3. User selects target language.
4. Translation engine converts the text.
5. Result is displayed and saved in history.
""")


st.subheader("🚀 Future Scope")

st.write("""
- Support more languages
- Add offline translation models
- Improve translation accuracy
- Add user accounts
- Deploy as a web application
""")


st.subheader("📌 Project Category")

st.success(
    "Artificial Intelligence + Natural Language Processing + Web Application"
)