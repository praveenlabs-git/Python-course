
data = {
    123456: {"pin": 1234, "balance": 7000, "transactions": []},
    123457: {"pin": 1234, "balance": 7000, "transactions": []},
    123458: {"pin": 1234, "balance": 7000, "transactions": []},
    123459: {"pin": 1234, "balance": 7000, "transactions": []},
    123450: {"pin": 1234, "balance": 7000, "transactions": []}
}


def login():
    global accu_number

    accu_number = int(input("Enter account number: "))
    pin = int(input("Enter PIN: "))

    if accu_number in data and data[accu_number]['pin'] == pin:
        print("Login Successful!")
        return True
    else:
        print("Invalid Login!")
        return False


def menu():
    print("\n---------- ATM MENU ----------")
    print("[C] Check Balance")
    print("[D] Deposit")
    print("[W] Withdraw")
    print("[T] Transactions")
    print("[P] Change PIN")
    print("[E] Exit")


def checkbalance():
    print(f"Current balance: ₹{data[accu_number]['balance']}")


def deposit():
    amount = int(input("Enter amount to deposit: "))

    if amount > 0:
        data[accu_number]['balance'] += amount
        data[accu_number]['transactions'].append(
            f"Deposited: ₹{amount}"
        )
        print(f"₹{amount} deposited successfully")
    else:
        print("Enter a valid amount")


def withdraw():
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Enter a valid amount")

    elif data[accu_number]['balance'] >= amount:
        data[accu_number]['balance'] -= amount
        data[accu_number]['transactions'].append(
            f"Withdrawn: ₹{amount}"
        )
        print(f"₹{amount} withdrawn successfully")

    else:
        print("Insufficient Balance")


def transactions():
    history = data[accu_number]['transactions']

    if history:
        print("\n------- Transaction History -------")

        for i in history:
            print(i)
    else:
        print("No Transactions Yet")


def changepin():
    old_pin = int(input("Enter old PIN: "))

    if old_pin == data[accu_number]['pin']:

        new_pin = int(input("Enter new PIN: "))
        confirm_pin = int(input("Confirm new PIN: "))

        if new_pin == confirm_pin and 1000 <= new_pin <= 9999:
            data[accu_number]['pin'] = new_pin
            print("PIN changed successfully!")
        else:
            print("Invalid PIN or PINs do not match")

    else:
        print("Incorrect old PIN")
