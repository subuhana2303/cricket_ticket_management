-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    phone VARCHAR(20),
    favorite_teams TEXT,
    loyalty_points INTEGER DEFAULT 0,
    membership_tier VARCHAR(20) DEFAULT 'Bronze',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Stadiums table
CREATE TABLE stadiums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) DEFAULT 'India',
    capacity INTEGER NOT NULL,
    rows INTEGER NOT NULL,
    seats_per_row INTEGER NOT NULL,
    amenities TEXT,
    weather_info TEXT,
    pitch_type VARCHAR(50) DEFAULT 'Batting',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Matches table
CREATE TABLE matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team1 VARCHAR(100) NOT NULL,
    team2 VARCHAR(100) NOT NULL,
    stadium_id INTEGER NOT NULL,
    match_date DATETIME NOT NULL,
    match_type VARCHAR(20) DEFAULT 'ODI',
    tournament VARCHAR(100),
    ticket_price FLOAT NOT NULL,
    vip_price FLOAT,
    premium_price FLOAT,
    status VARCHAR(20) DEFAULT 'Upcoming',
    weather_forecast VARCHAR(100),
    live_score TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (stadium_id) REFERENCES stadiums(id) ON DELETE CASCADE
);

-- Bookings table
CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    match_id INTEGER NOT NULL,
    seat_row INTEGER NOT NULL,
    seat_number INTEGER NOT NULL,
    seat_category VARCHAR(20) DEFAULT 'Regular',
    total_amount FLOAT NOT NULL,
    discount_applied FLOAT DEFAULT 0,
    loyalty_points_earned INTEGER DEFAULT 0,
    booking_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_status VARCHAR(20) DEFAULT 'completed',
    qr_code VARCHAR(255),
    check_in_time DATETIME,
    UNIQUE(match_id, seat_row, seat_number),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE CASCADE
);

-- Match Reviews table
CREATE TABLE match_reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    match_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    review_text TEXT,
    stadium_rating INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE CASCADE
);

-- Seat Categories table
CREATE TABLE seat_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    benefits TEXT,
    color_code VARCHAR(7) DEFAULT '#28a745'
);

-- Price History table
CREATE TABLE price_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    seat_category VARCHAR(20) NOT NULL,
    price FLOAT NOT NULL,
    date_changed DATETIME DEFAULT CURRENT_TIMESTAMP,
    reason VARCHAR(100),
    FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE CASCADE
);

-- Notifications table
CREATE TABLE notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    message TEXT NOT NULL,
    notification_type VARCHAR(50) DEFAULT 'info',
    is_read BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
