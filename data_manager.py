import pandas as pd
import os
import json
from settings_manager import settings_manager
from fpdf import FPDF as fpdf
import matplotlib.pyplot as plt
from io import BytesIO

class data_manager:
    @staticmethod
    def get_data_as_df(year):
        """
        test_function does blah blah blah.

        :param p1: describe about parameter p1
        :param p2: describe about parameter p2
        :param p3: describe about parameter p3
        :return: describe what it returns
        """
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

    @staticmethod
    def analyse_data(team1, team2):
        pdf = fpdf('P', 'mm', 'A4')
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

        # Zwei plots mit den daten

        plt.figure(figsize=(10, 6))
        # Width of a bar
        width = 0.4

        plt.bar(team1_home['Date']-(width/2), team1_home['Count'], width=width,color='skyblue', label=team1)
        plt.bar(team2_home['Date']+(width/2), team2_home['Count'], width=width,color='purple', label=team2)
        plt.legend(loc="best")
        plt.title(f'Home Matches per Year')
        plt.xticks(team1_home['Date'])
        plt.grid(axis='y', alpha=0.7)

        plt.savefig('plot.png')

        plt.figure(figsize=(10, 6))
        # Width of a bar
        width = 0.4

        plt.bar(team1_away['Date'] - (width / 2), team1_away['Count'], width=width, color='skyblue', label=team1)
        plt.bar(team2_away['Date'] + (width / 2), team2_away['Count'], width=width, color='purple', label=team2)
        plt.legend(loc="best")
        plt.title(f'Away Matches per Year')
        plt.xticks(team1_away['Date'])
        plt.grid(axis='y', alpha=0.7)

        plt.savefig('plot1.png')

        top_margin = 50
        height = 57

        pdf.cell(w=40, h=10, txt=f"{team1} vs {team2} Report", border=0, ln=1, align='', fill=False, link='')
        pdf.set_font('Arial', '', 10)
        pdf.multi_cell(w=210, h=10, txt=f"Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.  Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer",
                 border=0, align='', fill=False)

        pdf.image('plot.png', x=7, y=top_margin, w=100)
        pdf.image('plot1.png', x=103, y=top_margin, w=100)

        pdf.image('plot.png', x=7, y=top_margin+height, w=100)
        pdf.image('plot1.png', x=103, y=top_margin+height, w=100)

        pdf.image('plot.png', x=7, y=top_margin+height*2, w=100)
        pdf.image('plot1.png', x=103, y=top_margin+height*2, w=100)

        pdf.image('plot.png', x=7, y=top_margin+height*3, w=100)
        pdf.image('plot1.png', x=103, y=top_margin+height*3, w=100)
        file_name = f'exports/{team1}_vs_{team2}.pdf'
        pdf.output(file_name, 'F')
        return file_name

