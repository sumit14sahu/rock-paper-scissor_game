import random
print("Rock Paper Scissor GAME")
# rock = -1
# paper =  0
# scissor = 1
choice = input ("Enter Your Choice(r, p, s): ").lower()

if choice not in ["r", "p", "s"]:
    print("Invalid choice! Please enter r, p, or s.")
    exit()

comp = random.choice(["r","s","p"])

menu= {"r": "Rock", "p":"Paper", "s":"Scissor" }
print("Your choice is ",menu[choice])
print("Computer's choice is ", menu[comp])

if choice == comp:
    print("It's a draw")

elif choice == "r" and comp == "s":
    print("YOU Win!!!")

elif choice == "p" and comp == "r":
    print("YOU Win!!!")

elif choice == "s" and comp == "p":
    print("YOU Win!!!")

else:
    print("YOU Lose!!!")