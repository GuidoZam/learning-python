import os

def getName(message: str) -> str:
    print(message)
    inputValue = input()
    return inputValue

def createFile(fileName: str, content: str):
    try:
        with open(fileName, "w") as f:
            f.write(content)
    except FileNotFoundError:
        # str.format() with names
        print("File '{fileName}' not found!".format(fileName = fileName))

print("Hi! I'm a program that creates a directory, some sample files and then delete all of the created stuff :)")
print("Press enter to begin")
input()

dirName = getName("What is the name of directory to create?")
firstFileName  = getName("What is the name of the first text file?")
if (firstFileName.endswith(".txt") == False):
    firstFileName += ".txt"

secondFileName  = getName("What is the name of the second text file?")
if (secondFileName.endswith(".txt") == False):
    secondFileName += ".txt"

# Old school formatting
print("Creating folder '%s' in path '%s'" % (dirName, os.getcwd()))
os.mkdir(dirName)
os.chdir(dirName)

# str.format()
print("Creating first file named {}".format(firstFileName))
createFile(firstFileName, "Some sample content")

# str.format() with index
print("Creating second file named {0}".format(secondFileName))
createFile(secondFileName, "Some sample content")

print("Files created!")
print("Go and check the results, after that press ENTER here to delete the created files and directory.")
input()

os.remove(firstFileName)
os.remove(secondFileName)
os.chdir("../")
os.rmdir(dirName)

print("All done!")
print("Bye! :)")