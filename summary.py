from datasets import load_dataset
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import google.generativeai as genai
import spacy



# Loading the dataset
ds = load_dataset("ccdv/pubmed-summarization", "document")
raw_text = ds['train'][2]['article']

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    # Removing special characters and punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenizing the text into words
    words = word_tokenize(text)
    # Removing stopwords
    words = [word for word in words if word not in stop_words]
    # Converting into single string
    cleaned_text = ' '.join(words)
    return cleaned_text

def preprocess_sentences(text):
    # Converting into sentences
    sentences = sent_tokenize(text)
    cleaned_sentences = [preprocess_text(sentence) for sentence in sentences]
    return cleaned_sentences

def summarize_and_calculate_similarity(raw_text, api_key, summary_style='brief'):
    cleaned_sentences = preprocess_sentences(raw_text)
    input_text = ' '.join(cleaned_sentences)

    # Configure Google AI API
    genai.configure(api_key=api_key)

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(input_text)

    summarized_text = response.text

   
    num_words_original = len(word_tokenize(raw_text))
    num_words_summarized = len(word_tokenize(summarized_text))

    # Calculating Semantic Similarity
    def calculate_similarity(text1, text2):
        
        nlp = spacy.load("en_core_web_md")
        
        
        doc1 = nlp(text1)
        doc2 = nlp(text2)
        
       
        similarity = doc1.similarity(doc2)
        
        return similarity

    similarity_score = calculate_similarity(raw_text, summarized_text)

    return raw_text, summarized_text, similarity_score, num_words_original, num_words_summarized



API_KEY = "AIzaSyBjLMM9Bb8fotEz_ONDlXt8gcH0kpJioWw"


original_text, summarized_text, similarity_score, num_words_original, num_words_summarized = summarize_and_calculate_similarity(raw_text, API_KEY, summary_style='brief')
print("Original Text:", original_text)
print("Brief Summarized Text:", summarized_text)
print(f"Semantic Similarity Score (Brief): {similarity_score}")
print(f"Number of words in original text: {num_words_original}")
print(f"Number of words in summarized text: {num_words_summarized}")

original_text, summarized_text, similarity_score, num_words_original, num_words_summarized = summarize_and_calculate_similarity(raw_text, API_KEY, summary_style='detailed')
print("Original Text:", original_text)
print("Detailed Summarized Text:", summarized_text)
print(f"Semantic Similarity Score (Detailed): {similarity_score}")
print(f"Number of words in original text: {num_words_original}")
print(f"Number of words in summarized text: {num_words_summarized}")
