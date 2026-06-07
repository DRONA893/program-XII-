def fact (n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=int(input("enter a number:"))
result=fact(x)
print("factorial of",x,"is",result)
