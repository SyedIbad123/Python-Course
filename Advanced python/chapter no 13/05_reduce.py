# REDUCE METHOD..
# 01 : The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
# 02 : Reduce apply a rolling computation to sequential pair of elements.



# EXAMPLE ...
from functools import reduce
sum = lambda a,b : a + b
l = [1,2,3,4,5,6]
value = reduce(sum , l)
print (value)