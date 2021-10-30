import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        infile = open(filename, "r")
        print("File opened.")
        return True
    except:
        print("Unexpected error!")
        return False

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        return num1 / num2

    except:
        if num2 == 0:
            return "Error: Divide by Zero"
        elif isinstance(num1, str) or isinstance(num2, str):
            return "Error: Can't divide with strings"
        else:
            return "Error"
## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    try:
        x1 = float(x1)
        x2 = float(x2)
        y1 = float(y1)
        y2 = float(y2)
    except:
        return False

    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    try:
        test = temp[::-1]

        if(test == temp):
            return True
        else:
            return False

    except:
        return "Invalid"

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    try:
        float(num1)
        float(num2)
    except:
        print("Error! Only numbers and no division by zero!")
        return

    try:
        div = num1 / num2
    except ZeroDivisionError:
        print("Error! Only numbers and no division by zero!")
        return
    print("Your numbers divided is:", div)

## returns the squareroot of a particular number
def sq(num):
    try:
        return math.sqrt(num)
    except:
        return "Invalid"

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    first = str(first)
    middle = str(middle)
    last = str(last)

    isNumberFirst = any(map(str.isdigit, first))
    isNumberMiddle = any(map(str.isdigit, middle))
    isNumberLast = any(map(str.isdigit, last))
    
    if (isNumberFirst or isNumberMiddle or isNumberLast):
        print("Error! Names should only include letters.")        
    else:
        print("Hello!")
        print("Welcome to the program", first, middle, last)
        print("Glad to have you!")


## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    isList = isinstance(numbers, list)
    if (not isList):
        print("Error! Invalid")
    else:
        try:
            print("Your item at", index, "index is", numbers[index])
        except:
            print("Error! Invalid")

