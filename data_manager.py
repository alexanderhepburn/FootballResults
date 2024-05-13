import pandas as pd
import os
import json
from settings_manager import settings_manager
from fpdf import FPDF

class data_manager:
    @staticmethod
    def get_data_as_df(year):
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
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_margins(0, 0, 0)

        pdf.set_font('Arial', 'B', 14)
        pdf.cell(w=40, h=10, txt=f"{team1} vs {team2}", border=0, ln=1, align='', fill=False, link='')

        file_name = f'exports/{team1}_vs_{team2}.pdf'
        pdf.output(file_name, 'F')
        return file_name

