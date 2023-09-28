from flask_frozen import Freezer
from app import app  # Import your Flask app instance

# Create a Freezer instance with your Flask app
freezer = Freezer(app)

if __name__ == '__main__':
    # Freeze the Flask app into static files
    freezer.freeze()
