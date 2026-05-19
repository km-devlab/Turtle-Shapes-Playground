# ==========================================
# PYTHON TURTLE SHAPES PLAYGROUND
# ==========================================

import turtle

# ------------------------------------------
# SCREEN SETUP
# ------------------------------------------

screen = turtle.Screen()
screen.title("Turtle Shapes Playground")
screen.bgcolor("white")

# Create turtle object
pen = turtle.Turtle()

# Speed:
# 1 = slow
# 10 = fast
# 0 = fastest
pen.speed(3)

# Pen thickness
pen.pensize(3)

# ------------------------------------------
# FUNCTION 1 : DRAW A LINE
# ------------------------------------------

def draw_line():
    pen.clear()
    pen.penup()
    pen.goto(-100, 0)
    pen.pendown()

    pen.forward(200)

# ------------------------------------------
# FUNCTION 2 : DRAW A SQUARE
# ------------------------------------------

def draw_square():
    pen.clear()

    for i in range(4):
        pen.forward(100)
        pen.right(90)

# ------------------------------------------
# FUNCTION 3 : DRAW A TRIANGLE
# ------------------------------------------

def draw_triangle():
    pen.clear()

    for i in range(3):
        pen.forward(120)
        pen.left(120)

# ------------------------------------------
# FUNCTION 4 : DRAW A RECTANGLE
# ------------------------------------------

def draw_rectangle():
    pen.clear()

    for i in range(2):
        pen.forward(150)
        pen.right(90)

        pen.forward(80)
        pen.right(90)

# ------------------------------------------
# FUNCTION 5 : DRAW A CIRCLE
# ------------------------------------------

def draw_circle():
    pen.clear()

    pen.circle(100)

# ------------------------------------------
# FUNCTION 6 : DRAW A STAR
# ------------------------------------------

def draw_star():
    pen.clear()

    for i in range(5):
        pen.forward(200)
        pen.right(144)

# ------------------------------------------
# FUNCTION 7 : DRAW A HEXAGON
# ------------------------------------------

def draw_hexagon():
    pen.clear()

    for i in range(6):
        pen.forward(100)
        pen.right(60)

# ------------------------------------------
# FUNCTION 8 : FILLED SHAPE
# ------------------------------------------

def draw_filled_square():
    pen.clear()

    pen.fillcolor("yellow")

    pen.begin_fill()

    for i in range(4):
        pen.forward(100)
        pen.right(90)

    pen.end_fill()

# ------------------------------------------
# FUNCTION 9 : SPIRAL DESIGN
# ------------------------------------------

def draw_spiral():
    pen.clear()

    for i in range(50):
        pen.forward(i * 5)
        pen.right(91)

# ------------------------------------------
# FUNCTION 10 : FLOWER DESIGN
# ------------------------------------------

def draw_flower():
    pen.clear()

    for i in range(36):
        pen.circle(100)
        pen.right(10)

# ------------------------------------------
# MAIN MENU
# ------------------------------------------

print("\n===== TURTLE SHAPES PLAYGROUND =====")
print("1  - Line")
print("2  - Square")
print("3  - Triangle")
print("4  - Rectangle")
print("5  - Circle")
print("6  - Star")
print("7  - Hexagon")
print("8  - Filled Square")
print("9  - Spiral")
print("10 - Flower")

choice = input("\nEnter your choice: ")

# ------------------------------------------
# CALL FUNCTIONS BASED ON USER INPUT
# ------------------------------------------

if choice == "1":
    draw_line()

elif choice == "2":
    draw_square()

elif choice == "3":
    draw_triangle()

elif choice == "4":
    draw_rectangle()

elif choice == "5":
    draw_circle()

elif choice == "6":
    draw_star()

elif choice == "7":
    draw_hexagon()

elif choice == "8":
    draw_filled_square()

elif choice == "9":
    draw_spiral()

elif choice == "10":
    draw_flower()

else:
    print("Invalid choice")

# Keep window open
turtle.done()
