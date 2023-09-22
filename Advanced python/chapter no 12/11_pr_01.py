#  Program to open three files. If any of these files are not present , a message without exiting a program must be printed prompting the same.

def read_File(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

read_File("1.txt")
read_File("2.txt")
read_File("3.txt")
