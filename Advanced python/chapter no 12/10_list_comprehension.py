# LIST COMPREHENSION
# 01 : Python List comprehension provides a much more short syntax for creating a new list based on the values of an existing list.
# 02 : 


# EXAMPLE NO : 01
a = [12,3,4,5,6,7,8,33,4,455,66,77,88,9,2,2,24444,4,5555,7,78888,9,99,9,9943,3333]
b = [i for i in a if i%2 == 0 ]
print(b)


# EXAMPLE NO : 02 
t = [1,2,3,4,55,222,3,4,2,1]
s = {i for i in t}    # Set comprehension..
print(s)