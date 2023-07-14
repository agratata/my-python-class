#prime or composite
def check_prime(num):
    c=0
    for i in range(1,num+1,1):
        if num%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False

num=int(input("enter input: "))
if check_prime(num)==True:
    print(f"{num} is prime")
else:
    print(f"{num} is composite")