import math

# get a float value from user, including error handling
def get_float(msg, fail = "Invalid."):
    try:
        ans = float(input(msg))
    except Exception as e:
        print(fail)
        return get_float(msg, fail)
    return ans
        
# get the equation from the user, return it if not empty
def get_equation():
    print("Enter the a, b, and c values of the quadratic equation (ax^2 + bx + c)")
    a = get_float("Enter 'a' value: ")
    b = get_float("Enter 'b' value: ")
    c = get_float("Enter 'c' value: ")
    return [a, b, c]


# calcualte the zeros of the equation given abc values
def calculate_answer(a, b, c):
    try:
        ans1 = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)
        ans2 = (-b - math.sqrt((b**2) - (4*a*c))) / (2*a)
    except:
        return False
    return [round(ans1, 3), round(ans2, 3)]

# get a valid equation, then parse, solve, and display it    
def solve_quadrtic():
    [a, b, c] = get_equation()
    ans = calculate_answer(a, b, c)

    if not ans:
        print("Problem has no solution.")
    elif ans[0] == ans[1]:
        print("Problem has one solution at:\n  " + str(ans[0]))
    else:
        print("Problem 2 solutions at:")
        print("  " + str(ans[0]))
        print("  " + str(ans[1]))

solve_quadrtic()