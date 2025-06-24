# models.py
from extension import db
from flask_login import UserMixin
from datetime import datetime
import json

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    phone = db.Column(db.String(20), nullable=True)
    favorite_teams = db.Column(db.Text, nullable=True)
    loyalty_points = db.Column(db.Integer, default=0)
    membership_tier = db.Column(db.String(20), default='Bronze')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    bookings = db.relationship('Booking', backref='user', lazy=True, cascade='all, delete-orphan')

    def get_favorite_teams(self):
        return json.loads(self.favorite_teams) if self.favorite_teams else []

    def set_favorite_teams(self, teams):
        self.favorite_teams = json.dumps(teams)

class Stadium(db.Model):
    __tablename__ = 'stadiums'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False, default='India')
    capacity = db.Column(db.Integer, nullable=False)
    rows = db.Column(db.Integer, nullable=False)
    seats_per_row = db.Column(db.Integer, nullable=False)
    amenities = db.Column(db.Text, nullable=True)
    weather_info = db.Column(db.Text, nullable=True)
    pitch_type = db.Column(db.String(50), default='Batting')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    matches = db.relationship('Match', backref='stadium', lazy=True, cascade='all, delete-orphan')

    def get_amenities(self):
        return json.loads(self.amenities) if self.amenities else []

    def set_amenities(self, amenities_list):
        self.amenities = json.dumps(amenities_list)

class Match(db.Model):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key=True)
    team1 = db.Column(db.String(100), nullable=False)
    team2 = db.Column(db.String(100), nullable=False)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadiums.id'), nullable=False)
    match_date = db.Column(db.DateTime, nullable=False)
    match_type = db.Column(db.String(20), default='ODI')
    tournament = db.Column(db.String(100), nullable=True)
    ticket_price = db.Column(db.Float, nullable=False)
    vip_price = db.Column(db.Float, nullable=True)
    premium_price = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(20), default='Upcoming')
    weather_forecast = db.Column(db.String(100), nullable=True)
    live_score = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    bookings = db.relationship('Booking', backref='match', lazy=True, cascade='all, delete-orphan')

    def get_live_score(self):
        return json.loads(self.live_score) if self.live_score else {}

    def set_live_score(self, score_data):
        self.live_score = json.dumps(score_data)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    seat_row = db.Column(db.Integer, nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)
    seat_category = db.Column(db.String(20), default='Regular')
    total_amount = db.Column(db.Float, nullable=False)
    discount_applied = db.Column(db.Float, default=0.0)
    loyalty_points_earned = db.Column(db.Integer, default=0)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_status = db.Column(db.String(20), default='completed')
    qr_code = db.Column(db.String(255), nullable=True)
    check_in_time = db.Column(db.DateTime, nullable=True)

    __table_args__ = (db.UniqueConstraint('match_id', 'seat_row', 'seat_number'),)

class MatchReview(db.Model):
    __tablename__ = 'match_reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text, nullable=True)
    stadium_rating = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='reviews')
    match = db.relationship('Match', backref='reviews')

class SeatCategory(db.Model):
    __tablename__ = 'seat_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    benefits = db.Column(db.Text, nullable=True)
    color_code = db.Column(db.String(7), default='#28a745')

    def get_benefits(self):
        return json.loads(self.benefits) if self.benefits else []

class PriceHistory(db.Model):
    __tablename__ = 'price_history'
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    seat_category = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_changed = db.Column(db.DateTime, default=datetime.utcnow)
    reason = db.Column(db.String(100), nullable=True)

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notification_type = db.Column(db.String(50), default='info')
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='notifications', lazy=True)
