import random
user_score=0
comp_score=0
for i in range (0,5,1):
    print(" ")
    user=int(input("enter a number from 1 to 6: "))
    comp=int(random.randint(1,6))
    print(f"computer generation: {comp}")

    if comp==user:
        print("draw")
    
    elif user>comp:
        user_score+=10
        print("you: ",user_score)
        print("computer: ",comp_score)
    
    elif comp>user:
        comp_score+=10
        print("you: ",user_score)
        print("computer: ",comp_score)

if user_score>comp_score:
    print("you win!")
elif user_score<comp_score:
    print("you lose!")
elif user_score==comp_score:
    print("it's draw!")