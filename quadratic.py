import math

def is_float(x):
    try:
        float(x)
    except:
        return False
    return True
        
def get_equation():
    ans = input("Enter an equation (use ^ for exponents)\n").split()
    if ans:
        return ans
    print("Invalid.")
    return get_equation()
    
def parse_equation(eq):
    var = ""

    for term in eq:
        for a in term:
            if a.isalpha():
                if var == "":
                    var = a
                elif a == var:
                    pass
                else:
                    return False
        
    if eq[1] == "^":
        if eq[2] != "2":
            return False
        del eq[1:3]

    if eq[1][0] == "^":
        if eq[1][1] != "2":
            return False
        del eq[1]

    if eq[0][-1] == "^":
        if eq[1] != '2':
            return False
        del eq[1]

    a = ""
    for i in range(len(eq[0]) - 1, -1, -1):
        char = eq[0][i]
        if is_float(a + char):
            a += char
        else:
            if a == "":
                a = "1"
            if is_float(a):
                a = float(a)
                break
            else:
                return False
    
    if eq[2][-1] != var:
        return False
    else:
        b = eq[2][:-1]
        if is_float(b):
            b = float(b)
        else:
            return False
    
    if eq[1] != "+" and eq[1] != "-":
        return False
    elif eq[1] == "-":
        b *= -1

    if is_float(eq[4]):
        c = float(eq[4])
    else:
        return False
    
    if eq[3] != "+" and eq[3] != "-":
        return False
    elif eq[3] == "-":
        c *= -1

    return [a, b, c]

def calculate_answer(a, b, c):
    try:
        ans1 = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)
        ans2 = (-b - math.sqrt((b**2) - (4*a*c))) / (2*a)
    except:
        return False
    return [round(ans1, 3), round(ans2, 3)]
        
def solve_quadrtic():
    works = False
    while not works:
        terms = get_equation()
        parsed = parse_equation(terms)
        if parsed:
            works = True
        else:
            print("Invalid.")

    ans = calculate_answer(parsed[0], parsed[1], parsed[2])

    if not ans:
        print("Problem has no solution.")
    elif ans[0] == ans[1]:
        print("Problem has one solution at:\n  " + str(ans[0]))
    else:
        print("Problem 2 solutions at:")
        print("  " + str(ans[0]))
        print("  " + str(ans[1]))
    
    print()

solve_quadrtic()