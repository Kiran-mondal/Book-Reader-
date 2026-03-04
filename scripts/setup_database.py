#!/usr/bin/env python3
"""
Setup script to initialize the AI Book Recommender database
"""

import json
import os
import sys
from pathlib import Path
from models.data_loader import DataLoader
from models.enhanced_recommender import EnhancedBookRecommender

def create_sample_database():
    """Create sample book data"""
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
            "id": 5,
            "title": "The God of Small Things",
            "author": "Arundhati Roy",
            "genre": "Literary Fiction",
            "description": "A family saga set in Kerala.",
            "themes": "indian literature, family, caste issues",
            "rating": 4.1,
            "year": 1997,
            "pages": 340,
            "language": "English"
        }
    ]
    
    # Create data directory if it doesn't exist
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Save sample data
    output_file = data_dir / "books.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sample_books, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Sample database created at {output_file}")
    return output_file

def setup_directories():
    """Create necessary directories"""
    directories = [
        "data",
        "data/backups",
        "logs",
        "models",
        "web/static/css",
        "web/static/js",
        "web/templates",
        "tests/fixtures",
        "deployment/docker",
        "docs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("✅ All necessary directories created.")

def main():
    """Main setup function"""
    print("🚀 Setting up AI Book Recommender...")
    
    try:
        # Create directories
        setup_directories()
        
        # Create sample database
        db_file = create_sample_database()
        
        # Create auto-loader
        create_auto_loader()
        
        print("✅ Setup completed successfully!")
        print("\n📋 Next steps:")
        print("1. Run 'python app.py' to start the web application")
        print("2. Visit http://localhost:5000 to use the application")
        print("3. Run 'python scripts/setup_database.py' if you need to reset the database")
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1)

def create_auto_loader():
    """Create auto-loader script"""
    loader_content = '''#!/usr/bin/env python3
"""
Auto-loader for the AI Book Recommender
"""

import sys
import os
from pathlib import Path

# Add the project directory to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def main():
    from app import create_app
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
'''
    
    with open("auto_loader.py", "w") as f:
        f.write(loader_content)
    
    # Make it executable
    os.chmod("auto_loader.py", 0o755)

if __name__ == "__main__":
    main()
