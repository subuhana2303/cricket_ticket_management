-- Insert a sample user
INSERT INTO users (name, email, password_hash, is_admin)
VALUES ('Admin User', 'admin@cricket.com', 'hashed_password_here', TRUE);

-- Insert a stadium
INSERT INTO stadiums (name, city, country, capacity, rows, seats_per_row)
VALUES ('Eden Gardens', 'Kolkata', 'India', 66000, 35, 55);

-- Insert a match
INSERT INTO matches (team1, team2, stadium_id, match_date, match_type, ticket_price)
VALUES ('India', 'Pakistan', 1, '2025-08-30 18:00:00', 'T20', 85.00);

-- Booking example
INSERT INTO bookings (user_id, match_id, seat_row, seat_number, total_amount)
VALUES (1, 1, 5, 12, 85.00);

-- Select all upcoming matches
SELECT * FROM matches WHERE status='Upcoming';

-- Update seat booking status
UPDATE bookings SET payment_status='completed' WHERE id=1;

-- Delete a notification
DELETE FROM notifications WHERE id=5;
