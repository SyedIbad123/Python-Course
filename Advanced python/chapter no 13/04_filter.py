# FILTER METHOD..
# 01 : The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# 02 : Filter creates a list of items for which the function returns true.


# EXAMPLE..
def less_than(num):
    if num<10:
        return True
    else:
        return False
l = [1,23,45,5,6,9,10,76,555]
print(list(filter(less_than , l)))