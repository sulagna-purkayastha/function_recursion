# table

# def table(n,y=1):
#     if y==10:
#         print(n*y)
#     else:
#         print(n*y)
#         table(n,y+1)
# n=int(input("enter no: "))
# table(n)


# reverse table

def table(n,y=10):
    if y==1:
        print(n*y)
    else:
        print(n*y)
        table(n,y-1)
n=int(input("enter no: "))
table(n)