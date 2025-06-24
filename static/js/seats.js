// Seat Selection JavaScript for Cricket Ticket System

class SeatSelection {
    constructor(options) {
        this.matchId = options.matchId;
        this.rows = options.rows;
        this.seatsPerRow = options.seatsPerRow;
        this.ticketPrice = options.ticketPrice;
        this.bookedSeats = new Set(options.bookedSeats.map(seat => `${seat[0]}-${seat[1]}`));
        this.selectedSeats = new Set();
        
        this.init();
    }
    
    init() {
        this.generateSeatsGrid();
        this.bindEvents();
    }
    
    generateSeatsGrid() {
        const grid = document.getElementById('seats-grid');
        if (!grid) return;
        
        grid.innerHTML = '';
        
        for (let row = 1; row <= this.rows; row++) {
            const rowElement = document.createElement('div');
            rowElement.className = 'seat-row';
            
            // Row label
            const rowLabel = document.createElement('div');
            rowLabel.className = 'row-label';
            rowLabel.textContent = row;
            rowElement.appendChild(rowLabel);
            
            // Seats container
            const seatsContainer = document.createElement('div');
            seatsContainer.className = 'seats-in-row';
            
            for (let seat = 1; seat <= this.seatsPerRow; seat++) {
                const seatKey = `${row}-${seat}`;
                const seatElement = document.createElement('div');
                seatElement.className = 'seat';
                seatElement.dataset.row = row;
                seatElement.dataset.seat = seat;
                seatElement.textContent = seat;
                
                // Set seat status
                if (this.bookedSeats.has(seatKey)) {
                    seatElement.classList.add('booked');
                    seatElement.title = 'Seat already booked';
                } else {
                    seatElement.classList.add('available');
                    seatElement.title = `Row ${row}, Seat ${seat} - $${this.ticketPrice.toFixed(2)}`;
                }
                
                seatsContainer.appendChild(seatElement);
            }
            
            rowElement.appendChild(seatsContainer);
            grid.appendChild(rowElement);
        }
    }
    
    bindEvents() {
        const grid = document.getElementById('seats-grid');
        if (!grid) return;
        
        grid.addEventListener('click', (e) => {
            if (e.target.classList.contains('seat') && e.target.classList.contains('available')) {
                this.toggleSeat(e.target);
            }
        });
        
        const proceedBtn = document.getElementById('proceed-btn');
        if (proceedBtn) {
            proceedBtn.addEventListener('click', () => {
                this.proceedToPayment();
            });
        }
    }
    
    toggleSeat(seatElement) {
        const row = parseInt(seatElement.dataset.row);
        const seat = parseInt(seatElement.dataset.seat);
        const seatKey = `${row}-${seat}`;
        
        if (seatElement.classList.contains('selected')) {
            // Deselect seat
            seatElement.classList.remove('selected');
            this.selectedSeats.delete(seatKey);
        } else {
            // Select seat (limit to 6 seats per booking)
            if (this.selectedSeats.size >= 6) {
                showError('Maximum of 6 seats can be selected per booking.');
                return;
            }
            
            seatElement.classList.add('selected');
            this.selectedSeats.add(seatKey);
        }
        
        this.updateSummary();
    }
    
    updateSummary() {
        const selectedSeatsContainer = document.getElementById('selected-seats');
        const seatCountElement = document.getElementById('seat-count');
        const totalAmountElement = document.getElementById('total-amount');
        const proceedBtn = document.getElementById('proceed-btn');
        
        if (this.selectedSeats.size === 0) {
            selectedSeatsContainer.innerHTML = `
                <div class="text-center text-muted py-3">
                    <i class="fas fa-mouse-pointer fa-2x mb-2"></i>
                    <p>Click on seats to select them</p>
                </div>
            `;
            proceedBtn.disabled = true;
        } else {
            const seatsList = Array.from(this.selectedSeats).map(seatKey => {
                const [row, seat] = seatKey.split('-');
                return `
                    <div class="d-flex justify-content-between align-items-center mb-1">
                        <span>Row ${row}, Seat ${seat}</span>
                        <span class="text-success">$${this.ticketPrice.toFixed(2)}</span>
                    </div>
                `;
            }).join('');
            
            selectedSeatsContainer.innerHTML = `
                <h6 class="mb-2">Selected Seats:</h6>
                ${seatsList}
            `;
            proceedBtn.disabled = false;
        }
        
        seatCountElement.textContent = this.selectedSeats.size;
        totalAmountElement.textContent = `$${(this.selectedSeats.size * this.ticketPrice).toFixed(2)}`;
    }
    
    proceedToPayment() {
        if (this.selectedSeats.size === 0) {
            showError('Please select at least one seat.');
            return;
        }
        
        const selectedSeatsArray = Array.from(this.selectedSeats).map(seatKey => {
            const [row, seat] = seatKey.split('-');
            return { row: parseInt(row), seat: parseInt(seat) };
        });
        
        const data = {
            match_id: this.matchId,
            seats: selectedSeatsArray
        };
        
        fetch('/book_seats', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect;
            } else {
                showError(data.message || 'Failed to book seats. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showError('An error occurred. Please try again.');
        });
    }
}

// Utility function to show error messages
function showError(message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-danger alert-dismissible fade show';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alertDiv);
            bsAlert.close();
        }, 5000);
    }
}
