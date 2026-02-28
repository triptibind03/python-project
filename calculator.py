def add(a,b):
    return a+b
def subtract(a,b):
    return a-b  
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "error: division by zero"
    else:
        return a/b
print("simple calculator")
print(1. addition)
print(2. subtraction)
print(3. multiplication)
print(4. division)
choice-int(input("enter choice: "))

x=int(input("enter first number: "))
y=int(input("enter second number: "))
if choice==1:
    print("result: ", add(x,y))
elif choice==2:
    print("result: ", subtract(x,y))
elif choice==3:
    print("result: ", multiply(x,y))
elif choice==4:
    print("result: ", divide(x,y))
else:
    print("invalid choice") 
