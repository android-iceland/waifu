# import os
# os.system("python app.py")
import os

def run_app():
    try:
        os.system("python app.py")
    except KeyboardInterrupt:
        print("Script stopped by user")

if __name__ == "__main__":
    while True:
        run_app()
