# Program to find the given word in file..

with open('sample.txt', 'r') as f:
    a = f.read()
    if "university" in a:
        print("yes ! word is present")
    else:
        print("No ! word is not present")