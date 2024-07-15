# server/config.py

import os

class Config:
    DEBUG = True  # Set to False in production
    SECRET_KEY = 'your_secret_key'
    DATABASE = {
        'driver': 'sqlite',
        'name': os.path.join(os.path.dirname(__file__), 'ecommerce.db'),
        'host': 'localhost',
        'port': 5432,
        'username': 'your_username',
        'password': 'your_password'
    }
    MIDDLEWARE = [
        # Add middleware classes/functions here
    ]
    STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static/')
