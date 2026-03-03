import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from typing import List, Dict
import json
import os

class EnhancedBookRecommender:
 def __init__(self, model_name='all-MiniLM-L6-v2'):
 self.sentence_model = SentenceTransformer(model_name)
 self.books_data = None
 self.book_embeddings = None
 self.metadata = None
 
 def load_books(self, books_file='data/books.json'):
 try:
 with open(books_file, 'r', encoding='utf-8') as f:
 self.books_data = json.load(f)
 except FileNotFoundError:
 self.create_sample_data(books_file)
 with open(books_file, 'r', encoding='utf-8') as f:
 self.books_data = json.load(f)
 
 self.df = pd.DataFrame(self.books_data)
 self._preprocess_books()
 self._create_embeddings()
 
 def create_sample_data(self, filepath):
 sample_books = [
 {
 "id": 1, "title": "The Midnight Library", "author": "Matt Haig",
 "genre": "Fantasy Fiction", "description": "Between life and death there is a library...",
 "themes": "life choices, regret, second chances, fantasy",
 "rating": 4.2
 },
 {
 "id": 2, "title": "Sapiens", "author": "Yuval Noah Harari",
 "genre": "Non-Fiction", "description": "A brief history of humankind.",
 "themes": "human history, evolution, anthropology",
 "rating": 4.4
 }
 ]
 
 with open(filepath, 'w', encoding='utf-8') as f:
 json.dump(sample_books, f, indent=2, ensure_ascii=False)
 
 def _preprocess_books(self):
 self.df['combined_text'] = (
 self.df['title'] + ' ' + 
 self.df['author'] + ' ' + 
 self.df['description'] + ' ' + 
 self.df['themes'] + ' ' + 
 self.df['genre']
 ).
