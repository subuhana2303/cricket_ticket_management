from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO
from datetime import datetime

def generate_ticket_pdf(booking):
    """Generate a PDF ticket for a booking"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=1*inch)
    
    # Get styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.darkblue,
        alignment=1  # Center alignment
    )
    
    content = []
    
    # Title
    content.append(Paragraph("🏏 CRICKET TICKET", title_style))
    content.append(Spacer(1, 20))
    
    # Match details
    match_info = [
        ['Match:', f"{booking.match.team1} vs {booking.match.team2}"],
        ['Stadium:', f"{booking.match.stadium.name}, {booking.match.stadium.city}"],
        ['Date & Time:', booking.match.match_date.strftime('%B %d, %Y at %I:%M %p')],
        ['Seat:', f"Row {booking.seat_row}, Seat {booking.seat_number}"],
        ['Price:', f"${booking.total_amount:.2f}"],
        ['Booking ID:', f"#{booking.id}"],
        ['Booked By:', booking.user.name],
        ['Booking Date:', booking.booking_date.strftime('%B %d, %Y')]
    ]
    
    table = Table(match_info, colWidths=[2*inch, 4*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (1, 0), (1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    content.append(table)
    content.append(Spacer(1, 30))
    
    # Instructions
    instructions = """
    <b>Important Instructions:</b><br/>
    • Please arrive at the stadium at least 30 minutes before the match<br/>
    • Carry a valid ID proof along with this ticket<br/>
    • Outside food and beverages are not allowed<br/>
    • Ticket is non-transferable and non-refundable<br/>
    • Lost tickets will not be replaced<br/><br/>
    
    <b>Enjoy the match! 🏏</b>
    """
    
    content.append(Paragraph(instructions, styles['Normal']))
    
    # Build PDF
    doc.build(content)
    buffer.seek(0)
    
    return buffer
