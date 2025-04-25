import flask
from flask import Flask, render_template, request
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

# Load models
top_100_books = joblib.load('popularity_model.pkl')
collab_data = joblib.load('collab_model.pkl')
tfidf = collab_data['tfidf_vectorizer']
tfidf_matrix = collab_data['tfidf_matrix']
reduced_df = collab_data['filtered_df']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/popular_books')
def popular_books():
    return render_template('popular_books.html', books=top_100_books)

@app.route('/collaborative', methods=['GET', 'POST'])
def collaborative():
    book_titles = reduced_df['title'].dropna().unique()
    similar_books = []
    selected_title = None
    search_query = None
    
    if request.method == 'POST':
        # Handle direct book title selection
        if 'book_title' in request.form and request.form.get('book_title'):
            selected_title = request.form.get('book_title')
        # Handle search query
        elif 'search_query' in request.form and request.form.get('search_query'):
            search_query = request.form.get('search_query')
            # Find closest match in titles
            matching_titles = [title for title in book_titles if search_query.lower() in title.lower()]
            if matching_titles:
                selected_title = matching_titles[0]  # Use the first match
        
        # Get recommendations if we have a title
        if selected_title:
            try:
                idx = reduced_df[reduced_df['title'] == selected_title].index[0]
                sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
                top_indices = sim_scores.argsort()[-6:-1][::-1]
                similar_books = [reduced_df.iloc[i] for i in top_indices]
            except:
                similar_books = []
    
    return render_template('collaborative.html', 
                          book_titles=book_titles, 
                          similar_books=similar_books, 
                          selected_title=selected_title,
                          search_query=search_query)

@app.route('/personal', methods=['GET', 'POST'])
def personal_recommendations():
    book_titles = reduced_df['title'].dropna().unique()
    recommended_books = []
    selected_titles = []
    
    if request.method == 'POST':
        selected_titles = request.form.getlist('book_titles')
        
        if selected_titles:
            # Aggregate recommendations from multiple books
            all_sim_scores = np.zeros(len(reduced_df))
            
            for title in selected_titles:
                try:
                    idx = reduced_df[reduced_df['title'] == title].index[0]
                    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
                    # Add to cumulative scores (avoiding the book itself)
                    for i, score in enumerate(sim_scores):
                        if reduced_df.iloc[i]['title'] not in selected_titles:
                            all_sim_scores[i] += score
                except:
                    continue
            
            # Get top recommendations excluding selected books
            top_indices = all_sim_scores.argsort()[-10:][::-1]
            recommended_books = [reduced_df.iloc[i] for i in top_indices if all_sim_scores[i] > 0]
            
    return render_template('personal.html',
                          book_titles=book_titles,
                          recommended_books=recommended_books,
                          selected_titles=selected_titles)

if __name__ == '__main__':
    app.run(debug=True)

