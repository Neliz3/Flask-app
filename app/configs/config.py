from dotenv import load_dotenv
import os

# Initialize environment variables
load_dotenv('/home/elizabeth/flask-app/app/configs/.env')

secret_key = os.urandom(12)
