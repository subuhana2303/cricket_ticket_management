"""
CricketTix Local Configuration
Modified version of app.py for local development with SQLite
"""
import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_login import LoginManager

# Configure logging
logging.basicConfig(level=logging.INFO)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create the app
app = Flask(__name__)

# Configuration for local development
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Database configuration - Use SQLite for local development
database_url = os.environ.get("DATABASE_URL", "sqlite:///cricketTix_local.db")

# Convert postgres:// to postgresql:// if needed (for compatibility)
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    import models
    return models.User.query.get(int(user_id))

# Create database tables and sample data
with app.app_context():
    import models  # Import models after db is initialized
    db.create_all()
    
    # Only create sample data if no users exist
    if not models.User.query.first():
        from werkzeug.security import generate_password_hash
        from datetime import datetime, timedelta
        
        # Create admin user
        admin = models.User(
            name='Admin User',
            email='admin@cricket.com',
            password_hash=generate_password_hash('admin123'),
            is_admin=True,
            loyalty_points=1000,
            membership_tier='Platinum'
        )
        db.session.add(admin)
        db.session.commit()
        logging.info("Admin user created: admin@cricket.com / admin123")

# Import routes after app is configured
import routes