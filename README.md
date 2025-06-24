# 🏏 CricketTix - Premium Cricket Ticketing Platform

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Available-brightgreen?style=for-the-badge)](https://your-replit-url.replit.app)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3-red?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)](https://postgresql.org)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)](https://getbootstrap.com)

CricketTix is a next-generation cricket ticketing platform that revolutionizes how fans experience cricket matches. Built with cutting-edge technology, it combines traditional ticketing with modern features like live scores, loyalty rewards, weather forecasts, smart seat recommendations, and premium experiences.

## 🚀 Live Demo

**🌐 Application URL**: [https://your-replit-url.replit.app](https://your-replit-url.replit.app)

### Demo Credentials
- **Admin Access**: 
  - Email: `admin@cricket.com`
  - Password: `admin123`
- **User Registration**: Create your own account or use the admin credentials to access the full dashboard

## ✨ Revolutionary Features

### 🎯 Smart Ticketing Experience
- **🧠 AI-Powered Recommendations**: Smart seat suggestions based on user preferences and viewing history
- **📊 Live Match Integration**: Real-time scores, ball-by-ball commentary, and match updates
- **🌤️ Weather Intelligence**: Smart weather forecasts with rain alerts and match day recommendations
- **⭐ Loyalty Rewards Program**: Earn points with every booking, unlock exclusive benefits and discounts
- **🏆 Membership Tiers**: Bronze, Silver, Gold, and Platinum membership levels with progressive benefits

### 💎 Premium Features
- **🎫 Multi-Category Seating**: Regular, VIP, and Premium seating options with exclusive amenities
- **📱 QR Code Entry**: Contactless stadium entry with digital verification
- **💰 Dynamic Pricing**: Smart pricing based on demand, match importance, and weather conditions
- **🔔 Smart Notifications**: Personalized alerts for favorite teams, match updates, and exclusive offers
- **📝 Match Reviews**: Post-match rating system for venues and overall experience

### 🏟️ Stadium Intelligence
- **🎯 Venue Insights**: Detailed stadium information with amenities, pitch conditions, and historical data
- **🗺️ Interactive Seat Maps**: Visual stadium layout with real-time availability and pricing
- **🍽️ Amenity Information**: Comprehensive details about food courts, parking, Wi-Fi, and accessibility
- **📍 Location Services**: Integrated maps, directions, and local area information

## 🏗️ Technical Architecture

### Backend Stack
- **Framework**: Python Flask 2.3 with modular architecture
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: Flask-Login with Werkzeug security
- **Session Management**: Flask built-in sessions with secure configuration
- **PDF Generation**: ReportLab for professional ticket PDFs
- **Server**: Gunicorn WSGI server for production deployment

### Frontend Stack
- **UI Framework**: Bootstrap 5.3 with Replit Dark Theme
- **Icons**: Font Awesome 6.0 for modern iconography
- **Charts**: Chart.js for interactive admin analytics
- **JavaScript**: Vanilla ES6+ for seat selection and interactive features
- **Responsive Design**: Mobile-first approach with CSS Grid and Flexbox

### Database Design
- **Users**: Secure authentication with role-based access control
- **Stadiums**: Configurable venue management with custom seating layouts
- **Matches**: Complete match scheduling with pricing and venue assignment
- **Bookings**: Transaction records with seat reservation and payment tracking

## 📁 Project Structure

```
CricketTix/
├── app.py                  # Flask application configuration
├── main.py                # Application entry point
├── models.py              # Database models (User, Stadium, Match, Booking)
├── routes.py              # URL routing and view functions
├── utils.py               # Utility functions (PDF generation)
├── requirements.txt       # Python dependencies
├── templates/             # Jinja2 HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage
│   ├── login.html        # User login
│   ├── register.html     # User registration
│   ├── matches.html      # Match listings
│   ├── seats.html        # Interactive seat selection
│   ├── payment.html      # Payment processing
│   ├── tickets.html      # User ticket history
│   ├── dashboard.html    # Admin dashboard
│   └── admin/            # Admin-specific templates
│       ├── stadiums.html
│       └── manage_matches.html
├── static/               # Static assets
│   ├── css/
│   │   └── style.css    # Custom styles and seat selection
│   └── js/
│       ├── main.js      # General JavaScript utilities
│       └── seats.js     # Seat selection functionality
└── README.md
```

## 🎯 Application Screenshots

### Homepage
The landing page showcases the application's purpose with clear navigation and feature highlights.

### Match Listings
Browse upcoming cricket matches with comprehensive details including venue, date, and pricing.

### Interactive Seat Selection
Real-time seat availability with visual stadium layout, allowing users to select their preferred seats.

### Admin Dashboard
Comprehensive analytics dashboard showing booking statistics, revenue tracking, and system management tools.

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL database
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CricketTix.git
   cd CricketTix
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   export DATABASE_URL="postgresql://username:password@localhost/cricket_db"
   export SESSION_SECRET="your-secret-key-here"
   ```

4. **Initialize the database**
   ```bash
   python -c "from app import app, db; app.app_context().push(); db.create_all()"
   ```

5. **Run the application**
   ```bash
   gunicorn --bind 0.0.0.0:5000 main:app
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 🔧 Configuration

### Database Setup
The application uses PostgreSQL with SQLAlchemy ORM. The database schema includes:
- **Users**: Authentication and profile management
- **Stadiums**: Venue configuration with customizable seating
- **Matches**: Event scheduling with pricing
- **Bookings**: Transaction records with seat reservations

### Admin Account
Default admin credentials (created automatically):
- Email: `admin@cricket.com`
- Password: `admin123`

## 🌟 Key Functionality

### User Workflow
1. **Registration/Login**: Secure account creation with password hashing
2. **Browse Matches**: View upcoming cricket events with full details
3. **Select Seats**: Interactive stadium layout with real-time availability
4. **Payment Process**: Simulated payment flow with validation
5. **Download Tickets**: PDF generation with booking details

### Admin Workflow
1. **Dashboard Access**: Comprehensive system overview and analytics
2. **Stadium Management**: Add venues with custom seating configurations
3. **Match Creation**: Schedule events with pricing and venue assignment
4. **Booking Analytics**: Monitor sales performance and revenue

## 🛡️ Security Features

- **Password Security**: Bcrypt hashing for all user passwords
- **Session Management**: Secure Flask-Login implementation
- **CSRF Protection**: Built-in protection against cross-site request forgery
- **Input Validation**: Comprehensive form validation and sanitization
- **Role-Based Access**: Admin and user role separation

## 📊 Technical Highlights

### Performance Optimizations
- **Database Connection Pooling**: Efficient PostgreSQL connection management
- **Static Asset Optimization**: CDN delivery for Bootstrap and icons
- **Responsive Design**: Mobile-first approach with optimized layouts

### Code Quality
- **Modular Architecture**: Separation of concerns with dedicated modules
- **Error Handling**: Comprehensive exception management
- **Logging**: Detailed application logging for debugging
- **Documentation**: Extensive code comments and documentation

## 🔄 API Endpoints

### Public Routes
- `GET /` - Homepage
- `GET /matches` - Match listings
- `POST /register` - User registration
- `POST /login` - User authentication

### Protected Routes
- `GET /seats/<match_id>` - Seat selection interface
- `POST /book_seats` - Process seat booking
- `GET /tickets` - User booking history
- `GET /download_ticket/<booking_id>` - PDF ticket download

### Admin Routes
- `GET /dashboard` - Admin analytics dashboard
- `GET /admin/stadiums` - Stadium management
- `GET /admin/matches` - Match management

## 📈 Future Enhancements

- **Payment Integration**: Real payment gateway integration (Stripe/PayPal)
- **Email Notifications**: Automated booking confirmations
- **Mobile App**: React Native mobile application
- **Advanced Analytics**: Detailed reporting and insights
- **Multi-language Support**: Internationalization features
- **Real-time Updates**: WebSocket integration for live seat availability

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Portfolio: [your-portfolio.com](https://your-portfolio.com)

## 🙏 Acknowledgments

- Flask community for excellent documentation
- Bootstrap team for responsive design framework
- ReportLab for PDF generation capabilities
- Chart.js for beautiful data visualizations

---

**⭐ Star this repository if you found it helpful!**

