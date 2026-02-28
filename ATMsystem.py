from datetime import datetime

# ---------------- USERS DATABASE ---------------- #

users = {
    "1001": {
        "pin": "1234",
        "name": "Tripti",
        "accounts": {
            "savings": {
                "balance": 100000,
                "statement": []
            },
            "current": {
                "balance": 50000,
                "statement": []
            }
        }
    },
    "1002": {
        "pin": "1111",
        "name": "cheekuu",
        "accounts": {
            "savings": {
                "balance": 70000,
                "statement": []
            },
            "current": {
                "balance": 20000,
                "statement": []
            }
        }
    }
}

# ---------------- LANGUAGE ---------------- #

print("Select Language")
print("1. English")
print("2. Hindi")

lang = input("Enter choice: ")

# ---------------- CARD FETCH ---------------- #

card = input("Insert your card (Enter Card ID): ")

if card not in users:
    print("Invalid Card")
    exit()

# ---------------- PIN ATTEMPTS ---------------- #

attempts = 0

while attempts < 3:
    pin = input("Enter PIN: ")

    if pin == users[card]["pin"]:
        print("Login Successful")
        break
    else:
        attempts += 1
        print("Wrong PIN")

if attempts == 3:
    print("Card Blocked")
    exit()

# ---------------- ACCOUNT TYPE ---------------- #

print("Select Account")
print("1. Savings")
print("2. Current")

acc_choice = input("Enter choice: ")

if acc_choice == "1":
    acc_type = "savings"
elif acc_choice == "2":
    acc_type = "current"
else:
    print("Invalid choice")
    exit()

account = users[card]["accounts"][acc_type]

# ---------------- ATM MENU ---------------- #

while True:

    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Bank Statement")
    print("4. Exit")

    choice = input("Enter choice: ")

    # -------- WITHDRAW -------- #
    if choice == "1":
        amount = int(input("Enter amount: "))

        if amount > account["balance"]:
            print("Insufficient Balance")
        else:
            account["balance"] -= amount
            date = datetime.now().strftime("%d-%m-%Y %H:%M")
            account["statement"].append(f"{amount} withdrawn on {date}")
            print("Withdrawal Successful")

    # -------- DEPOSIT -------- #
    elif choice == "2":
        amount = int(input("Enter amount: "))
        account["balance"] += amount
        date = datetime.now().strftime("%d-%m-%Y %H:%M")
        account["statement"].append(f"{amount} deposited on {date}")
        print("Deposit Successful")

    # -------- STATEMENT -------- #
    elif choice == "3":
        print("\n----- BANK STATEMENT -----")
        for record in account["statement"]:
            print(record)
        print("Current Balance:", account["balance"])

    # -------- EXIT -------- #
    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
