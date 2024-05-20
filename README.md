# FootballResults

A python based programm to visualize football data

# Table of contents

- Installation
- Usage
- Features
- Contributing
- License
- Contact

# Installation

### Clone the repository

    git clone https://github.com/alexanderhepburn/FootballResults.git

### Navigate to the project directory

    cd FootballResults

### Install the required dependencies

    pip install -r requirements.txt

# Usage

### Example of how to use the programm --> see run.py

    from misc import setup_program

    if __name__ == '__main__':
        setup_program()  # Download all requirements
        # Imported after SetupProgram to make sure all requirements have been downloaded
        from commands import run_program

        run_program()

### Command Execution Loop:

- The program enters a loop where it waits for user input.
- Upon receiving input, it checks if the input matches any available command.
- If a match is found, the corresponding command is executed.
- If no match is found, an error message is displayed indicating that the input is invalid.

# Features

### Available Commands:

- Help Command: Provides a list of available commands and their descriptions.
- Settings Command: Allows the user to view and modify program settings.
- Teams Command: Displays a list of teams.
- UpdateData Command: Updates or retrieves data required by the program.
- Analyse Command: Performs analysis on specified data.

### Note:

- This structure allows the program to be modular, with individual commands encapsulated in separate functions or
  classes.
  It promotes code organization, maintainability, and ease of adding new features or commands.

# Contributing

- Fork the repository
- Create a new branch for your feature or bug fix
- Commit your changes
- Push to the branch
- Open a Pull Request

# License

??? IS THERE A SPECIAL LICENSE? THIS IS A PROJECT FOR THE UNIVERSITY OF ST. GALLEN LOL

# Contact

- Email: student@student.unisg.ch
- linkedin: www.linkedin.com/in/student
- GitHub: https://github.com/Student


