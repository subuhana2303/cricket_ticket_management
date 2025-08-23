-- seed.sql
-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    is_admin BOOLEAN DEFAULT 0,
    loyalty_points INTEGER DEFAULT 0,
    membership_tier TEXT DEFAULT 'Bronze',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Stadiums table
CREATE TABLE stadiums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT DEFAULT 'India',
    capacity INTEGER NOT NULL
);

-- Matches table
CREATE TABLE matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team1 TEXT NOT NULL,
    team2 TEXT NOT NULL,
    stadium_id INTEGER NOT NULL,
    match_date DATETIME NOT NULL,
    match_type TEXT DEFAULT 'ODI',
    ticket_price REAL NOT NULL,
    FOREIGN KEY (stadium_id) REFERENCES stadiums(id)
);

-- Sample admin
INSERT INTO users (name, email, password_hash, is_admin, loyalty_points, membership_tier)
VALUES ('Admin User', 'admin@cricket.com', 'hashed_password_here', 1, 1000, 'Platinum');
