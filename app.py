from flask import Flask, render_template, request
from summary import summarize_and_calculate_similarity

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/analyze", methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary_style = request.form['summary_style']  # Get the selected summary style
        
        API_KEY = "AIzaSyBjLMM9Bb8fotEz_ONDlXt8gcH0kpJioWw"
        original_text, summarized_text, similarity_score, num_words_original, num_words_summarized = summarize_and_calculate_similarity(rawtext, API_KEY, summary_style)
        
        return render_template('result.html', original_text=original_text, summarized_text=summarized_text, similarity_score=similarity_score, num_words_original=num_words_original, num_words_summarized=num_words_summarized)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
