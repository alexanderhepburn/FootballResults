from command_manager import command_manager
from network_manager import network_manager
import subprocess
import sys

if __name__ == '__main__':
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    command_manager().run_program()
