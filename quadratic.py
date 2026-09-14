import os
import math

def clear():
    os.system("cls")

def is_float(x):
    try:
        float(x)
    except:
        return False
    return True
        

def get_equation():
    ans = input("Enter an equation (use ^ for exponents)\n")
    if ans:
        return ans
    print("Invalid.")
    return get_equation()

def get_type(a):
    if a.isalpa():
        return "letter"
    elif a.is_float():
        return "number"
    elif a == "+" or a == "-" or a == "^" or a == '/' or a == "*":
        return "symbol"
    else:
        return "none"
    

def parse_equation(eq):
    var = ""
    terms = []
    term = ""
    last_type = "none"

    for a in eq:
        ty = get_type(a)

        match ty:
            case "letter":
                if var == "":
                    var = a
                elif a == var:
                    pass
                else:
                    return False
            case "number" if last_type == "number":
                term += a
            case "number" if last_type != "number":
                # add old term to list and clear term varraible
                term

        
def calculate_quadratic():
    works = False
    while not works:
        terms = get_equation()
        parsed = parse_equation(terms)
        if parsed:
            works = True
        else:
            print("Invalid.")