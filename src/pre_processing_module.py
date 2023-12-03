from typing import Any
import spacy
import re

from src.module import Process

def extractive_summarize(input_text):
    # Load SpaCy model for English
    nlp = spacy.load("en_core_web_sm")

    # Process the input text
    doc = nlp(input_text)

    # Get sentences and their corresponding importance scores
    sentences = [sent.text for sent in doc.sents]
    scores = [sum(token.vector) for token in doc]

    # Select the top sentences based on importance scores
    selected_sentences = sorted(zip(sentences, scores), key=lambda x: x[1], reverse=True)

    # Combine selected sentences into the final summarized text
    summarized_text = ' '.join(sentence for sentence, _ in selected_sentences)

    return summarized_text

def input_cleaner(c_input):
    clean_input = ''
    c_i = remove_extra_spaces(c_input)
    s_i = extractive_summarize(c_i)

    clean_input = s_i
    return clean_input

class RemoveSpace(Process):
    def __init__(self):
        super().__init__('remove space')
    
    def __call__(self, prompt):
        # Use a regular expression to replace multiple spaces with a single space
        cleaned_string = re.sub(r'\s+', ' ', prompt.get_prompt())
        prompt.set_prompt(cleaned_string)