def price(it):
    if it==1:
        return 10000
    elif it==2:
        return 5000
    elif it==3:
        return 800
    elif it==4:
        return 3000
    elif it==5:
        return 900
    else:
        return 0

shop={
    "1.sneakers":10000,
    "2.skirt":5000,
    "3.socks":800,
    "4.slippers":3000,
    "5.shirt":900
}
for key,value in shop:
    print(key,value)

print("enter serial number of items you want to purchase. enter -1 to exit")
a=0
pr=0
while a!=-1:
    a=int((input("input serial number: ")))
    pr+=price(a)

if pr>25000:
     pr_final=pr-((10/100)*pr)
     print(f"actual price: {pr}")
     print(f"total price after 10% discount: {pr_final}")
else:
    print(f"total price: {pr}")