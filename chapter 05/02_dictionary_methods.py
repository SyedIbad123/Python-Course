# Dictionry methods


mydict = {
    "fast" : "in a quick manner",
    "slow" : "lazy",
    "ibad" : "A coder"
}


# A - Key method
# the type of mydict.keys are (dict_keys)
print(mydict.keys()) # it prints the keys of the dictionary
print(type(mydict.keys()))
print(list(mydict.keys())) # we can convert it into list by using this syntax...


# B - Value method 
print(mydict.values()) # it prints the values of dictionary...


# C - Item method
print(mydict.items()) # it returns tuple..


# D - Update method
# It also updates the existing values
updatedict = {
    "mahad" : "gadha"
}
mydict.update(updatedict) # This method is used to edit dictionary and updates dictionary by adding key value pairs from updatedict


# E - Get method
# If there is nothing in dictionary it prints (none).
print(mydict.get("fast")) # It prints the value of key...



