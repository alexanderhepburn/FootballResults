import pandas as pd
import os
import json
from settings_manager import settings_manager
from fpdf import FPDF as fpdf
import matplotlib.pyplot as plt
from io import BytesIO

class data_manager:
    @staticmethod
    def get_data_as_df(year: int):
        df = pd.read_csv(f"data/{year-1}{year}.csv")
        return df

    @staticmethod
    def get_all_data():
        current_league = settings_manager().user_league
        directory = os.fsencode(f"data/{current_league}")

        list_of_df = []

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if not filename.endswith(".csv"):
                print("ERROR Filename CSV")
                continue
            try:
                df = pd.read_csv(f"data/{current_league}/{filename}")
            except Exception as e:
                print(f"Error with file {filename}: {e}")
            list_of_df.append(df)
        combined_df = pd.concat(list_of_df)

        def custom_date_parser(date_str):
            try:
                # Try parsing date with four-digit year
                return pd.to_datetime(date_str, format='%d/%m/%Y')
            except ValueError:
                # If parsing fails, try parsing with two-digit year
                return pd.to_datetime(date_str, format='%d/%m/%y')

        combined_df['Date'] = combined_df['Date'].apply(custom_date_parser)
        return combined_df

    @staticmethod
    def get_all_teams():
        try:
            df = data_manager.get_all_data()
            unique_values_list = list(set(df['HomeTeam'].unique()).union(df['AwayTeam'].unique()))
            unique_values_list = list(filter(lambda x: not pd.isna(x), unique_values_list))

            return unique_values_list
        except Exception as e:
            print(f"Teams Error: {e}")

    def analyse_data(self, team1, team2):
        pdf = fpdf('P', 'mm', 'A4') # A4 (210 by 297 mm)

        PHEIGHT = 297
        PWIDTH = 210

        pdf.add_page()
        pdf.set_margins(7, 0, 7)

        pdf.set_font('Arial', 'B', 14)

        df = data_manager.get_all_data()
        total_games_home = df.groupby([df['Date'].dt.year, 'HomeTeam']).size().reset_index(name='Count')
        team1_home = total_games_home[total_games_home['HomeTeam'] == team1]
        team2_home = total_games_home[total_games_home['HomeTeam'] == team2]

        total_games_away = df.groupby([df['Date'].dt.year, 'AwayTeam']).size().reset_index(name='Count')
        team1_away = total_games_away[total_games_away['AwayTeam'] == team1]
        team2_away = total_games_away[total_games_away['AwayTeam'] == team2]

        self.create_bar(team1_home['Count'], team2_home['Count'], team1_home['Date'],
                        team2_home['Date'], team1, team2, 1)
        self.create_bar(team1_away['Count'], team2_away['Count'], team1_away['Date'],
                        team2_away['Date'], team1, team2, 2)

        team1_home_df = df[df['HomeTeam'] == team1]
        team2_home_df = df[df['HomeTeam'] == team2]
        # Group by year and aggregate points using sum
        team1_home_by_year = team1_home_df.groupby(team1_home_df['Date'].dt.year)['FTHG'].sum()
        team2_home_by_year = team2_home_df.groupby(team2_home_df['Date'].dt.year)['FTHG'].sum()
        self.create_bar(team1_home_by_year.values, team2_home_by_year.values, team1_home_by_year.index, team2_home_by_year.index, team1, team2, 3)

        team1_home_df = df[df['AwayTeam'] == team1]
        team2_home_df = df[df['AwayTeam'] == team2]
        # Group by year and aggregate points using sum
        team1_home_by_year = team1_home_df.groupby(team1_home_df['Date'].dt.year)['FTAG'].sum()
        team2_home_by_year = team2_home_df.groupby(team2_home_df['Date'].dt.year)['FTAG'].sum()
        self.create_bar(team1_home_by_year.values, team2_home_by_year.values, team1_home_by_year.index, team2_home_by_year.index, team1, team2, 4)
        self.create_bar(team1_home_by_year.values, team2_home_by_year.values, team1_home_by_year.index, team2_home_by_year.index, team1, team2, 5)
        self.create_bar(team1_home_by_year.values, team2_home_by_year.values, team1_home_by_year.index, team2_home_by_year.index, team1, team2, 6)
        self.create_bar(team1_home_by_year.values, team2_home_by_year.values, team1_home_by_year.index, team2_home_by_year.index, team1, team2, 7)
        self.create_bar(team1_home_by_year.values, team2_home_by_year.values, team1_home_by_year.index, team2_home_by_year.index, team1, team2, 8)


        top_margin = 50
        height = 57

        pdf.cell(w=40, h=10, txt=f"{team1} vs {team2} Report", border=0, ln=1, align='', fill=False, link='')
        pdf.set_font('Arial', '', 10)
        pdf.multi_cell(w=210, h=10, txt=f"Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.  Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer",
                 border=0, align='', fill=False)

        for i in range(1, 9):
            pdf.image(f'tmp/plot{i}.png', x=(0 if i % 2 != 0 else 1)*96+7, y=top_margin+((i-1)//2)*height, w=100)

        # pdf.image('tmp/plot1.png', x=7, y=top_margin, w=100)
        # pdf.image('tmp/plot2.png', x=103, y=top_margin, w=100)
        #
        # pdf.image('tmp/plot3.png', x=7, y=top_margin+height, w=100)
        # pdf.image('tmp/plot4.png', x=103, y=top_margin+height, w=100)
        #
        # pdf.image('tmp/plot.png', x=7, y=top_margin+height*2, w=100)
        # pdf.image('tmp/plot1.png', x=103, y=top_margin+height*2, w=100)
        #
        # pdf.image('tmp/plot.png', x=7, y=top_margin+height*3, w=100)
        # pdf.image('tmp/plot1.png', x=103, y=top_margin+height*3, w=100)
        file_name = f'exports/{team1}_vs_{team2}.pdf'
        pdf.output(file_name, 'F')
        return file_name

    def create_bar(self, x1: list, x2: list, y1: list, y2: list, x1_name: str, x2_name: str, plot_number: int):
        plt.figure(figsize=(10, 6))
        # Width of a bar
        width = 0.4

        plt.bar(y1 - (width / 2), x1, width=width, color='skyblue',
                label=x1_name)
        plt.bar(y2 + (width / 2), x2, width=width, color='purple',
                label=x2_name)
        plt.legend(loc="best")
        plt.title(f'Away Goals per Year')
        plt.xticks(y1)
        plt.grid(axis='y', alpha=0.7)

        plt.savefig(f'tmp/plot{plot_number}.png')

