import math

# return if a value is a float or not
def is_float(x):
    try:
        float(x)
    except:
        return False
    return True

# get a coordinate pair, with error handling
def get_coord(n):
    ans = input("Enter coordinate pair " + str(n) + ": ")

    x = "0"
    for i in range(len(ans)):
        char = ans[i]
        if is_float(x+char) and char != " ":
            x += char
        else:
            if x != "0":
                ans = ans[i+1:]
                break

    y = "0"
    for i in range(len(ans)):
        char = ans[i]
        if is_float(y+char) and char != " ":
            y += char
        else:
            if y != "0":
                break

    return [float(x), float(y)]

# calculate the distance and midpoint between 2 coordinate pairs
def calculate():
    pos1 = get_coord(1)
    pos2 = get_coord(2)

    dist = math.sqrt(((pos2[0]-pos1[0])**2) + ((pos2[1]-pos1[1])**2))

    print("\nDistance between points: ")
    print("("  + str(pos1[0]) + ", " + str(pos1[1]) + ") and ("  + str(pos2[0]) + ", " + str(pos2[1]) + ") is " + str(round(dist, 3)))

    mid_x = (pos1[0] + pos2[0]) / 2
    mid_y = (pos1[1] + pos2[1]) / 2

    print("\nMidpoint between them is (" + str(round(mid_x, 3)) + ", " + str(round(mid_y, 3)) + ")")

calculate()
