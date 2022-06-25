def my_func(x,y):
    if y==0:
        return 1
    else:
        return(x*my_func(x,y-1))
x= int(input("enter no:  "))
y= int(input("enter exponent:  "))
print(my_func(x,y))