from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# W = Forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    tim.rt(5)

def turn_left():
    new_heading=tim.heading() + 5
    tim.setheading(new_heading)

def move_clockwise():
    tim.circle(50)

def clear_window():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_window)
screen.exitonclick()
