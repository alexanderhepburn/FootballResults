import os

import pandas as pd

from settings.settings_manager import SettingsManager


class DataManager:
    @staticmethod
    def get_data_as_df(year: int):
        df = pd.read_csv(f"data/{year - 1}{year}.csv")
        return df

    @staticmethod
    def get_all_data():
        directory = os.fsencode(f"data/{SettingsManager.user_settings.league.name}")

        list_of_df = []

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if not filename.endswith(".csv"):
                print("ERROR Filename CSV")
                continue
            try:
                df = pd.read_csv(f"data/{SettingsManager.user_settings.league.name}/{filename}")
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

        filtered_df = combined_df[
            (combined_df['Date'].dt.year >= SettingsManager.user_settings.starting_year) & (
                    combined_df['Date'].dt.year <= SettingsManager.user_settings.ending_year)]

        return filtered_df

    @staticmethod
    def get_all_teams():
        try:
            df = DataManager.get_all_data()
            unique_values_list = list(set(df['HomeTeam'].unique()).union(df['AwayTeam'].unique()))
            unique_values_list = list(filter(lambda x: not pd.isna(x), unique_values_list))

            return unique_values_list
        except Exception as e:
            print(f"Teams Error: {e}")

    @staticmethod
    def get_data_with_columns(teams: [str]) -> pd.DataFrame:
        try:
            df = DataManager.get_all_data()
            data_to_keep: dict[str: list[str]] = {"HomeTeam": ['FTHG', 'HTHG', 'HST', 'HS', 'HF', 'HC'],
                                                  "AwayTeam": ['FTAG', 'HTAG', 'AST', 'AS', 'AF', 'AC']}

            new_names = ['Full Time Team Goals', 'Half Time Team Goals', 'Team Shots on Target', 'Team Shots',
                         'Team Fouls Committed',
                         'Team Corners']

            team_dfs: list[pd.DataFrame] = []
            for team in teams:
                list_of_dfs: list[pd.DataFrame] = []
                for team_type, columns in data_to_keep.items():
                    columns_to_keep = {element: "sum" for element in columns}
                    new_df = df[df[team_type] == team]
                    new_df = new_df.loc[:, columns + ['Date', team_type]]
                    new_df = new_df.rename(columns={team_type: 'Team'})
                    new_df = new_df.groupby([new_df['Date'].dt.year, "Team"]).agg(columns_to_keep)
                    list_of_dfs.append(new_df)

                combined_data = {}
                for home_column, away_column, new_name in zip(data_to_keep["HomeTeam"], data_to_keep["AwayTeam"],
                                                              new_names):
                    combined_data[f"{new_name}"] = list_of_dfs[0][home_column] + list_of_dfs[1][
                        away_column]

                team_dfs.append(pd.DataFrame(combined_data))

            return pd.concat(team_dfs)
        except Exception as e:
            # TODO HANDLE
            print(e)
