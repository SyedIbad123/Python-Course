# program to find greatest of four numbers using fucntions....

def maximum(num1,num2,num3,num4):
    if num1>num4:
        if num1>num3:
            return num1
        else:
            return num3
        
    elif num4>num3:
        if num4>num2:
            return num4
        else:
            return num2
    else:
        if num2>num3:
            return num2
        else:
            return num3
        
m = maximum(20,11,100,60)
print("The value of maximum number is : ", m)
    