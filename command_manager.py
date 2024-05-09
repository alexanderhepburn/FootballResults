import pandas as pd
from network_manager import network_manager
from tabulate import tabulate

class command_manager:

    def run_program(self):
        self.__list_of_commands = {"help": {"function" : self.info, "description" : "This function helps you"},
                                   "leagues": {"function" : self.get_leagues, "description" : "INPUT DESCR"}}

        print(f"Welcome to the FootballResults program!")
        print(f"For a list of all commands, please type help.")
        while True:
            try:
                user_input = input(f"Please enter your command: ")

                if user_input == "end":
                    print(f"Thank you for using our program! Bye!")
                    return

                if not user_input in self.__list_of_commands:
                    print(f"Error your command: {user_input} is not a valid input!")
                    print(f"Please reenter your command or type help for a directory of all commands.")
                    continue

                self.__list_of_commands[user_input]["function"]()
            except KeyError:
                print("Error Function")

    def info(self):
        print(f"\nPrinting all of the available commands:")
        for method, contents in self.__list_of_commands.items():
            try:
                print(f"{method}: {contents['description']}")
            except KeyError:
                print(f"{method}: No description")
        print("") # Adding space for readibility

    def get_leagues(self):
        try:
            request_information = f"leagues"
            results = network_manager.get_json_data(request_information)
            df = pd.DataFrame(results["data"])
            df.set_index("id", inplace=True)

            print(tabulate(df[['name']], headers='keys', tablefmt='psql'))
        except:
            print("ERRORORROROROROR")