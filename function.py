#a and b are parameters
def calc(op,a,b):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    elif op=="%":
        return a%b
    else:
        return None
    #default return type is None

#x and y are arguments
x=int(input("number1: "))
y=int(input("number2: "))
op=input("operator: ")
print(f"{x} {op} {y} = {calc(op,x,y)}")