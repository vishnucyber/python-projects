import random
choices = ("r","p","s")

while True:
    user = input("Choose rock,paper,scissors.?(r/p/s): " ).lower()
    computer = random.choice(choices)
    print(f"You chose {user}")
    print(f"Computer chose {computer}")

    if user not in choices:
        print("Invalid choice")
    elif "user" == "computer":
        print("Tie")
    elif user == "r" and computer == "s" :
         print("You won") 
    elif user == "s" and computer == "p" :
        print("You won")
    elif user == "p" and computer == "r" :
        print("You won")
    else:
        print("You lost")
    next = input("Do you want to continue (y/n): ").lower()
    if next == "n":
        break
    else:
        continue