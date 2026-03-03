from flask import Flask, jsonify, request
from models.enhanced_recommender import EnhancedBookRecommender
from models.traditional_recommender import TraditionalRecommender
import logging
from config import config
import os

def create_app(config_name=None):
    config_name = config_name or os.environ.get('FLASK_ENV', 'default')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Configure logging
    logging.basicConfig(
        level=app.config['LOG_LEVEL'],
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    
    # Initialize recommenders
    try:
        app.enhanced_recommender = EnhancedBookRecommender()
        app.enhanced_recommender.load_books(app.config['DATABASE_PATH'])
        logger.info("Enhanced recommender loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load enhanced recommender: {str(e)}")
        app.enhanced_recommender = None
    
    try:
        app.traditional_recommender = TraditionalRecommender()
        app.traditional_recommender.load_books(app.config['DATABASE_PATH'])
        logger.info("Traditional recommender loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load traditional recommender: {str(e)}")
        app.traditional_recommender = None
    
    @app.route('/')
    def home():
        return jsonify({
            "message": "AI Book Recommender API",
            "version": "1.0.0",
            "endpoints": [
                "/api/recommend?book={title}",
                "/api/books/genre/{genre}",
                "/api/trending",
                "/api/books",
                "/api/health",
                "/api/docs"
            ]
        })
    
    @app.route('/api/docs')
    def api_docs():
        return jsonify({
            "title": "AI Book Recommender API",
            "version": "1.0.0",
            "description": "API for AI-powered book recommendations",
            "endpoints": {
                "GET /api/recommend": "Get recommendations for a book",
                "GET /api/books/genre/{genre}": "Get books by genre",
                "GET /api/trending": "Get trending books",
                "GET /api/books": "List all books",
                "POST /api/books": "Add a new book",
                "GET /api/health": "Health check endpoint"
            }
        })
    
    @app.route('/api/health')
    def health_check():
        status = {
            "status": "healthy",
            "timestamp": str(os.times()),
            "models_loaded": {
                "enhanced": app.enhanced_recommender is not None,
                "traditional": app.traditional_recommender is not None
            }
        }
        return jsonify(status)
    
    @app.route('/api/recommend')
    def get_recommendations():
        """Get AI-powered book recommendations"""
        book_title = request.args.get('book', '')
        method = request.args.get('method', 'enhanced')
        
        if not book_title:
            return jsonify({"error": "Book title is required"}), 400
        
        try:
            if method == 'traditional' and app.traditional_recommender:
                recommendations = app.traditional_recommender.recommend_books(book_title, count=5)
            elif app.enhanced_recommender:
                recommendations = app.enhanced_recommender.recommend_books(book_title, count=5)
            else:
                return jsonify({"error": "Recommendation models not available"}), 503
            
            return jsonify({
                "book": book_title,
                "method": method,
                "recommendations": recommendations
            })
        except Exception as e:
            logger.error(f"Error getting recommendations: {str(e)}")
            return jsonify({"error": "Internal server error"}), 500
    
    @app.route('/api/books/genre/<genre>')
    def get_books_by_genre(genre):
        """Get books filtered by genre"""
        try:
            if app.enhanced_recommender:
                books = app.enhanced_recommender.discover_new_books(genre=genre, min_rating=3.0)
            else:
                books = []
            
            return jsonify({
                "genre": genre,
                "book_count": len(books),
                "books": books
            })
        except Exception as e:
            logger.error(f"Error getting books by genre: {str(e)}")
            return jsonify({"error": "Internal server error"}), 500
    
    @app.route('/api/
                                                               
