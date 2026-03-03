import pytest
from web.app import app as web_app

class TestWebApp:
 @pytest.fixture
 def client(self):
 """A test client for the web app"""
 web_app.config['TESTING'] = True
 with web_app.test_client() as client:
 yield client
 
 def test_homepage(self, client):
 """Test the homepage"""
 response = client.get('/')
 assert response.status_code == 200
 assert b'Discover Your Next Favorite Book' in response.data
 
 def test_genre_page(self, client):
 """Test the genre browsing page"""
 response = client.get('/genre')
 assert response.status_code == 200
 
 def test_trending_page(self, client):
 """Test the trending books page"""
 response = client.get('/trending')
 assert response.status_code == 200
 
 def test_book_details_page(self, client):
 """Test the book details page"""
 response = client.get('/book/1')
 assert response.status_code == 200
 
 def test_api_docs_page(self, client):
 """Test the API documentation page"""
 response = client.get('/api-docs')
 assert response.status_code == 200
 
 def test_static_css(self, client):
 """Test that static CSS files are accessible"""
 response = client.get('/static/css/style.css')
 assert response.status_code == 200
 assert b'body' in response.data
 
 def test_static_js(self, client):
 """Test that static JS files are accessible"""
 response = client.get('/static/js/main.js')
 assert response.status_code == 200
  
