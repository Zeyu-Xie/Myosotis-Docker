import os
import subprocess

# Config Variables
name = "xelatex"

# Check if Docker image exists
result = subprocess.getoutput(f"docker images -q --filter reference={name} | head -n 1")

# No Image Found
if not result:
    print("\033[1;31mDocker Image not Found\033[0m")
    option = input("- Do you want to build the image now? (Y/N) ")
    if option.lower() == "y":
        subprocess.run(["docker", "build", "-t", name, os.path.dirname(__file__)])
    else:
        print("You have canceled building the image.")

# Image Exists
else:
    print("\033[1;32mImage Exists\033[0m")
    docker_time = subprocess.getoutput(f"docker inspect --format='{{{{.Created}}}}' {name} | head -n 1")
    print(f"Your image was created at {docker_time}.")
    print("\033[0;34m1. Run Image")
    print("2. Remove Image")
    print("3. Exit\033[0m")
    option = input("- Please choose your option (1-3): ")
    if option == "1":
        subprocess.run(["docker", "run", "-i", "-v", f"{os.path.dirname(__file__)}:/app", "-t", result])
    elif option == "2":
        subprocess.run(["docker", "rmi", "-f", result])
        print(f"Image {result} has been removed.")
    elif option == "3":
        print("You have canceled image running.")
    else:
        print("ERROR: Illegal Option. Quit.")
