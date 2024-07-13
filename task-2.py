import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def draw_koch_snowflake(order, size=300):

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    koch_snowflake(t, order, size)

    window.mainloop()


if __name__ == "__main__":
    try:
        order = int(input("Enter the recursion level for the Koch snowflake: "))
        draw_koch_snowflake(order)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the recursion level.")
