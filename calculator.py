#calculator.py

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
         print("Error! Division by zero is not allowed")

def get_2in():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return x, y

while True:

    print("\nOperation \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1 :
        print(add(*get_2in()))
    elif ch == 2:
        print(sub(*get_2in()))
    elif ch == 3:
        print(mul(*get_2in()))
    elif ch == 4 :
        print(div(*get_2in()))
    elif ch == 5:
        print(".......\n")
        break
    else:
        print("Invalid Option")
    
