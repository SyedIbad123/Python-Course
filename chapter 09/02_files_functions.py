
# Functions of files in python...

# A - Opening a file
# 01: For this, we should use Python’s inbuilt function open().  
# 02 : It takes two parameters : filename , mode..
'''The syntax for opening a file is:
        f = open(filename, mode)'''



# Read function of file..
# 01 : In read function we are only read file..
# 02 : If we are not specify any mode, it will default read...


f = open('sample.txt') 
a = f.read() 
b = f.read(10) # Reads 10 characters from the file..
print(a)
f.close()



# Write function of file..
# 01 : In write function we edit the file to write in this file..
# 02 : It takes always one argument..

f = open('sample.txt', 'w')
a = f.write("i am ibad ali")
f.close()



# Readline function of file..
# 01 : This function only reads one line in file..
f = open('sample.txt')
a = f.readlines()
print(a)
f.close()



# Modes of files in python...
# 01 : Mode is the purpose of opening a file.
# 02 : At the time of opening, we have to specify the mode, which represents the purpose of the opening file and what we are going to done with that specific file.
# 03 : When we open a file we must have to close a file, for this we use built-in function called close()..

f = open('sample.txt','r') # "r" is read mode..
for each in f:   # Here we use loop to print file content...
    print (each)
f.close()
    
file = open("sample.txt", "r")
print (file.read())  # This is the second and best way...
file.close()

file = open("sample.txt", "w") # "w" represents write mode..
f = file.write("he is a good boy")
print(f)
file.close()


file = open("sample.txt", "a") # "a" is used for appending..
f = file.write("Ned university")
file.close()



