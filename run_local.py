#!/usr/bin/env python3
"""
CricketTix - Local Development Server
Run this file to start the application locally
"""
import os
import sys
from datetime import datetime, timedelta

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set environment variables for local development
os.environ['DATABASE_URL'] = 'sqlite:///cricketTix_local.db'
os.environ['SESSION_SECRET'] = 'your-super-secret-key-change-this-in-production'
os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = '1'

from app_local import app, db
import models

def setup_local_database():
    """Setup local SQLite database with sample data"""
    print("Setting up local database...")
    
    with app.app_context():
        # Drop all tables and recreate (for fresh start)
        db.drop_all()
        db.create_all()
        
        # Create admin user
        from werkzeug.security import generate_password_hash
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
        
        # Create sample stadiums
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
        stadium3 = models.Stadium(
            name='Eden Gardens',
            city='Kolkata',
            country='India',
            capacity=66000,
            rows=35,
            seats_per_row=55,
            pitch_type='Bowling',
            amenities='["Traditional Food", "Fan Shop", "Press Box", "Player Lounge", "Medical Room"]'
        )
        
        db.session.add_all([stadium1, stadium2, stadium3])
        db.session.commit()
        
        # Create sample matches
        matches = [
            models.Match(
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
            ),
            models.Match(
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
            ),
            models.Match(
                team1='New Zealand',
                team2='South Africa',
                stadium_id=stadium3.id,
                match_date=datetime.now() + timedelta(days=21),
                match_type='Test',
                tournament='Test Championship',
                ticket_price=65.00,
                vip_price=130.00,
                premium_price=200.00,
                weather_forecast='Clear skies, 28°C',
                status='Upcoming'
            ),
            models.Match(
                team1='Australia',
                team2='West Indies',
                stadium_id=stadium1.id,
                match_date=datetime.now() + timedelta(days=28),
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
        
        print("Database setup completed successfully!")
        print(f"Admin credentials: admin@cricket.com / admin123")
        print(f"Database file: cricketTix_local.db")

if __name__ == '__main__':
    print("=" * 60)
    print("  🏏 CricketTix - Premium Cricket Ticketing Platform")
    print("=" * 60)
    
    # Check if database exists, if not create it
    if not os.path.exists('cricketTix_local.db'):
        setup_local_database()
    
    print("\nStarting development server...")
    print("Access the application at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("-" * 60)
    
    # Start the Flask development server
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
        use_reloader=True
    )