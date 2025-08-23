# 🏏 CricketTix - Premium Cricket Ticketing Platform

CricketTix is a next-generation cricket ticketing platform that revolutionizes how fans experience cricket matches. Built with cutting-edge technology, it combines traditional ticketing with modern features like live scores, loyalty rewards, weather forecasts, smart seat recommendations, and premium experiences.

---

## 🚀 Features

- 👤 User registration and login (with admin support)
- 🎟️ Book match tickets by selecting available seats
- 🏟️ Stadium management with amenities and capacity
- 🏏 Match creation with details like teams, type, date, and stadium
- 📊 Admin dashboard (create stadiums, matches, view bookings)
- 📅 Upcoming match listing
- ✅ Secure login with Flask-Login
- 🔒 Passwords for users
- 💬 Match reviews and stadium ratings
- 📥 Notifications system
- 📈 Price history tracking

---

## 🏗️ Technical Stack

| Layer     | Technology                       |
|-----------|----------------------------------|
| **Backend** | Python, SQL, SQLite |
| **Frontend** | HTML, CSS, JavaScript |

---
## 🚀 Live Demo

🌐 **Live video**: [click here to watch](https://your-demo-url.com)

## 🖼️ Screenshots outputs are:
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
CricketTix/
│
├── app.py                  # Main Flask app
├── app_local.py            # Local configuration for SQLite
├── run_local.py            # Script to initialize local database & start server
├── extension.py            # Initialize database and login manager
├── models.py               # Database models (User, Match, Stadium, etc.)
├── routes.py               # Route handlers for user/admin actions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── static/                 # Static files
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── matches.html
│   ├── booking.html
│   ├── dashboard.html
│   └── ...
│
├── sql/                    # SQL scripts for DB setup and seeding
│   └── seed.sql
│
└── instance/               # Database files
    └── cricketTix_local.db # SQLite database for local testing

```

---


## ⚙️ Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL
- Git (optional)

### Steps

```bash
# Clone the repo
git clone https://github.com/yourusername/CricketTix.git
cd CricketTix

# Install dependencies
pip install -r requirements.txt



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
   ```bash
   git checkout -b feature/your-feature
## 📝 License
This project is licensed under the MIT License.
See the LICENSE file for more information.
---
## ⭐ Show Your Support
If you found this project helpful or inspiring, please give it a ⭐ on GitHub!

 - Let others discover and contribute too!🤝



