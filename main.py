import subprocess
import sys

if __name__ == '__main__':
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    from command_manager import command_manager

    command_manager().run_program()
