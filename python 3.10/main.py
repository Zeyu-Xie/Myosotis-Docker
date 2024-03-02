import os

if __name__ == "__main__":
    os.system("clear")
    # System Info
    print("=== System Info ===")
    os.system("uname -a")
    print("")
    # Python Version
    print("=== Python Version ===")
    os.system("python --version")
    print("")
    # Pip List
    print("=== Pip List ===")
    os.system("pip list")
    print("")
    # File Path
    print("=== File Path ===")
    print(os.path.abspath(__file__))
    print("")