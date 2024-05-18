from fpdf import FPDF as fpdf

from settings.settings_manager import SettingsManager


class PdfCreator:
    def create(self, team1: str, team2: str) -> str:
        pdf = fpdf('P', 'mm', 'A4')  # A4 (210 by 297 mm)

        PHEIGHT = 297
        PWIDTH = 210
        margin_side = 7

        pdf.add_page()
        pdf.set_margins(margin_side, 0, margin_side)

        pdf.set_font('Arial', 'B', 14)

        title_x = pdf.l_margin
        # Set the position
        pdf.set_x(title_x)

        pdf.cell(w=40, h=10,
                 txt=f"{team1} vs {team2} Performance Report ({SettingsManager.user_settings.starting_year}-{SettingsManager.user_settings.ending_year})",
                 border=0, ln=1, align='', fill=False, link='')
        pdf.set_font('Arial', '', 10)
        pdf.multi_cell(w=PWIDTH - 2 * margin_side, h=5,
                       txt=f"Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.",
                       border=0, align='J', fill=False)

        top_margin = 60
        height = 57

        for i in range(1, 9):
            try:
                pdf.image(f'tmp/plot{i}.png', x=(0 if i % 2 != 0 else 1) * 96 + 7,
                          y=top_margin + ((i - 1) // 2) * height, w=100)
            except Exception as e:
                print(f"Error with image generation: {e}")

        file_name = f'exports/{team1}_vs_{team2}.pdf'
        pdf.output(file_name, 'F')
        return file_name
