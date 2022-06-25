# find natural number.

def number(n):
    if n==1:
        print(n)
    else: 
        print(n)
        number(n-1)
n=int(input("enter no: "))
number(n)