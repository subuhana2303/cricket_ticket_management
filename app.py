import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "cricket-ticket-secret-key-2025")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure the database
database_url = os.environ.get("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL environment variable is not set")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

with app.app_context():
    # Import models to create tables
    import models
    db.create_all()
    
    # Create default admin user if it doesn't exist
    from werkzeug.security import generate_password_hash
    admin = models.User.query.filter_by(email='admin@cricket.com').first()
    if not admin:
        admin_user = models.User(
            name='Admin',
            email='admin@cricket.com',
            password_hash=generate_password_hash('admin123'),
            is_admin=True
        )
        db.session.add(admin_user)
        db.session.commit()
        logging.info("Default admin user created: admin@cricket.com / admin123")
    
    # Create sample data if no stadiums exist
    if not models.Stadium.query.first():
        from datetime import datetime, timedelta
        
        # Create stadiums
        stadium1 = models.Stadium(
            name='Lord\'s Cricket Ground',
            city='London',
            capacity=30000,
            rows=30,
            seats_per_row=50
        )
        stadium2 = models.Stadium(
            name='Melbourne Cricket Ground',
            city='Melbourne',
            capacity=100000,
            rows=40,
            seats_per_row=60
        )
        
        db.session.add_all([stadium1, stadium2])
        db.session.commit()
        
        # Create matches
        match1 = models.Match(
            team1='England',
            team2='Australia',
            stadium_id=stadium1.id,
            match_date=datetime.now() + timedelta(days=7),
            ticket_price=75.00
        )
        match2 = models.Match(
            team1='India',
            team2='Pakistan',
            stadium_id=stadium2.id,
            match_date=datetime.now() + timedelta(days=14),
            ticket_price=85.00
        )
        
        db.session.add_all([match1, match2])
        db.session.commit()
        logging.info("Sample stadiums and matches created")

# Import routes after app is configured
import routes
