def show_balance():
    print(f"Your balance is {balance:.2f}")

def deposit():
    amt = float(input("Enter the amount to be depodited:"))
    print("-----------------------")
    
    if amt < 0:
        print("Amount cant be negative:")
        return 0
    else:
        return amt

def withdraw():
    amount = float(input("Enter the amount to be withdrwn: "))
    print("-----------------------")
    if amount > balance:
        print("insufficient balance")
        return 0
    elif amount < 0:
        print("amount should be greter than zero")
        return 0
    else:
        return amount

balance = 0
is_running = True
while is_running:
    print("***************")
    print("Banking Program")
    print("***************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    print("***************")
    choice = input("What do you want to do? ")
    print("****************")

    if choice == "1":
        show_balance()

    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice")

print("Thank you have a nice day!")