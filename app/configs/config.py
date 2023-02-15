from dotenv import load_dotenv
import os

# Initialize environment variables
load_dotenv('/home/elizabeth/flask-app/app/configs/.env')

# Flask app
secret_key = os.urandom(12)

# Database settings
db_uri = os.getenv("DB_URI")
