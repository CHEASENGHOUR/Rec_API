from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import requests

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and origins
# JSON server endpoint
JSON_SERVER_URL = 'https://json-db-m5if.onrender.com/laptops'
# Function to fetch data from JSON server


def fetch_data_from_json_server():
    response = requests.get(JSON_SERVER_URL)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()  # Parse JSON response
    return pd.DataFrame(data)  # Convert to DataFrame


# Function to get recommendations based on title or description
def get_recommendations(search_term, num_recommendations=10):
    # Fetch data from JSON server
    df = fetch_data_from_json_server()
    # Combine title and description into one field
    df['combined'] = df['title'] + " " + df['description']
    
    # Vectorize the text data using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['combined'])
    
    # Vectorize the search term
    search_vector = vectorizer.transform([search_term])
    
    # Compute cosine similarity between the search term and all items
    similarity_scores = cosine_similarity(search_vector, tfidf_matrix).flatten()
    df['similarity'] = similarity_scores
    
    # Sort by similarity and get top N recommendations
    # recommended = df.nlargest(num_recommendations, 'similarity')
    # return recommended[['id', 'title', 'description']].to_dict(orient='records')
    
    # Sort by similarity and rating, then get top recommendations
    recommended = df.sort_values(by=['similarity', 'rating'], ascending=[False, False]).head(num_recommendations)
    result = recommended[['title', 'description', 'rating', 'processor', 'ram_size', 'storage', 'price', 'stock']].to_dict(orient='records')

    return result


@app.route('/', methods=['POST'])
def recommendations():
    # Parse JSON data from request
    data = request.get_json()
    search_term = data.get('query')

    if not search_term:
        return jsonify({"error": "Search term is required"}), 400

    # Get recommendations based on search term
    recommended_items = get_recommendations(search_term)
    return jsonify({"recommendations": recommended_items})


if __name__ == '__main__':
    app.run(debug=True)
