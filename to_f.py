def convert(c):
    f=(c*(9/5))+32
    return f

c=float(input("temperature in celsius: "))
print(f"temperature in farenhet: {convert(c)}")