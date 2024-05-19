from misc import *

if __name__ == '__main__':
    setup_program()  # Download all requirements

    # Imported after SetupProgram to make sure all requirements have been downloaded
    from commands import run_program

    run_program()
