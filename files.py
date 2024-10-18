import os

print("Program To List Files or Folders in a Directory\n\n")

folders = input("Input the folder names with a space in between: ").split()

for folder in folders:
    try:
        dirr = os.listdir(folder)
        print(f"\nFiles and Folders in '{folder}' are: {dirr}")
    except FileNotFoundError:
        print(f"\nFolder '{folder}' not found")