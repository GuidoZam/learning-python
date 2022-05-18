import os

print("Listing all txt files in the current directory")

files = []

for file in os.listdir():
    if file.endswith(".txt"):
        files.append(file)

print(files)