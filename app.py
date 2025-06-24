# app.py

import os
import json
import logging
from flask import Flask
from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix
from extension import db

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "cricket-ticket-secret-key-2025")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///crickettix.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Please log in to access this page."

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

# Sample data setup
with app.app_context():
    import models
    db.create_all()

    from werkzeug.security import generate_password_hash
    from datetime import datetime, timedelta

    if not models.User.query.filter_by(email='admin@cricket.com').first():
        admin_user = models.User(
            name='Admin',
            email='admin@cricket.com',
            password_hash=generate_password_hash('admin123'),
            is_admin=True
        )
        db.session.add(admin_user)
        db.session.commit()
        logging.info("✅ Admin user created")

    if not models.Stadium.query.first():
        # Create stadiums
        s1 = models.Stadium(
            name="Lord's Cricket Ground",
            city="London",
            country="England",
            capacity=30000,
            rows=30,
            seats_per_row=50,
            pitch_type="Batting",
            amenities=json.dumps(["Premium Restaurant", "VIP Lounge", "Museum", "Wi-Fi"])
        )
        s2 = models.Stadium(
            name="Melbourne Cricket Ground",
            city="Melbourne",
            country="Australia",
            capacity=100000,
            rows=40,
            seats_per_row=60,
            pitch_type="Balanced",
            amenities=json.dumps(["Food Courts", "Sports Bar", "Medical Center"])
        )
        s3 = models.Stadium(
            name="Eden Gardens",
            city="Kolkata",
            country="India",
            capacity=66000,
            rows=35,
            seats_per_row=55,
            pitch_type="Bowling",
            amenities=json.dumps(["Fan Shop", "Press Box", "Player Lounge"])
        )

        db.session.add_all([s1, s2, s3])
        db.session.commit()

        # Create matches
        matches = [
            models.Match(
                team1='England',
                team2='Australia',
                stadium_id=s1.id,
                match_date=datetime.now() + timedelta(days=5),
                match_type='ODI',
                tournament='Cricket World Cup 2025',
                ticket_price=75.00,
                vip_price=150.00,
                premium_price=250.00,
                weather_forecast='Sunny, 26°C',
                status='Upcoming'
            ),
            models.Match(
                team1='India',
                team2='Pakistan',
                stadium_id=s2.id,
                match_date=datetime.now() + timedelta(days=10),
                match_type='T20',
                tournament='Asia Cup 2025',
                ticket_price=85.00,
                vip_price=170.00,
                premium_price=300.00,
                weather_forecast='Cloudy, 24°C',
                status='Upcoming'
            ),
            models.Match(
                team1='New Zealand',
                team2='South Africa',
                stadium_id=s3.id,
                match_date=datetime.now() + timedelta(days=15),
                match_type='Test',
                tournament='Championship Test',
                ticket_price=65.00,
                vip_price=130.00,
                premium_price=200.00,
                weather_forecast='Clear, 28°C',
                status='Upcoming'
            ),
            models.Match(
                team1='Australia',
                team2='West Indies',
                stadium_id=s1.id,
                match_date=datetime.now() + timedelta(days=20),
                match_type='T20',
                tournament='ICC T20 Series',
                ticket_price=70.00,
                vip_price=140.00,
                premium_price=220.00,
                weather_forecast='Overcast, 22°C',
                status='Upcoming'
            )
        ]
        db.session.add_all(matches)
        db.session.commit()
        logging.info("✅ Stadiums and full sample matches added.")

# Load routes
import routes
