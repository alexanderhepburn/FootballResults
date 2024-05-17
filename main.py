import subprocess
import sys
import os

if __name__ == '__main__':
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)
    os.makedirs("tmp", exist_ok=True)
    os.makedirs("exports", exist_ok=True)
    from command_manager import CommandManager

    CommandManager.run_program()
