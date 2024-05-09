import pandas as pd
import requests

class network_manager:
    @staticmethod
    def get_json_data(request):
        __token_id = "PIPsnX8gPx038gU8dJgt1JBMaBN893Yc5RBdB8gcSOTXE6l9VDgqLBl3DuYv"
        url = f"https://api.sportmonks.com/v3/football/{request}?api_token={__token_id}"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            print("ERROR")
            return None