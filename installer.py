import os
import subprocess

def install_requirements():
    subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

def run_app():
    subprocess.Popen(['python', 'app.py'])

if __name__ == '__main__':
    print("Installing requirements...")
    install_requirements()
    print("Running the application...")
    run_app()
