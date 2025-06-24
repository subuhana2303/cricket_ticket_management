# CricketTix - Premium Cricket Ticketing Platform

## Overview
CricketTix is a next-generation cricket ticketing platform that revolutionizes how fans experience cricket matches. Built with cutting-edge technology using Python Flask and PostgreSQL, it combines traditional ticketing with modern features like live scores, loyalty rewards, weather forecasts, smart seat recommendations, QR code entry, and premium experiences. The platform offers multiple seating categories, dynamic pricing, and a comprehensive admin dashboard with advanced analytics.

## System Architecture

### Backend Architecture
- **Framework**: Python Flask with modular architecture and SQLAlchemy ORM
- **Database**: PostgreSQL with advanced features (loyalty points, reviews, notifications)
- **Authentication**: Flask-Login with Werkzeug security and bcrypt password hashing
- **Session Management**: Flask built-in sessions with secure configuration
- **Database Models**: Enhanced SQLAlchemy models with JSON fields and advanced relationships
- **Features**: Dynamic pricing, loyalty rewards, weather integration, QR code generation

### Frontend Architecture
- **UI Framework**: Bootstrap CSS with Replit Dark Theme
- **Icons**: Font Awesome 6.0
- **Charts**: Chart.js for admin analytics
- **Interactive Elements**: Vanilla JavaScript with Bootstrap components
- **Responsive Design**: Mobile-first Bootstrap grid system

### Application Structure
- **Entry Point**: `main.py` - WSGI application entry
- **Core App**: `app.py` - Flask app configuration and initialization
- **Models**: `models.py` - Database schema definitions
- **Routes**: `routes.py` - URL routing and view logic
- **Utilities**: `utils.py` - PDF generation and helper functions

## Key Components

### Database Schema
1. **User Model**: User authentication and profile management
   - id, name, email, password_hash, is_admin, created_at
   - One-to-many relationship with bookings

2. **Stadium Model**: Venue management with seating configuration
   - id, name, city, capacity, rows, seats_per_row, created_at
   - One-to-many relationship with matches

3. **Match Model**: Cricket match scheduling and pricing
   - id, team1, team2, stadium_id, match_date, ticket_price, created_at
   - Foreign key to stadium, one-to-many relationship with bookings

4. **Booking Model**: Ticket booking transactions
   - id, user_id, match_id, seat_row, seat_number, total_amount, booking_date, payment_status
   - Foreign keys to user and match models

### Authentication System
- **Registration**: Secure user registration with password hashing
- **Login/Logout**: Session-based authentication using Flask-Login
- **Admin Access**: Role-based access control for administrative functions
- **Default Admin**: Auto-created admin account (admin@cricket.com)

### Seat Selection System
- **Dynamic Grid**: JavaScript-powered interactive seat selection
- **Real-time Availability**: Live seat status checking
- **Visual Feedback**: Color-coded seat states (available, selected, booked)
- **Booking Validation**: Prevents double-booking with database constraints

### PDF Generation
- **ReportLab Integration**: Professional PDF ticket generation
- **Ticket Details**: Match info, seat details, booking confirmation
- **Download System**: Direct PDF download after booking completion

## Data Flow

1. **User Registration/Login**
   - User submits credentials → Backend validation → Session creation
   - Password hashing using Werkzeug security utilities

2. **Match Browsing**
   - Database query for upcoming matches → Template rendering with match details
   - Stadium information included via SQLAlchemy relationships

3. **Seat Selection**
   - Match selection → Seat availability check → Interactive grid display
   - JavaScript handles UI interactions, Flask manages booking state

4. **Booking Process**
   - Seat selection → Payment simulation → Database transaction
   - PDF generation → Booking confirmation → Email-ready ticket

5. **Admin Operations**
   - Role verification → CRUD operations on stadiums/matches
   - Analytics dashboard with Chart.js visualizations

## External Dependencies

### Python Packages
- **Flask**: Web framework and routing
- **Flask-SQLAlchemy**: ORM and database management
- **Flask-Login**: User session management
- **ReportLab**: PDF generation for tickets
- **Werkzeug**: Security utilities and password hashing
- **Gunicorn**: WSGI HTTP server for deployment

### Frontend Libraries
- **Bootstrap**: Responsive UI framework with Replit dark theme
- **Font Awesome**: Icon library for enhanced UI
- **Chart.js**: Data visualization for admin dashboard
- **Vanilla JavaScript**: Custom interactive functionality

### Database
- **SQLite**: Embedded database for simplified deployment
- **Auto-migration**: Database tables created automatically on startup

## Deployment Strategy

### Replit Configuration
- **Runtime**: Python 3.11 with Nix package management
- **Server**: Gunicorn WSGI server binding to 0.0.0.0:5000
- **Autoscaling**: Configured for automatic scaling based on demand
- **Environment**: Development and production configurations supported

### Database Strategy
- **File-based SQLite**: Simplifies deployment without external database dependencies
- **Connection Pooling**: Configured with pool recycling and pre-ping for reliability
- **Automatic Schema Creation**: Tables created on first application start

### Static Assets
- **CDN Integration**: Bootstrap and Font Awesome served from CDN
- **Local Assets**: Custom CSS and JavaScript served from static directory
- **Responsive Design**: Mobile-optimized interface

## Changelog
- June 24, 2025: Enhanced to CricketTix premium platform with advanced features
  - Added PostgreSQL database with enhanced schema
  - Implemented loyalty rewards and membership tiers
  - Added weather forecasts and match insights
  - Enhanced UI with premium features showcase
  - Added multiple seating categories (Regular, VIP, Premium)
  - Implemented QR code entry system
  - Added match reviews and rating system
  - Enhanced admin dashboard with advanced analytics
- June 24, 2025: Initial cricket ticket management system setup

## User Preferences
Preferred communication style: Simple, everyday language.