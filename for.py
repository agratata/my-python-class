for calc in range(0,3,1):
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
    else:
        print("invalid input")