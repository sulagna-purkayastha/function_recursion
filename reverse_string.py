def my_func(s,n):
    if n==0:
        print(s[0])
    else:
        print(s[n],end="")
        my_func(s,n-1)
s=input("enter string: ")
my_func(s,int(len(s))-1)