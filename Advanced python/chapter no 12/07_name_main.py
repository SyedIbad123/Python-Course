# __name__ evaluates to the name of the module in python from where the program is ran..
# If the module is ran directly from the command line, the __name__ is set to string "__main__". Thus, this behaviour is used t check whether the module is run directly or imported to another file.


def greet(name):
    print(f'Good Morning , {name}')

if __name__ == "__main__":
    n = input("Enter a name\n")
    greet(n)
    
    