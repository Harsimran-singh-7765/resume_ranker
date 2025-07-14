import spacy

# Load English tokenizer, POS tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    """
    Cleans and preprocesses raw text using SpaCy:
    - Lowercase
    - Removes stop words, punctuation, numbers
    - Lemmatizes words
    """
    doc = nlp(text.lower())

    tokens = [
        token.lemma_ for token in doc
        if not token.is_stop           # remove stop words (e.g., "and", "the")
        and not token.is_punct         # remove punctuation
        and token.is_alpha             # keep only alphabets
    ]

    return " ".join(tokens)



