# local scope --> if we declare in the function we can only access it in the inside not outside
# global dec --> if we declare in the function we can access it across the file 


# local
#ef display():
#    n = 10
#    print("Inside:", n)

#display()
#print("Outside:", n)

# global dec
#def display():
#    global n
#    n = 10
#    print("Inside ",n)

#display()
#print("Outside",n)

# global --> effect across the file 
# non local --> effect only the fuction 

#def display():
#    course ="JFS"
#    print("Starting:",course)
#    def update():
#        course ="PFS"
#        print("Updated:",course)
#    update()
#    print("Final:",course)
#display()

# global

#def display():
#    course ="JFS"
#    print("Starting:",course)
#    def update():
#        nonlocal course
#        course ="PFS"
#        print("Updated:",course)
#    update()
#    print("Final:",course)
#display()


# build scope 
#max
#s = "codegnan"

#max = 20

#print(max(s))

# len

#s = "codegnan"

#len = 10

#print(len(s))


