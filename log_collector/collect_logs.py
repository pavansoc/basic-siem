import time
from datetime import datetime

LOG_FILE = "custom.log"

def generate_log():
    while True:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} - WARNING: root login from unknown source\n")
        time.sleep(10)

if __name__ == "__main__":
    print("[1] Start Log Collection")
    print("[2] Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Collecting logs... (Press Ctrl+C to stop)")
        generate_log()
    else:
        print("Exiting...")
