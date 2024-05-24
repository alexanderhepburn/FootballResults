from fpdf import FPDF as fpdf

from settings import *


def create_pdf(team1: str, team2: str, text: str) -> str:
    """
    Creates a PDF report with performance data and plots for two teams.

    Args:
        team1 (str): Name of the first team.
        team2 (str): Name of the second team.
        text (str): Text content for the PDF report.

    Returns:
        str: File name of the generated PDF.
    """
    # Create a new PDF instance
    pdf = fpdf('P', 'mm', 'A4')  # A4 (210 by 297 mm)

    # Constants for page dimensions and margins
    PWIDTH = 210
    MARGIN_SIDE = 7

    # Add a new page and set margins
    pdf.add_page()
    pdf.set_margins(MARGIN_SIDE, 0, MARGIN_SIDE)

    # Set font for title
    pdf.set_font('Arial', 'B', 13)

    # Add title to the PDF
    pdf.set_x(pdf.l_margin)
    pdf.cell(w=40, h=10,
             txt=f"{team1} vs {team2} Performance Report ({SettingsManager.user_settings.starting_year}-{SettingsManager.user_settings.ending_year})",
             border=0, ln=1, align='', fill=False, link='')

    # Set font for content
    pdf.set_font('Arial', '', 10)

    # Add text content to the PDF
    pdf.multi_cell(w=PWIDTH - 2 * MARGIN_SIDE, h=5,
                   txt=text,
                   border=0, align='J', fill=False)

    # Set initial positions for images
    TOPMARGIN = 52
    HEIGHT = 61

    # Add plots to the PDF
    for i in range(1, 9):
        try:
            # Attempt to add image to the PDF
            pdf.image(f'tmp/plot{i}.png', x=(0 if i % 2 != 0 else 1) * 96 + 7,
                      y=TOPMARGIN + ((i - 1) // 2) * HEIGHT, w=100)
        except Exception as e:
            print(f"Error with image generation: {e}")

    # Define the file name for the PDF
    file_name = f'exports/{team1.replace(" ", "")}_vs_{team2.replace(" ", "")}.pdf'

    # Output the PDF to a file
    pdf.output(file_name, 'F')

    # Return the file name of the generated PDF
    return file_name
