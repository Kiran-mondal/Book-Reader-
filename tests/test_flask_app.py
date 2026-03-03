import pytest
import json
import tempfile
import os
from app import create_app

class TestFlaskApp:
 @pytest.fixture
 def app(self):
 """Create and configure a new app instance for each test"""
 with tempfile.TemporaryDirectory() as temp_dir:
 app = create_app('testing')
 app.config['TESTING'] = True
 app.config['DATABASE_PATH'] = os.path.join(temp_dir, 'test_books.json')
 return app
 
 @pytest.fixture
 def client(self, app):
 """A test client for the app"""
 return app.test_client()
 
 def test_home_page(self, client):
 """Test the home page"""
 response = client.get('/')
 assert response.status_code == 200
 data = json.loads(response.data)
 assert 'message' in data
 
 def test_api_docs_endpoint(self, client):
 """Test the API documentation endpoint"""
 response = client.get('/api/docs')
 assert response.status_code == 200
 data = json.loads(response.data)
 assert 'title' in data
 assert 'version' in data
 
 def test_health_check(self, client):
 """Test the health check endpoint"""
 response = client.get('/api/health')
 assert response.status_code == 200
 data = json.loads(response.data)
 assert 'status' in data
 
 def test_recommend_endpoint_missing_param(self, client):
 """Test recommend endpoint without book parameter"""
 response = client.get('/api/recommend')
 assert response.status_code == 400
 data = json.loads(response.data)
 assert 'error' in data
 
 def test_recommend_endpoint_invalid_method(self, client):
 """Test recommend endpoint with invalid method"""
 response = client.get('/api/recommend?book=Test&method=invalid')
 assert response.status_code == 500
 
 def test_recommend_endpoint_valid(self, client, test_data):
 """Test recommend endpoint with valid parameters"""
 response = client.get('/api/recommend?book=Test Book')
 assert response.status_code == 200
 data = json.loads(response.data)
 assert 'book' in data
 assert 'recommendations' in data
 
 @pytest.fixture
 def test_data(self):
 """Create test data file"""
 test_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
 test_books = [
 {
 "id": 1, "title": "Test Book 1", "author": "Test Author",
 "genre": "Fiction", "description": "Test description",
 "themes": "test", "rating": 4.0
 }
 ]
 json.dump(test_books, test_file)
 test_file.close()
 return test_file.name
 
 def test_books_by_genre(self, client, test_data):
 """Test getting books by genre"""
 response = client.get('/api/books/genre/Fiction')
 assert response.status_code == 200
 data = json.loads(response.data)
 assert 'genre' in data
 assert 'books' in data
 
 def test_trending_books(self, client, test_data):
 """Test trending books endpoint"""
 response = client.get('/api/trending')
 assert response.status_code == 200
 data = json.loads(response.data)
 assert 'trending_books' in data
  
