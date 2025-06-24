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
        
        # Create stadiums with enhanced features
        stadium1 = models.Stadium(
            name='Lord\'s Cricket Ground',
            city='London',
            country='England',
            capacity=30000,
            rows=30,
            seats_per_row=50,
            pitch_type='Batting',
            amenities='["Premium Restaurant", "VIP Lounge", "Museum", "Gift Shop", "Wi-Fi", "Parking"]'
        )
        stadium2 = models.Stadium(
            name='Melbourne Cricket Ground',
            city='Melbourne', 
            country='Australia',
            capacity=100000,
            rows=40,
            seats_per_row=60,
            pitch_type='Balanced',
            amenities='["Food Courts", "Sports Bar", "Merchandise Store", "Family Zone", "Medical Center", "Disabled Access"]'
        )
        
        db.session.add_all([stadium1, stadium2])
        db.session.commit()
        
        # Create matches with enhanced features
        match1 = models.Match(
            team1='England',
            team2='Australia',
            stadium_id=stadium1.id,
            match_date=datetime.now() + timedelta(days=7),
            match_type='ODI',
            tournament='Cricket World Cup 2025',
            ticket_price=75.00,
            vip_price=150.00,
            premium_price=250.00,
            weather_forecast='Sunny, 26°C',
            status='Upcoming'
        )
        match2 = models.Match(
            team1='India',
            team2='Pakistan',
            stadium_id=stadium2.id,
            match_date=datetime.now() + timedelta(days=14),
            match_type='T20',
            tournament='Asia Cup 2025',
            ticket_price=85.00,
            vip_price=170.00,
            premium_price=300.00,
            weather_forecast='Partly cloudy, 24°C',
            status='Upcoming'
        )
        match3 = models.Match(
            team1='New Zealand',
            team2='South Africa',
            stadium_id=stadium1.id,
            match_date=datetime.now() + timedelta(days=21),
            match_type='Test',
            tournament='Test Championship',
            ticket_price=65.00,
            vip_price=130.00,
            premium_price=200.00,
            weather_forecast='Clear skies, 28°C',
            status='Upcoming'
        )
        
        db.session.add_all([match1, match2, match3])
        db.session.commit()
        logging.info("Sample stadiums and matches created")

# Import routes after app is configured
import routes
