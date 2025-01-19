file_name = "pramod.txt"
content = "This is Pramod's File ABC"

with open("pramod.txt", "w") as file:
    file.write(content)

with open("pramod.txt", "r") as file:
    content2 = file.read()
    print(content2)

# os.chdir("Desktop")
