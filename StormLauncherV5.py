# removed virus

import subprocess
import time

def launch_fortnite():
    try:
        path = input("Enter the path to FortniteLauncher.exe: ")
        subprocess.Popen([path])
        print("Fortnite launched successfully.")
    except Exception as e:
        print(f"Error launching Fortnite: {e}")

if __name__ == "__main__":
    launch_fortnite()
    time.sleep(10)  # Adjust the delay if necessary
