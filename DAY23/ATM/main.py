import logic

if logic.login():

    while True:
        logic.menu()

        choice = input("Enter your choice: ").upper()

        if choice == 'C':
            logic.checkbalance()

        elif choice == 'D':
            logic.deposit()

        elif choice == 'W':
            logic.withdraw()

        elif choice == 'T':
            logic.transactions()

        elif choice == 'P':
            logic.changepin()

        elif choice == 'E':
            print("Thank you for using our ATM")
            break

        else:
            print("Invalid choice. Try again.")