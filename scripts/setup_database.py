#!/usr/bin/env python3
"""
Script to set up the database for AI Book Recommender
"""

import json
import os
import sys
from pathlib import Path
from models.data_loader import DataLoader
from models.enhanced_recommender import EnhancedBookRecommender

def create_sample_database():
    """Create a sample database with initial book data"""
    print("Creating sample database...")
    
    # Sample books data
    sample_books = [
        {
            "id": 1,
            "title": "The Midnight Library",
            "author": "Matt Haig",
            "genre": "Fantasy Fiction",
            "description": "Between life and death there is a library, and within that library, the shelves go on forever.",
            "themes": "life choices, regret, second chances, fantasy",
            "rating": 4.2,
            "year": 2020,
            "pages": 288,
            "language": "English"
        },
        {
            "id": 2,
            "title": "Sapiens",
            "author": "Yuval Noah Harari",
            "genre": "Non-Fiction",
            "description": "A brief history of humankind.",
            "themes": "human history, evolution, anthropology",
            "rating": 4.4,
            "year": 2011,
            "pages": 443,
            "language": "English"
        },
        {
            "id": 3,
            "title": "The White Tiger",
            "author": "Aravind Adiga",
            "genre": "Fiction",
            "description": "A novel about class struggle in modern India.",
            "themes": "indian fiction, social inequality, modern india",
            "rating": 3.8,
            "year": 2008,
            "pages": 304,
            "language": "English"
        },
        {
            "id": 4,
            "title": "Atomic Habits",
            "author": "James Clear",
            "genre": "Self-Help",
            "description": "Tiny changes, remarkable results.",
            "themes": "habits, self-improvement, productivity",
            "rating": 4.5,
            "year": 2018,
            "pages": 320,
            "language": "English"
        },
        {
            "id": 
  
