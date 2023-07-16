info_file=open("file_handling/bill.txt","a+")
base_menu={"cheese":100,"pesto":90}
top_menu={"olive":50,"chicken":40,"ham":70, "pepperoni":70 ,"bacon":70, "jalapeno":30, "garlic":30, "basil":40}

def menu():
   print("\nPIZZA BASE MENU")
   for x,y in base_menu.items():
      print(x,y)
   print("\nTOPPING MENU")
   for x,y in top_menu.items():
      print(x,y)

#5 customer input
for i in range(0,5,1):
   #customer display
   name=input("what is your name?: ")
   info_file.write(f"Name: {name}")
   print(f"Welcome to the shop, {name}")

   #printing menu
   menu()

   #input magdai + file ma lekhdai
   try:
      base=input("pizza base:")
      info_file.write(f"\n\torder details...\n{base}:{base_menu[base]}")
      amt=0
      amt+=base_menu[base]
   except:
      print("item is not in the menu")
      amt+=0
   
   i=0
   while True:
      i+=1
      topping=input(f"topping{i}: ")
      if topping=="done":
         break
      info_file.write(f"\n\t{topping}:{top_menu[topping]}")
      amt+=top_menu[topping]
      info_file.write(f"\ntotal bill is: {amt}\n\n")

   #printing bill informaion for the customer
   print(f"total bill is: {amt}\n")