# 🏏 CricketTix - Downloadable Version

## What You Get

This is a complete, self-contained version of **CricketTix** - a premium cricket ticketing platform that you can run on your own computer without any external dependencies or cloud services.

## One-Click Start

1. **Download** this folder to your computer
2. **Install Python** (if not already installed): https://python.org/downloads
3. **Open terminal/command prompt** in the CricketTix folder
4. **Run these commands:**
   ```bash
   pip install -r requirements_local.txt
   python run_local.py
   ```
5. **Open browser** and go to: http://localhost:5000

That's it! Your cricket ticketing platform is now running locally.

## Login Information

**Admin Account (Full Access):**
- Email: `admin@cricket.com`
- Password: `admin123`

**Regular User:**
- Create your own account by clicking "Register"

## What Works Locally

✅ **Complete CricketTix Experience**
- User registration and secure login
- Browse matches with weather forecasts
- Interactive seat selection system
- Multiple seating tiers (Regular, VIP, Premium)
- Complete booking process
- PDF ticket generation and download
- Admin dashboard with analytics
- Loyalty points and membership system
- Match reviews and ratings

✅ **Pre-loaded Sample Data**
- Famous cricket stadiums (Lord's, MCG, Eden Gardens)
- Exciting upcoming matches
- Different match formats (ODI, T20, Test)
- Ready-to-use admin account

✅ **No External Dependencies**
- Uses SQLite database (no PostgreSQL needed)
- All data stored locally
- No internet required after setup
- Works completely offline

## Key Features

### 🎯 For Cricket Fans
- **Smart Seat Selection**: Visual stadium layout with real-time availability
- **Weather Forecasts**: Plan your match day with weather information
- **Loyalty Rewards**: Earn points and unlock membership benefits
- **Multiple Categories**: Choose from Regular, VIP, or Premium seating
- **Digital Tickets**: Download PDF tickets with QR codes

### 📊 For Stadium Managers (Admin)
- **Match Management**: Create and schedule cricket matches
- **Stadium Setup**: Configure venues with custom seating layouts
- **Analytics Dashboard**: Track bookings, revenue, and user activity
- **User Management**: Monitor registrations and booking patterns
- **Pricing Control**: Set different prices for various seating categories

### 💎 Premium Features
- **Tournament Integration**: Organize matches by tournaments
- **Live Score Updates**: Display match status and scores
- **Review System**: Users can rate matches and stadiums
- **Notification System**: Alert users about important updates
- **Dynamic Pricing**: Adjust ticket prices based on demand

## File Structure

```
CricketTix/
├── 🚀 run_local.py          # START HERE - Main launcher
├── 📋 requirements.txt      # Python dependencies
├── 📖 SETUP_INSTRUCTIONS.md # Detailed setup guide
├── 📖 README_LOCAL.md       # This file
├── 
├── Core Application Files:
├── ⚙️ app_local.py          # Local app configuration
├── 🗃️ models.py             # Database structure
├── 🌐 routes.py             # Web pages and API
├── 🛠️ utils.py              # Helper functions
├── 
├── Web Interface:
├── 📁 templates/            # HTML pages
├── 📁 static/               # CSS, JavaScript, images
├── 
├── Database:
└── 🗃️ cricketTix_local.db   # Local database (auto-created)
```

## Troubleshooting

### Can't Install Dependencies?
```bash
# Try this instead:
python -m pip install -r requirements.txt
```

### Port 5000 Busy?
The app will automatically find another available port and show you the correct URL.

### Database Issues?
Delete the `cricketTix_local.db` file and restart - it will recreate automatically with fresh sample data.

### Python Not Found?
Download and install Python from: https://python.org/downloads
Make sure to check "Add to PATH" during installation.

## Customization

### Add Your Own Matches
1. Login as admin (`admin@cricket.com` / `admin123`)
2. Go to "Admin Dashboard"
3. Click "Manage Matches" → "Add New Match"
4. Fill in the details and save

### Modify Stadiums
1. Access admin dashboard
2. Go to "Manage Stadiums"
3. Add new venues or edit existing ones
4. Configure seating layout and amenities

### Change Branding
- Edit templates in `templates/` folder
- Modify styles in `static/css/style.css`
- Replace logo/images in `static/images/`

## Production Deployment

To deploy this application to a web server:

1. **Use PostgreSQL** instead of SQLite for better performance
2. **Set environment variables**:
   ```bash
   export DATABASE_URL="postgresql://user:pass@host/database"
   export SESSION_SECRET="random-secure-secret-key"
   ```
3. **Use Gunicorn** or similar WSGI server instead of Flask development server
4. **Configure reverse proxy** (nginx/Apache) with HTTPS

## Technical Details

- **Backend**: Python Flask with SQLAlchemy ORM
- **Database**: SQLite (local) / PostgreSQL (production)
- **Frontend**: Bootstrap 5 with responsive design
- **Authentication**: Flask-Login with secure password hashing
- **PDF Generation**: ReportLab for ticket creation
- **Charts**: Chart.js for admin analytics

## License & Usage

This is a complete, functional cricket ticketing platform. You can:
- ✅ Use it for personal projects
- ✅ Modify and customize it
- ✅ Learn from the code structure
- ✅ Deploy it for your cricket club/organization

## Support

If you need help:
1. Check `SETUP_INSTRUCTIONS.md` for detailed troubleshooting
2. Review error messages in the terminal
3. Try deleting the database file and restarting
4. Ensure Python 3.8+ is installed

---

**Enjoy your complete CricketTix platform! 🏏**

*Start with: `python run_local.py`*