a=float(input("enter first number: "))
b=float(input("enter second numebr: "))
op=input("enter any operator(+, -, *, /, %): ")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
elif op=="%":
    print(a%b)
elif type(op)==str:
    print("program invalid")
else:
    print("invalid input")