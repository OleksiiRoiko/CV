import pdfkit

# Path to your HTML file
html_file = 'index.html'

# Path to save the PDF
output_pdf = 'Oleksii_Roiko_CV.pdf'

# Convert HTML file to PDF
pdfkit.from_file(html_file, output_pdf)
