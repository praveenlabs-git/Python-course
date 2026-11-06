'''
l = [12, 9, 3, 4, 5, 10, 2, 4, 5, 2, 4, 5]

i = 0
j = len(l) - 1

while i <= j:
    if i == j:
        print(l[i]) 
    else:
        print(l[i]+ l[j])
    i+= 1
    j-= 1
'''
'''
bill = 0

while True:
    product = input("Enter the name of the product(STOP): ")
    if product == "STOP":
        print("Total bill: ", bill)
        break
    price = int(input("Enter the price of the product: "))
    quantity = int(input("Enter the quantity of the product: "))
    bill += price * quantity
'''
'''
products = {
    "Rice": 60,
    "Sugar": 45,
    "Milk": 30,
    "Oil": 150,
    "Bread": 40
}

bill = 0
cart = {}

print("========== WELCOME TO THE STORE ==========")

while True:
    print("\n---------- PRODUCT MENU ----------")

    for product, price in products.items():
        print(product, ":", price)

    print("----------------------------------")

    choice = input("Enter product name (STOP): ").title()

    if choice == "Stop":
        break

    if choice not in products:
        print("Product not available!")
        continue

    quantity = int(input("Enter quantity: "))

    price = products[choice]
    amount = price * quantity

    bill += amount

    cart[choice] = cart.get(choice, 0) + quantity

    print("Product:", choice)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Amount:", amount)

print("\n========== FINAL BILL ==========")

print("Product\tQuantity\tPrice\tTotal")

for product, quantity in cart.items():
    price = products[product]
    total = price * quantity

    print(product, "\t", quantity, "\t\t", price, "\t", total)

print("----------------------------------")
print("Total Bill:", bill)
print("Thank you for shopping with us!")
print("==================================")
'''

products =  {
     "Rice": 60,
        "Sugar": 45,
        "Milk": 30,
        "Oil": 150,
        "Bread": 40
}

# display menu 
print("Welcome to the store".center(50,'-'))
print("ProductName ,'price'")
for i in products:
    print(i.ljust(12,' '),':',products[i])


carts = {}
while True:
    cart = input("Enter the Product Name (exit): ").lower()
    if cart == 'exit':
        break
    qua = int(input("Enter the Quantity: "))
    carts[cart]= qau

print("Bill".center(50,'-'))
print('Product Name Quantity price')
bill = 0 
for i in carts:
    print(i.ljust(12,' '),str(cart[i]).ljust(12,' '),products[i])
    bill += carts[i]*products[i]

print(f"Total bill: {bill}")
print("Thanks for shopping in the store")

