# app_local.py
"""
CricketTix Local Configuration and DB Setup
This file sets up Flask app, database (SQLite), models, and seeds sample data.
"""
import os
import logging
from datetime import datetime, timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import json
from werkzeug.security import generate_password_hash
from werkzeug.middleware.proxy_fix import ProxyFix

# ----------------------------
# Logging
# ----------------------------
logging.basicConfig(level=logging.INFO)

# ----------------------------
# Flask App Setup
# ----------------------------
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# ----------------------------
# Database Configuration
# ----------------------------
database_url = os.environ.get("DATABASE_URL", "sqlite:///cricketTix_local.db")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ----------------------------
# Flask-Login Setup
# ----------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

# ----------------------------
# Models
# ----------------------------
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    loyalty_points = db.Column(db.Integer, default=0)
    membership_tier = db.Column(db.String(20), default='Bronze')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Stadium(db.Model):
    __tablename__ = 'stadiums'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False, default='India')
    capacity = db.Column(db.Integer, nullable=False)

class Match(db.Model):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key=True)
    team1 = db.Column(db.String(100), nullable=False)
    team2 = db.Column(db.String(100), nullable=False)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadiums.id'), nullable=False)
    match_date = db.Column(db.DateTime, nullable=False)
    match_type = db.Column(db.String(20), default='ODI')
    ticket_price = db.Column(db.Float, nullable=False)

# ----------------------------
# Database Setup & Sample Data
# ----------------------------
def setup_database():
    """Create tables and insert sample data"""
    logging.info("Setting up database...")
    db.drop_all()
    db.create_all()

    # Add admin user
    admin = User(
        name="Admin User",
        email="admin@cricket.com",
        password_hash=generate_password_hash("admin123"),
        is_admin=True,
        loyalty_points=1000,
        membership_tier="Platinum"
    )
    db.session.add(admin)

    # Add stadiums
    stadiums = [
        Stadium(name="Lord's Cricket Ground", city="London", country="England", capacity=30000),
        Stadium(name="Melbourne Cricket Ground", city="Melbourne", country="Australia", capacity=100000),
        Stadium(name="Eden Gardens", city="Kolkata", country="India", capacity=66000)
    ]
    db.session.add_all(stadiums)
    db.session.commit()

    # Add matches
    matches = [
        Match(team1="England", team2="Australia", stadium_id=stadiums[0].id, match_date=datetime.now() + timedelta(days=7), match_type="ODI", ticket_price=75.0),
        Match(team1="India", team2="Pakistan", stadium_id=stadiums[1].id, match_date=datetime.now() + timedelta(days=14), match_type="T20", ticket_price=85.0),
        Match(team1="New Zealand", team2="South Africa", stadium_id=stadiums[2].id, match_date=datetime.now() + timedelta(days=21), match_type="Test", ticket_price=65.0)
    ]
    db.session.add_all(matches)
    db.session.commit()

    logging.info("Database setup complete!")
    logging.info("Admin credentials: admin@cricket.com / admin123")

# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    setup_database()
    logging.info("Starting Flask development server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
