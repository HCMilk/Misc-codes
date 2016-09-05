# calculator.py


import sys

def add(lhs, rhs): 
    return lhs + rhs 

def subtract(lhs, rhs):
    return lhs - rhs

def multiply(lhs, rhs):
    result = 0
    if lhs == 0 or rhs == 0:
        return result
    for i in range(abs(rhs)):
        result += lhs
    if rhs < 0:
        return -result
    return result
  
def divide(numerator, denominator):
    if denominator == 0:
        print "Error: the denominator cannot be 0"
        return ZeroDivisionError
    else:
        result = 0
        abs_numerator = abs(numerator)
        abs_denominator = abs(denominator)
        while abs_numerator >= abs_denominator:
            result += 1
            abs_numerator -= abs_denominator
        if bool(numerator < 0) != bool(denominator < 0):
            return -result
        return result
 
def power(num, raised_to):
    if raised_to == 0:    
        return 1
    result = num
    for i in range(raised_to - 1): 
        result = multiply(result, num)    
    return result
    
def calculation(lhs, operator, rhs):
    if operator == "+":
        print "Result: ", add(lhs, rhs)
    elif operator == "-":
        print "Result: ",  subtract(lhs, rhs)
    elif operator == "*":
        print "Result: ",  multiply(lhs, rhs)
    elif operator == "/":
        if rhs == 0:
            divide(lhs, rhs)
        else:
            print "Result: ", divide(lhs, rhs)
    elif operator == "^":
        print "Result: ",  power(lhs, rhs)
    else:
        print "Invalid input please try again!"
        
while True:
    print "Enter a number, [space] an operator (+, -, * , /, ^) [space], and another number OR control+d to EXIT: "
    str = sys.stdin.readline().strip("\n")
    if not str: break 
    list = str.split(" ")
    if len(list) != 3:
        print "Invalid input please try again!"
        continue
    if list[0].lstrip("-+").isdigit() and list [2].lstrip("-+").isdigit():
        lhs = int(list[0])
        rhs = int(list[2])
        calculation(lhs, list[1], rhs)
        continue       
    else:
        print "Invalid input please try again!"
        continue
