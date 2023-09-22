# Program to create a class a, create an object from it and set  a directly using object a = 0. Does this change  the  class attribute..
 
 
class sample:
    a = "ibad"

obj = sample()
obj.a = "vicky"    # Here class attribute does'nt change but an instance attribute is create..
sample.a = "vickky"  # Here a class attribute is changed..  
print(sample.a)
print(obj.a)
        
     