# Programme for a simple calculator

def add(x, y):
    return x + y
    

def subtract(x, y):
    return x - y
    

def divide(x, y):
    return x / y
    

def square(x):
    return x ** 2
   
def multiply(x, y):
    return x * y


print("Please select: \n 1. sum \n 2.subtraction \n 3.division \n 4.square\n 5.multiply \n")

choise = int(input("input selection: "))

x = int(input("1st number: "))
y = int(input("2nd number: "))


if choise == 1:
    print(f"sum is: {add(x,y)}")

elif choise == 2:
    print(f"subtraction is: {subtract(x,y)}")

elif choise == 3:
    print(f"division is: {divide(x,y)}")

elif choise == 4:
    print(f"square is: {square(x)}")

elif choise == 5:
    print(f"product is: {multiply(x,y)}")





