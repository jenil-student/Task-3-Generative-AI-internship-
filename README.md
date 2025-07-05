# Markov Chain Text Generator

This is a simple web app for text generation using Markov chains, built with Streamlit and Markovify.
![Uploading image.png…]()


## Features
- Generates new sentences based on a sample text using a Markov chain model.
- Upload your own `.txt` file to use as training data.
- Clean, modern UI.

## How to Run Locally
1. Install requirements:
   ```
   pip install -r requirements.txt
   ```
2. Start the app:
   ```
   streamlit run app.py
   ```
3. Open the browser link provided by Streamlit.

## How to Deploy (Streamlit Community Cloud)
1. Push this folder (`Task-3`) to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Connect your repo and select `app.py` as the main file.
4. Deploy and share your app!

## Files
- `app.py` — Streamlit UI for text generation
- `sample.txt` — Default training text (edit or replace as you wish)
- `requirements.txt` — Python dependencies

## Example
Try uploading a `.txt` file with your own text, or use the default sample to see how the Markov chain blends different writing styles!
