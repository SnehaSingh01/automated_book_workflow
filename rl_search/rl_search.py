# rl_search/rl_search.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def rl_search(query, history):
    """
    Retrieves the most relevant version based on cosine similarity using TF-IDF.
    
    Parameters:
        query (str): The user's current query or desired topic.
        history (dict): Dictionary with version_id as keys and text as values.

    Returns:
        str: The version_id with the highest similarity to the query.
    """
    if not history:
        return None

    version_ids = list(history.keys())
    documents = list(history.values())
    documents.insert(0, query)  # Add query to the start for vectorization

    # Compute TF-IDF matrix
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    # Compute cosine similarity (query vs each document)
    cosine_scores = cosine_similarity([vectors[0]], vectors[1:])[0]
    best_index = np.argmax(cosine_scores)

    return version_ids[best_index]
