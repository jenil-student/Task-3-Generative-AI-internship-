"""
Text Generation with Markov Chains
References:
1. https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33/
2. https://github.com/aparrish/predictive-text-and-text-generation/blob/master/predictive-text-and-text-generation.ipynb
"""

import markovify
import os

# Try to read from sample.txt if it exists, else use default text
sample_file = os.path.join(os.path.dirname(__file__), "sample.txt")
if os.path.exists(sample_file):
    with open(sample_file, "r", encoding="utf-8") as f:
        text = f.read()
else:
    text = """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'
So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.
There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! I shall be late!' (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge."""

# Build the Markov model with higher state size for better accuracy
model = markovify.Text(text, state_size=3)

# Generate 5 sentences
print("Generated Text:\n")
for i in range(5):
    sentence = model.make_sentence()
    if sentence is None:
        sentence = model.make_short_sentence(140)
    if sentence is None:
        print("[Could not generate a sentence. Try adding more or different text to sample.txt]")
    else:
        print(sentence)
