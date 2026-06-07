try:
    num1=int(input("enter first no:"))
    num2=int(input("enter second no:"))
    quotient=num1/num2
    print("both numbers are correct")
except ValueError:
    print("please enter only numbers")
except ZeroDivisionError:
    print("num2 should not be zero")
else:
    print("great!! you are a good programmer")
finally:
    print("job over,go! get some rest")
