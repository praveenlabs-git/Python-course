data = {
    'praveen':{'status':True, 'python': 97,'java': 98,'c': 95},
    'john':{'status':True, 'python': 85,'java': 80,'c': 75},
    'alice':{'status':True, 'python': 68,'java': 65,'c': 60},
    'aditya':{'status':True, 'python': 12,'java': 13,'c': 14},
    'varshit':{'status':False, 'python': None,'java':None,'c': None},
    'sachin':{'status':True, 'python': 45,'java': 50,'c': 55},
}

name = input("Enter the name: ")

if name in data:
    if data[name]['status']:
        total = data[name]['python'] + data[name]['java'] + data[name]['c']
        avg = total/3
        if avg >80:
            print(f"{name},Congrates you got 1st grade ")
        elif avg >60:
            print(f"{name},Congrates you got 2nd grade ")
        elif avg >50:
            print(f"{name},Better perform next time ")
        elif avg >40:
            print(f"{name},you have just passed the exam ")
        else:
            print(f"{name},you are failed in the exam ")
    else:
        print(f"{name},did not attend the exam bring your parent to the school ")
else:
    print(f"{name},is not in the data ")