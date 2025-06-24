from flask import render_template, request, redirect, url_for, flash, session, jsonify, make_response
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User, Stadium, Match, Booking
from utils import generate_ticket_pdf
from datetime import datetime
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered. Please use a different email.', 'error')
            return render_template('register.html')
        
        # Create new user
        user = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(password),
            is_admin=False
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            next_page = request.args.get('next')
            if user.is_admin:
                return redirect(next_page) if next_page else redirect(url_for('dashboard'))
            return redirect(next_page) if next_page else redirect(url_for('matches'))
        else:
            flash('Invalid email or password.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/matches')
def matches():
    matches = Match.query.join(Stadium).filter(Match.match_date > datetime.utcnow()).all()
    return render_template('matches.html', matches=matches)

@app.route('/seats/<int:match_id>')
@login_required
def seats(match_id):
    match = Match.query.get_or_404(match_id)
    stadium = match.stadium
    
    # Get booked seats
    bookings = Booking.query.filter_by(match_id=match_id).all()
    booked_seats = [[booking.seat_row, booking.seat_number] for booking in bookings]
    
    return render_template('seats.html', match=match, stadium=stadium, booked_seats=booked_seats)

@app.route('/book_seats', methods=['POST'])
@login_required
def book_seats():
    data = request.get_json()
    match_id = data.get('match_id')
    selected_seats = data.get('seats', [])
    
    if not selected_seats:
        return jsonify({'success': False, 'message': 'No seats selected'})
    
    match = Match.query.get_or_404(match_id)
    
    # Check if any selected seats are already booked
    for seat in selected_seats:
        existing_booking = Booking.query.filter_by(
            match_id=match_id,
            seat_row=seat['row'],
            seat_number=seat['seat']
        ).first()
        if existing_booking:
            return jsonify({
                'success': False, 
                'message': f'Seat {seat["row"]}-{seat["seat"]} is already booked'
            })
    
    # Store booking details in session for payment
    session['booking_details'] = {
        'match_id': match_id,
        'seats': selected_seats,
        'total_amount': len(selected_seats) * match.ticket_price
    }
    
    return jsonify({'success': True, 'redirect': url_for('payment')})

@app.route('/payment')
@login_required
def payment():
    booking_details = session.get('booking_details')
    if not booking_details:
        flash('No booking details found. Please select seats first.', 'error')
        return redirect(url_for('matches'))
    
    match = Match.query.get(booking_details['match_id'])
    return render_template('payment.html', booking_details=booking_details, match=match)

@app.route('/process_payment', methods=['POST'])
@login_required
def process_payment():
    booking_details = session.get('booking_details')
    if not booking_details:
        flash('No booking details found.', 'error')
        return redirect(url_for('matches'))
    
    # Simulate payment processing
    match_id = booking_details['match_id']
    seats = booking_details['seats']
    total_amount = booking_details['total_amount']
    
    # Create bookings
    bookings = []
    for seat in seats:
        booking = Booking(
            user_id=current_user.id,
            match_id=match_id,
            seat_row=seat['row'],
            seat_number=seat['seat'],
            total_amount=total_amount / len(seats),
            payment_status='completed'
        )
        db.session.add(booking)
        bookings.append(booking)
    
    db.session.commit()
    
    # Clear session
    session.pop('booking_details', None)
    
    flash(f'Payment successful! {len(seats)} tickets booked.', 'success')
    return redirect(url_for('tickets'))

@app.route('/tickets')
@login_required
def tickets():
    bookings = Booking.query.filter_by(user_id=current_user.id).join(Match).join(Stadium).all()
    return render_template('tickets.html', bookings=bookings)

@app.route('/download_ticket/<int:booking_id>')
@login_required
def download_ticket(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    
    # Ensure user owns this booking
    if booking.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('tickets'))
    
    pdf_buffer = generate_ticket_pdf(booking)
    
    response = make_response(pdf_buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=ticket_{booking.id}.pdf'
    
    return response

# Admin routes
@app.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('matches'))
    
    # Statistics
    total_users = User.query.count()
    total_matches = Match.query.count()
    total_bookings = Booking.query.count()
    total_revenue = db.session.query(db.func.sum(Booking.total_amount)).scalar() or 0
    
    # Recent bookings
    recent_bookings = Booking.query.join(Match).join(User).order_by(Booking.booking_date.desc()).limit(10).all()
    
    # Booking statistics for chart
    booking_stats = db.session.query(
        Match.team1,
        Match.team2,
        db.func.count(Booking.id).label('booking_count')
    ).join(Booking).group_by(Match.id).all()
    
    return render_template('dashboard.html', 
                         total_users=total_users,
                         total_matches=total_matches,
                         total_bookings=total_bookings,
                         total_revenue=total_revenue,
                         recent_bookings=recent_bookings,
                         booking_stats=booking_stats)

@app.route('/admin/stadiums')
@login_required
def admin_stadiums():
    if not current_user.is_admin:
        flash('Access denied.', 'error')
        return redirect(url_for('matches'))
    
    stadiums = Stadium.query.all()
    return render_template('admin/stadiums.html', stadiums=stadiums)

@app.route('/admin/stadiums/add', methods=['POST'])
@login_required
def add_stadium():
    if not current_user.is_admin:
        return jsonify({'success': False, 'message': 'Access denied'})
    
    name = request.form['name']
    city = request.form['city']
    capacity = int(request.form['capacity'])
    rows = int(request.form['rows'])
    seats_per_row = int(request.form['seats_per_row'])
    
    stadium = Stadium(
        name=name,
        city=city,
        capacity=capacity,
        rows=rows,
        seats_per_row=seats_per_row
    )
    
    db.session.add(stadium)
    db.session.commit()
    
    flash('Stadium added successfully!', 'success')
    return redirect(url_for('admin_stadiums'))

@app.route('/admin/matches')
@login_required
def admin_matches():
    if not current_user.is_admin:
        flash('Access denied.', 'error')
        return redirect(url_for('matches'))
    
    matches = Match.query.join(Stadium).all()
    stadiums = Stadium.query.all()
    return render_template('admin/manage_matches.html', matches=matches, stadiums=stadiums)

@app.route('/admin/matches/add', methods=['POST'])
@login_required
def add_match():
    if not current_user.is_admin:
        return jsonify({'success': False, 'message': 'Access denied'})
    
    team1 = request.form['team1']
    team2 = request.form['team2']
    stadium_id = int(request.form['stadium_id'])
    match_date = datetime.strptime(request.form['match_date'], '%Y-%m-%dT%H:%M')
    ticket_price = float(request.form['ticket_price'])
    
    match = Match(
        team1=team1,
        team2=team2,
        stadium_id=stadium_id,
        match_date=match_date,
        ticket_price=ticket_price
    )
    
    db.session.add(match)
    db.session.commit()
    
    flash('Match added successfully!', 'success')
    return redirect(url_for('admin_matches'))
