import pandas as pd
import os

class data_manager:
    @staticmethod
    def get_data_as_df(year):
        df = pd.read_csv(f"data/{year-1}{year}.csv")
        return df

    @staticmethod
    def get_all_data():
        directory = os.fsencode("data")

        list_of_df = []

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if not filename.endswith(".csv"):
                print("ERROR Filename CSV")
                continue
            df = pd.read_csv(f"data/{filename}")
            list_of_df.append(df)
        combined_df = pd.concat(list_of_df)
        return combined_df