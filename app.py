import streamlit as st
import markovify
import os

st.set_page_config(page_title="Markov Chain Text Generator", page_icon="📝", layout="centered")
st.markdown("""
<style>
body, .stApp {
    background: linear-gradient(120deg, #232526 0%, #2c5364 100%) !important;
    color: #f5f6fa !important;
}
#main-header {
    background: rgba(34,37,38,0.95);
    border-radius: 0 0 32px 32px;
    box-shadow: 0 4px 24px #00000044;
    padding: 2.5em 2em 1.5em 2em;
    margin-bottom: 2em;
    text-align: center;
}
#main-header h1 {
    color: #38b6ff;
    font-size: 2.4em;
    letter-spacing: 2px;
    font-family: 'Montserrat', 'Segoe UI', Arial, sans-serif;
    font-weight: 800;
    margin-bottom: 0.2em;
    text-shadow: 2px 2px 12px #00000055;
}
.stTextInput>div>div>input, .stNumberInput>div>input {
    border-radius: 12px;
    border: 2px solid #38b6ff;
    padding: 1em;
    font-size: 1.1em;
    background: #232526;
    color: #f5f6fa;
    margin-bottom: 1.2em;
    font-family: 'Montserrat', 'Segoe UI', Arial, sans-serif;
}
.stButton>button {
    background: linear-gradient(90deg, #38b6ff 0%, #4F8BF9 100%);
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.7em 2.2em;
    font-size: 1.1em;
    margin-top: 1em;
    margin-bottom: 1.2em;
    box-shadow: 0 2px 12px #00000033;
    border: none;
    font-family: 'Montserrat', 'Segoe UI', Arial, sans-serif;
    transition: background 0.2s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #4F8BF9 0%, #38b6ff 100%);
}
.stSuccess {
    background: #38b6ff22 !important;
    color: #38b6ff !important;
    border-radius: 12px;
    font-weight: bold;
    font-size: 1.1em;
    margin-top: 1.2em;
    font-family: 'Montserrat', 'Segoe UI', Arial, sans-serif;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div id="main-header">
        <h1>📝 Markov Chain Text Generator</h1>
        <p>Generate new text based on your sample using a simple Markov chain model.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Load sample text
sample_file = os.path.join(os.path.dirname(__file__), "sample.txt")
if os.path.exists(sample_file):
    with open(sample_file, "r", encoding="utf-8") as f:
        text = f.read()
else:
    text = "Alice was beginning to get very tired of sitting by her sister on the bank. She had nothing to do. Once or twice she had peeped into the book her sister was reading. But it had no pictures or conversations in it. What is the use of a book, thought Alice, without pictures or conversation?"

# File uploader for user text
uploaded_file = st.file_uploader("Upload your own .txt file for training (optional)", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.success("Custom text file loaded!")

st.text_area("Sample Text Used for Training", value=text, height=200, disabled=True)

num_sentences = st.number_input("Number of sentences to generate", min_value=1, max_value=10, value=5)

generate = st.button("Generate Text")

if generate:
    model = markovify.Text(text)
    st.subheader("Generated Text:")
    for i in range(num_sentences):
        sentence = model.make_sentence()
        if sentence is None:
            sentence = model.make_short_sentence(140)
        if sentence is None:
            st.write("[Could not generate a sentence. Try adding more or different text to sample.txt or upload a larger file.]")
        else:
            st.write(sentence)
