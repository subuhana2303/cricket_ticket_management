# 🏏 CricketTix - Local Setup Instructions

## Quick Start (5 minutes)

### Option 1: Using Python (Recommended)

1. **Download and Extract**
   - Download the CricketTix project folder
   - Extract to your desired location

2. **Install Python Requirements**
   ```bash
   cd CricketTix
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python run_local.py
   ```

4. **Access the Application**
   - Open your browser and go to: `http://localhost:5000`
   - Admin login: `admin@cricket.com` / `admin123`

### Option 2: Using Virtual Environment (Recommended for Developers)

1. **Create Virtual Environment**
   ```bash
   cd CricketTix
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application**
   ```bash
   python run_local.py
   ```

## Features Available Locally

✅ **Full CricketTix Experience**
- User registration and authentication
- Match browsing with weather forecasts
- Interactive seat selection
- Multiple seating categories (Regular, VIP, Premium)
- Booking system with PDF ticket generation
- Admin dashboard for managing venues and matches
- Loyalty points and membership tiers
- Match reviews and ratings

✅ **Sample Data Included**
- Pre-configured stadiums (Lord's, MCG, Eden Gardens)
- Sample matches with different formats (ODI, T20, Test)
- Admin account ready to use
- SQLite database (no external database required)

## Default Credentials

**Admin Account:**
- Email: `admin@cricket.com`
- Password: `admin123`

## Troubleshooting

### Common Issues

1. **"ModuleNotFoundError" when running**
   ```bash
   pip install -r requirements.txt
   ```

2. **Port 5000 already in use**
   - The app will automatically find another available port
   - Or kill the process using port 5000

3. **Permission errors on Windows**
   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Database errors**
   - Delete `cricketTix_local.db` file and restart
   - The app will recreate the database automatically

### System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB free space
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

## File Structure

```
CricketTix/
├── run_local.py           # Local development server
├── requirements.txt       # Python dependencies
├── app.py                # Flask application setup
├── models.py             # Database models
├── routes.py             # URL routes and views
├── utils.py              # Utility functions
├── templates/            # HTML templates
├── static/               # CSS, JS, images
├── cricketTix_local.db   # SQLite database (created automatically)
└── SETUP_INSTRUCTIONS.md # This file
```

## Customization

### Adding Your Own Data

1. **Run the application once** to create the database
2. **Login as admin** (`admin@cricket.com` / `admin123`)
3. **Use the admin dashboard** to:
   - Add new stadiums
   - Create matches
   - Manage users
   - View analytics

### Modifying the Application

- **Templates**: Edit HTML files in `templates/` folder
- **Styles**: Modify CSS in `static/css/` folder
- **Database**: Update models in `models.py`
- **Features**: Add new routes in `routes.py`

## Production Deployment

For production deployment, consider:

1. **Use PostgreSQL** instead of SQLite
2. **Set proper environment variables**:
   ```bash
   export DATABASE_URL="postgresql://user:pass@localhost/cricketTix"
   export SESSION_SECRET="your-random-secret-key"
   ```
3. **Use a production WSGI server** like Gunicorn
4. **Enable HTTPS** and proper security headers

## Support

If you encounter any issues:

1. Check the console output for error messages
2. Ensure all requirements are installed correctly
3. Try deleting the database file and restarting
4. Make sure Python 3.8+ is installed

## Features Overview

**🎯 Smart Ticketing**
- AI-powered seat recommendations
- Real-time weather forecasts
- Dynamic pricing system

**💎 Premium Experience**
- Multiple seating categories
- QR code entry system
- Loyalty rewards program

**📊 Analytics Dashboard**
- Revenue tracking
- Booking analytics
- User management

**🏟️ Stadium Management**
- Interactive seat maps
- Venue amenities information
- Capacity management

Enjoy your CricketTix experience! 🏏