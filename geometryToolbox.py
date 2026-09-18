import os
import math

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_float(msg, fail = "Invalid."):
    try:
        ans = float(input(msg))
    except Exception as e:
        print(fail)
        return get_float(msg, fail)
    return ans

def get_int(msg, fail = "Invalid."):
    try:
        ans = int(input(msg))
    except Exception as e:
        print(fail)
        return get_int(msg, fail)
    return ans

class Shape:
    name = "NONE"

    def callback(self):
        print("UNASSIGNED")

class Circle(Shape):
    name = "Circle"

    def callback(self):
        r = self.get_radius()
        self.display_info(r)

    def get_radius():
        return get_float("Enter radius: ")
    
    def display_info(r):
        area = math.pi * (r*r)
        cir = 2 * math.pi * r

        print("Area is " + str(round(area, 2)))
        print("Circumference is " + str(round(cir, 2)))

class Triangle(Shape):
    name = "Triangle"

    def callback(self):
        ans = get_float("Enter base (-1 to swtich to using side lenghts): ")

        if ans >= 0:
            self.calc_from_base(ans)
        else:
            self.calc_from_sides(self)
            

    def calc_from_base(base):
        height = get_float("Enter height: ")
        area = base * height / 2

        print("Area is " + str(round(area, 2)))

    def calc_from_sides(self):
        a = get_float('Side 1 length: ')
        b = get_float('Side 2 length: ')
        c = get_float('Side 3 length: ')

        max_side = max(a, max(b, c))

        if a + b + c - max_side < max_side:
            print("Invalid Side lengths.")
            self.calc_from_sides(self)
            return
        
        s = (a + b + c) / 2
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))

        print("Area is " + str(round(area, 2)))

class Trapezoid(Shape):
    name = "Trapezoid"

    def callback(self):
        self.display_area(self.get_inputs())
        
    def get_inputs():
        b1 = get_float("Enter base length: ")
        b2 = get_float("Enter second base length: ")
        h = get_float("Enter height: ")

        return [b1, b2, h]
    
    def display_area(inputs):
        [b1, b2, h] = inputs
        area = ((b1 + b2) * h) / 2

        print("Area is " + str(round(area, 2)))

class Regular_Polygon(Shape):
    name = "Regular Polygon"

    def callback(self):
        n = get_int("Enter number of sides: ")
        s = get_float("Enter side lenght: ")

        a = s / (2 * math.tan(math.radians(180.0/n)))
        area = (1/2) * a * s * n

        print("\nA " + str(n) + " sided Regular Polygon of side length " + str(round(s, 2)))
        print(" has area " + str(round(area, 2)))
        

class Menu:
    shapes = []
    selected = 0

    def display(self):
        clear()
        print("  Choose Shape")
        print("----------------")
        print("enter to change selection")
        print("'s' to select, 'q' to quit\n")
        
        for i in range(len(self.shapes)):
            shape = self.shapes[i]
            if i == self.selected:
                print(shape.name.upper())
            else:
                print(shape.name)

    def add_shape(self, shape):
        self.shapes.append(shape)

    def  cycle_menu(self):
        self.selected = (self.selected + 1) % len(self.shapes)

    def select_shape(self):
        clear()
        
        shape = self.shapes[self.selected]
        
        print("Shape: " + shape.name + '\n')

        shape.callback(shape)

def init_menu(menu):
    menu.add_shape(Circle)
    menu.add_shape(Triangle)
    menu.add_shape(Trapezoid)
    menu.add_shape(Regular_Polygon)
    
def main_loop():
    run = True
    menu = Menu()

    init_menu(menu)

    while run:
        
        menu.display()
        
        user_in = input()
        if user_in.lower() == 's':
            menu.select_shape()
            input("\nEnter to return\n")
            menu.selected = 0
        elif user_in.lower() == 'q':
            print("Program Quit")
            return
        else:
            menu.cycle_menu()

main_loop()