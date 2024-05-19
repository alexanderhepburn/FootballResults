from misc.helper_methods import SetupProgram

if __name__ == '__main__':
    SetupProgram()  # Download all requirements

    # Imported after SetupProgram to make sure all requirements have been downloaded
    from managers.command_manager import CommandManager

    CommandManager.run_program()
