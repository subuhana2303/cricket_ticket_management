# 🏏 CricketTix - Premium Cricket Ticketing Platform

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Available-brightgreen?style=for-the-badge)](https://your-demo-url.com)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3-red?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)](https://postgresql.org)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)](https://getbootstrap.com)

CricketTix is a next-generation cricket ticketing platform that revolutionizes how fans experience cricket matches. Built with cutting-edge technology, it combines traditional ticketing with modern features like live scores, loyalty rewards, weather forecasts, smart seat recommendations, and premium experiences.This project was our Second-year dbms project,Implemented as a fundational step in our learning joureny.

---

## 🚀 Features

- 👤 User registration and login (with admin support)
- 🎟️ Book match tickets by selecting available seats
- 🏟️ Stadium management with amenities and capacity
- 🏏 Match creation with details like teams, type, date, and stadium
- 📊 Admin dashboard (create stadiums, matches, view bookings)
- 📅 Upcoming match listing
- ✅ Secure login with Flask-Login
- 🔒 Passwords hashed using `werkzeug.security`
- 💬 Match reviews and stadium ratings
- 📥 Notifications system
- 📈 Price history tracking

---

## 🏗️ Technical Stack

| Layer     | Technology                                                                 |
|-----------|----------------------------------------------------------------------------|
| **Backend** | - Python Flask 2.3  <br> - PostgreSQL + SQLAlchemy ORM  <br> - Flask-Login & Werkzeug for Authentication <br> - ReportLab for PDF generation <br> - Gunicorn WSGI server |
| **Frontend** | - Bootstrap 5.3  <br> - Font Awesome & Chart.js <br> - Vanilla JavaScript (ES6+) <br> - CSS Grid & Flexbox for responsive layout |

---
## 🚀 Live Demo

🌐 **Live video**: [click here to watch](https://drive.google.com/file/d/15AAF1ic2W0d5k2iKRcfWkU8xulglvVDT/view?usp=drivesdk)
🖼️ **Screenshots outputs are:**
- home pages
![homepages](2025-06-24.png)
- login
![login](login.png)
- matches availbale
![matches avail](2025-06-24-1.png)
- seat selection
![seat selection](<seat selection.png>)
- payment
![payment](<seat selection-1.png>)
---
### Demo Credentials
- **Admin Access**:  
  - Email: `admin@cricket.com`  
  - Password: `admin123`  
- **User Access**: Create your own account or use the admin login

---

## 📁 Folder Structure

```
CricketTicketManager/
│
├── app.py                  # Main Flask app and app context setup
├── main.py                 # Entry point: from app import app
├── extension.py            # Initialize extensions like db, login_manager
├── config.py               # (Optional) Config class for DB and secret keys
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── models.py               # SQLAlchemy models (User, Match, Stadium, etc.)
├── routes.py               # All route handlers (user/admin/auth/match/bookings)
│
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/              # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── matches.html
│   ├── booking.html
│   ├── dashboard.html
│   └── ...
│
├── instance/               # Instance folder for database and config
│   └── crickettix.db       # SQLite DB (or use PostgreSQL)
│
├── migrations/             # For database migrations (if using Flask-Migrate)
│
└── .venv/                  # Python virtual environment

````

---


## ⚙️ Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL
- Git (optional)

### Steps


# Clone the repo
git clone https://github.com/yourusername/CricketTix.git
cd CricketTix

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DATABASE_URL="postgresql://username:password@localhost/cricket_db"
export SESSION_SECRET="your-secret-key"

# Initialize the database
python -c "from app import app, db; app.app_context().push(); db.create_all()"

# Run the server
gunicorn --bind 0.0.0.0:5000 main:app



## 🔐 Security Features

- 🔑 Bcrypt Password Hashing
- 🛡️ CSRF Protection (via Flask-WTF or manual tokens)
- 🔐 Secure Session Management
- 🧼 Input Validation (forms & back-end sanitization)
- 🧍‍♂️🧍‍♀️ Role-Based Access (User / Admin)

---

## 🔄 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/` | Homepage |
| `GET`  | `/matches` | List all available matches |
| `POST` | `/register` | User registration |
| `POST` | `/login` | User login |
| `GET`  | `/seats/<match_id>` | View available seats |
| `POST` | `/book_seats` | Book selected seats |
| `GET`  | `/tickets` | View all your bookings |
| `GET`  | `/download_ticket/<booking_id>` | Download ticket as PDF |
| `GET`  | `/dashboard` | Admin dashboard |
| `GET`  | `/admin/stadiums` | Manage stadiums |
| `GET`  | `/admin/matches` | Manage matches |

---

## 🔮 Future Roadmap

- 💳 Stripe/PayPal Payment Gateway Integration
- 📧 Email Confirmations and OTP-based login
- 📱 React Native Mobile App Support
- 🟢 Real-Time Seat Availability via WebSocket
- 🌍 Internationalization (i18n) & Localization
- 🔁 Ticket Transfer / Resell System

---

## 👨‍💻 Authors

This project was developed by:

- **Subuhana B**
- **Sageetha G S**
- **Swetha S**
- **Saniyha Sunil**

🎉 _Contributions are always welcome!_

---

## 🤝 How to Contribute

1. **Fork** the repository
2. **Create a branch**  
   git checkout -b feature/your-feature
## 📝 License
This project is licensed under the MIT License.
See the LICENSE file for more information.
**⭐ Show Your Support**
_If you found this project helpful or inspiring, please give it a ⭐ on GitHub!_




