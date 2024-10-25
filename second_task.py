print("welcome, this is basic calculator")
y=float(input("enter first number\n "))
x=float(input("enter second number\n "))
c=input("chose operator +,/,*,-\n")

if c=='+':
    print(f"the addition of {x} and {y} is ",x + y)
elif c=="-":
    print(f"the substraction of  {x} and {y} is ",x - y)
elif c=="/":
    print(f"the division of {x}  and {y} is ",x / y)
else:
    print(f"the multipliation of {x} and  {y}  is ",x * y)



