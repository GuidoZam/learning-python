from fileinput import filename
import os

sampleFilePath = "c:/temp/some folder/file.txt"

# Get the file name from the path
fileName = os.path.basename(sampleFilePath)
print(fileName)

# Get the directory path
directoryPath = os.path.dirname(sampleFilePath)
print(directoryPath)

# Verify the existence of a file
fileExists = os.path.exists(sampleFilePath)
print(fileExists)

# Separate the file name and the path
pathParts = os.path.split(sampleFilePath)
print(pathParts)

# Separate the file extension from the rest of the path
splitText = os.path.splitext(sampleFilePath)
print(splitText)

# Get the current working directory
currentWorkingDirectory = os.getcwd()
print(currentWorkingDirectory)

# Change the current directory
os.chdir("../")
currentWorkingDirectory = os.getcwd()
print(currentWorkingDirectory)

# Get the current user name
login = os.getlogin()
print(login)

# Get the process groups ids
groups = os.getgroups()
print(groups)