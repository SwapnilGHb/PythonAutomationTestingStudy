import os

print(os.getcwd()) # Returns the current working directory

#List files in the current directory
files = os.listdir('/Users/Swapnil Bahe/PycharmProjects/PyATB5xLearning')
print(f"Files in current directory: {files}")

# Create a new directory
#os.mkdir("Test2")

# Check if a file exists
file_exists = os.path.exists("TestData.txt")
print(file_exists)

print(os.name)
