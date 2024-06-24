from datasets import load_dataset
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation

# Loading the dataset
ds = load_dataset("ccdv/pubmed-summarization", "document")
# checking the structure of the dataset
#print(ds['train'][0].keys())

# DATAPREPROCESSING
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
   
    text = text.lower()
    # Removing special characters and punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenizing the text into words
    words = word_tokenize(text)
    # Removing stopwords
    words = [word for word in words if word not in stop_words]
    #converting into single string
    cleaned_text = ' '.join(words)
    
    return cleaned_text

def preprocess_sentences(text):
    # coverting into sentences
    sentences = sent_tokenize(text)
    cleaned_sentences = [preprocess_text(sentence) for sentence in sentences]
    
    return cleaned_sentences

raw_text = ds['train'][45]['article']

cleaned_sentences = preprocess_sentences(raw_text)

print("\nCleaned Sentences:\n", cleaned_sentences)