# STRING FUNCTIONS

''' In python when we use functions this method is followed..
print(*function(*variable))
'''


Intro = "my name is syed ibad ali. I am studying at ned university of engineering and technology in software engineering."


# Length function
# 01 : it returns the number of characters stored in any variable....

print(len(Intro))


# A - endswith function
# 01 : It gives output in either true or false format according to the given input that is (endswith)
# 02 : The function of this syntax is => print(*variable.endswith("any string"))...

print(Intro.endswith("engineering.")) # it returns true (. dot is mendatory otherwise it returns false)
print(Intro.endswith("ibad")) # it returns false


# B - count function 
# 01 : The function of this syntax is => print(*variable.count("any character of string"))...
# 02 : in most of the cases it is used to find characters (* you will also find words with this function)..

print(Intro.count("a")) # it returns the number of character(a) in Intro..


# C - capatilize function
# 01 : it capatilize the first word of sentence

print(Intro.capitalize())


# D - Find function
# 01 : it returns the value of index of whole sentence..
# 02 : if we find a character/word that is not in sentence it returns (*-1)..
# 03 : if we find a character/word that is in sentence but more than one time it always returns the first occurence.

print(Intro.find("my"))


# E - Replace function
# 01 : it replaces an old word with new word in entire string..
# O2 : The syntax of this function is => print(variable.replace(old word , new word))

print(Intro.replace("my", "once")) # it replaces my with once in Intro in output..


# F - Strip functon
# 01 : It prints the string as it is we write in our code

a = "Ibad is the student of section              A"
print(a.strip())
