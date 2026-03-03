import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database Configuration
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'books.json')
    
    # ML Model Configuration
    TRANSFORMER_MODEL = 'all-MiniLM-L6-v2'
    MAX_RECOMMENDATIONS = 10
    DEFAULT_SIMILARITY_THRESHOLD = 0.1
    
    # API Configuration
    API_PREFIX = '/api'
    API_VERSION = 'v1'
    
    # Logging Configuration
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FILE = 'logs/app.log'

class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = 'INFO'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE_PATH = 'tests/fixtures/sample_books.json'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
