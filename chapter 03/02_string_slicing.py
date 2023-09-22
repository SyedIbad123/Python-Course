
# STRING SLICING

''' 
01 : index is always started with (*0)....
02 : we use square brackets for call the index of string...
03 : index = lenght(*of the string) - 1 
04 : length of the string is equal to the number of alphabets or characters used...
05 : For printing the index of the string we first write its variable than the index inside the square bracket => print(*variable[*index number])
06 : we will never change the character of string => 
variable[*index number] = "any alphabet/character" (this generates type error)....
07 : string slicing (break the strings into parts) this can be done by the method => 
print(*variable[*first index number:last index number])# In slicing last index number is not counted(*end-1)..
08 : if we leave a first index blank it always sense minimum value of index which means (*0)
09 : negative indice always starts at the end of tha string means tha last character of the string have index (*-1)
10 : spaces also includes in index when we written more than one words...
11 : if we pass third argument it means step-size or skip value(means that how many index are left)
'''

a = "ibad"
print(a[0])
print(a[0:3]) # slicing
print(a[:4]) # is same as [0:4]
print(a[0:]) # is same as [0:4],(* 4 is length of a string)..
print(a[-3:-1]) # it is same as a[1:2]..


# slicing with skip value or step size
name = "ibadisgoodboy"
print(name[0:4:2]) # here (2) is skip value means the characters print after skipping one value...
