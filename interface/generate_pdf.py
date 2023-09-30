from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate,Table, TableStyle, PageBreak, Paragraph
from interface.DatabaseConnection import DatabaseConnection

def generate_report(teacher):
    # Create a PDF file
    pdf_file = "Report.pdf"
    document = SimpleDocTemplate(pdf_file, pagesize=letter)

    db = DatabaseConnection()
    reportData = db.getReportData(teacher)

    story = []
    for key,value in reportData.items():    
        story.append(Paragraph("Course ID : "+str(key[0])+"\nCourse Name : "+key[1]))
        table = Table(value)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)),  # Gray background for the header row
            ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),  # White text for the header row
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center-align all cells
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for the header row
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding for the header row
            ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),  # Light gray background for data rows
            ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Add gridlines
        ])
        table.setStyle(style)
        story.append(table)
        story.append(PageBreak())

    story = story[:-1]

    document.build(story)