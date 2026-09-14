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
        

def get_terms():
    ans = input("Enter an equation (use ^ for exponents)\n").split()
    if ans:
        return ans
    print("Invalid.")
    return get_terms()

def parse_equation(terms):
    for i in range(len(terms)):
        if is_float(terms[i]):
            terms[i] = float(term)