# With statement..
# 01 : It is the alternative to close() function..
# 02 : The best way to open and close the file automatically we use with statement..


with open('sample.txt', 'r') as f:
    a = f.read()
print(a)