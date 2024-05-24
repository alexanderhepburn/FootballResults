from analyse.pdf_creator import create_pdf
from analyse.plot import Plot as p
from .data_manager import get_data_with_columns, get_all_data
from .text_generator import GenerateText
from misc import *


def analyse(team1: str, team2: str) -> str:
    """
    Analyzes the performance data of two teams and generates a PDF report.

    Args:
        team1 (str): Name of the first team.
        team2 (str): Name of the second team.

    Returns:
        str: File name of the generated PDF.
    """
    # Retrieve data for the specified teams with the necessary columns
    team_data = get_data_with_columns([team1, team2])

    information = GenerateText(get_all_data(), team1, team2)

    # Plot the performance data for the specified metrics
    p(team_data, team1, team2, [
        'Full Time Goals',
        'Shots on Target',
        'Fouls Committed',
        'Corners',
        'Yellow Cards',
        'Red Cards'
    ], information.team1_wins, information.team1_losses, information.draws, information.correlation_matrix)
    # Generate the PDF report
    pdf_name = create_pdf(team1, team2, information.get_text())
    # Return the file name of the generated PDF
    return pdf_name
