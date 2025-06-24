from app import db
from flask_login import UserMixin
from datetime import datetime
import json

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    phone = db.Column(db.String(20), nullable=True)
    favorite_teams = db.Column(db.Text, nullable=True)  # JSON string
    loyalty_points = db.Column(db.Integer, default=0)
    membership_tier = db.Column(db.String(20), default='Bronze')  # Bronze, Silver, Gold, Platinum
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    bookings = db.relationship('Booking', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def get_favorite_teams(self):
        return json.loads(self.favorite_teams) if self.favorite_teams else []
    
    def set_favorite_teams(self, teams):
        self.favorite_teams = json.dumps(teams)

class Stadium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False, default='India')
    capacity = db.Column(db.Integer, nullable=False)
    rows = db.Column(db.Integer, nullable=False)
    seats_per_row = db.Column(db.Integer, nullable=False)
    amenities = db.Column(db.Text, nullable=True)  # JSON string for amenities
    weather_info = db.Column(db.Text, nullable=True)  # JSON string for weather conditions
    pitch_type = db.Column(db.String(50), default='Batting')  # Batting, Bowling, Balanced
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    matches = db.relationship('Match', backref='stadium', lazy=True, cascade='all, delete-orphan')
    
    def get_amenities(self):
        return json.loads(self.amenities) if self.amenities else []
    
    def set_amenities(self, amenities_list):
        self.amenities = json.dumps(amenities_list)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team1 = db.Column(db.String(100), nullable=False)
    team2 = db.Column(db.String(100), nullable=False)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'), nullable=False)
    match_date = db.Column(db.DateTime, nullable=False)
    match_type = db.Column(db.String(20), default='ODI')  # Test, ODI, T20, T10
    tournament = db.Column(db.String(100), nullable=True)
    ticket_price = db.Column(db.Float, nullable=False)
    vip_price = db.Column(db.Float, nullable=True)
    premium_price = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(20), default='Upcoming')  # Upcoming, Live, Completed, Cancelled
    weather_forecast = db.Column(db.String(100), nullable=True)
    live_score = db.Column(db.Text, nullable=True)  # JSON string for live score updates
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    bookings = db.relationship('Booking', backref='match', lazy=True, cascade='all, delete-orphan')
    
    def get_live_score(self):
        return json.loads(self.live_score) if self.live_score else {}
    
    def set_live_score(self, score_data):
        self.live_score = json.dumps(score_data)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    seat_row = db.Column(db.Integer, nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)
    seat_category = db.Column(db.String(20), default='Regular')  # Regular, VIP, Premium
    total_amount = db.Column(db.Float, nullable=False)
    discount_applied = db.Column(db.Float, default=0.0)
    loyalty_points_earned = db.Column(db.Integer, default=0)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_status = db.Column(db.String(20), default='completed')
    qr_code = db.Column(db.String(255), nullable=True)  # QR code for entry
    check_in_time = db.Column(db.DateTime, nullable=True)
    
    # Unique constraint to prevent double booking
    __table_args__ = (db.UniqueConstraint('match_id', 'seat_row', 'seat_number'),)

# New Models for Enhanced Features
class MatchReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    review_text = db.Column(db.Text, nullable=True)
    stadium_rating = db.Column(db.Integer, nullable=True)  # 1-5 stars
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref='reviews')
    match = db.relationship('Match', backref='reviews')

class SeatCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # Regular, VIP, Premium, Corporate
    description = db.Column(db.Text, nullable=True)
    benefits = db.Column(db.Text, nullable=True)  # JSON string for benefits list
    color_code = db.Column(db.String(7), default='#28a745')  # Hex color for visualization
    
    def get_benefits(self):
        return json.loads(self.benefits) if self.benefits else []

class PriceHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    seat_category = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_changed = db.Column(db.DateTime, default=datetime.utcnow)
    reason = db.Column(db.String(100), nullable=True)  # Dynamic pricing reason

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notification_type = db.Column(db.String(50), default='info')  # info, warning, success, danger
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    user = db.relationship('User', backref='notifications', lazy=True)
