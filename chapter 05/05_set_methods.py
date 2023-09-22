# Set method in pyhton programming
# 01 : We can't add list in set.
# 02 : we can add tuples in set..
# 03 : we can't add dictonary in set..


# Properties of Set
# 01 : sets are unordered(elments order doesnt matters)
# 02 : sets are unindexed(can't accessed items through index)
# 03 : there is no way to change items in sets
# 04 : sets can't contain duplicate elements.




# A - Add method
a = {1,2,3,4}
a.add(5) # This adds an element at the end of the set.
print(a)


# B - Length method
print(len(a)) # it prints the length of set..


# C - Rmeove method 
a.remove(2) # it removes the given value
print(a) 


# D - Pop method
b = {1,2,3}
print(b.pop()) # it removes random value from set


# E - Clear method
# its empty the set

# F - Union method
c = {1,2,3}
d = {4,5,6}
e = d.union(c)
print(e)


# G - Intersection method
c = {1,2,3}
d = {4,5,6}
e = d.intersection(c)
print(e)


