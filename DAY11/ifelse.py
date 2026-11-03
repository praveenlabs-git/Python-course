#data = ("admin@gmail.com", "admin@123")

#email = input("Enter your mailid: ")
#password = input("Enter your password: ")

#if (email,password) == data:

#    print("Login successful")

#else:
#    print("Login is invalid")



#seats = {
#    'S1': 'available',
#    'S2': 'Booked',
#    'S3': 'available',
 #   'S4': 'Booked',
#   'S5': 'available',
#    'S6': 'available',
#}

#seatno = input("Enter the seat number(sn): ")

#if (seatno in seats) and seats[seatno] == 'available':
#   seats[seatno] = 'Booked'
#    print(f"Seat {seatno} is booked successfully.")
#    print(seats)
#else:
#    print(f' {seatno} is already booked')


products = {
    'laptop':{'price': 75000, 'stock': 23},
    'mobile':{'price': 25000, 'stock': 50},
    'tablet':{'price': 15000, 'stock':0},
    'headphones':{'price': 5000, 'stock': 100},
    'keyboard':{'price': 2000, 'stock': 75},
}

search = input("Enter the product name: ")

if search in products and products[search]['stock']>0:
    print(f'You can buy {search} at the price: {products[search]["price"]}')
else:
    print(f'{search} is not available in stock')