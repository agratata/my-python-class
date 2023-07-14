shop={
    "sneakers":10000,
    "skirt":5000,
    "socks":800,
    "slippers":3000,
    "shirt":900
}
for key,value in shop.items():
    print(key,value)

print("enter the name of the required item. enter 'done' to exit.")
pr=0
while True:
    item=input("input name: ")
    if item=="done":
        break
    pr+=shop[item]
    
if pr>24000:
    pr_final=pr-((10/100)*pr)
    print(f"actual price: {pr}")
    print(f"total price after 10% discount: {pr_final}")
else:
    print(f"total price: {pr}")