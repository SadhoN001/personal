import random
a="""
1. ROCK
2. PAPER
3. SCISSORS
<<(computer VS You)>>
"""
print(a)
Me=int(input("How many times do you want to play : "))
def check(computer,you):
    
    if(computer==1 and you==2 ):
        return 1
    elif(computer==2 and you==1 ):
        return 0
    elif(computer==1 and you==3 ):
        return 0
    elif(computer==3 and you==1 ):
        return 1
    elif(computer==2 and you==3 ):
        return 1
    elif(computer==3 and you==2 ):
        return 0
    else:
        return 10
    
while(Me):
    Me=Me-1;
    computer=random.randint(1,3)
    you=int(input("1, 2 or 3 Which is your choice = "))
    print(f"Computer={computer} and you={you}")
    if(computer==you):
        print("!...DRAW...!\n")
    else:
        x=check(computer,you)
        if(x==10):
            print("Wrong Input\n")
        elif(x):
            print("Congrats!!! YOU WON \n")
        else:
            print("YOU LOSE...\n")
else:
    print("FINISHED.......!!!")