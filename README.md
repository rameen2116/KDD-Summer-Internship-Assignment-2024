PubMed Article Summarization
This repository contains a web application for summarizing PubMed articles using natural language processing techniques and Google's Generative AI. The application allows users to input a text and receive a summarized version of the text, along with a similarity score indicating how similar the summary is to the original text.

Table of Contents
Project Overview
Data Preprocessing
Model Selection and Fine-Tuning
Web Application Development
The project involves the following steps:

Data exploration and preprocessing.
Summarization using Google's Generative AI model.
Calculation of semantic similarity between the original and summarized text.
Development of a Flask web application to interact with the summarization model.
Data Preprocessing:
The dataset used for this project is the ccdv/pubmed-summarization dataset. The preprocessing involves:

Converting the text to lowercase.
Removing special characters and punctuation.
Tokenizing the text into words.
Removing stopwords.
Tokenizing the text into sentences and cleaning each sentence.
Model Selection and Fine-Tuning:
We use Google's Generative AI, specifically the "gemini-1.5-flash" model, for text summarization. This model is configured using specific parameters for temperature, top_p, top_k, and max_output_tokens, which are adjusted based on the summary style (brief or detailed).

Web Application Development:
The web application is built using Flask. It allows users to input text and choose a summary style (brief or detailed). The application then returns the original text, the summarized text, the similarity score, and the word counts of both texts.
 
