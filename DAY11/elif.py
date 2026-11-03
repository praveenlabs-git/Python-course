print("Welcome to my budget planner!")
budget = int(input("Enter the budget: "))

print("You can go with ",end =" " )
if budget > 10000:
    print("You can go to trip")
elif budget > 5000:
    print("You can go to a resort")
elif budget > 2000:
    print("You can go to a movie")
elif budget > 1000:
    print("You can go to street shopping")
elif budget > 500:
    print("You can go to a park")
else:
    print("Better save for next time you idoit! wasting my time")
