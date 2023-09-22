# MAP METHOD.
# 01 : map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# 02 : Map applies a function to all the items in an input list.
''' The syntax for map function is:
        map (function , iter)'''


# EXAMPLE...

def sum(num):
    return num+num
l1 = [12,18,20]
print(list(map(sum,l1))) # Here l1 is iter bcz we want to sum the list item that is in l1. list function is used to convert it into list.
