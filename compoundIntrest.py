# get a float value from user, including error handling
def get_float(msg, fail = "Invalid."):
    try:
        ans = float(input(msg))
    except Exception as e:
        print(fail)
        return get_float(msg, fail)
    return ans

# get account data from user and return it
def get_inputs():
    p = get_float("Starting amount in account: ")
    r = get_float("Annual intrest as decimal: ")
    n = get_float("Times compounded per year: ")
    t = get_float("Number of years: ")
    return [p, r, n, t]

# calculate intrest using instrest formula
def calculate_intrest():
    [p, r, n, t] = get_inputs()

    amount = p * ((1+ (r/n))**(n*t))

    print("Expected intrest: " + str(round(amount, 2)))

calculate_intrest()