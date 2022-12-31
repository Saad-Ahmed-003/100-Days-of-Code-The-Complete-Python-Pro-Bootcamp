from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


screen.listen()
screen.onkey(key="d", fun=move_forward)
screen.onkey(key="a", fun=move_backward)
screen.onkey(key="s", fun=move_right)
screen.onkey(key="w", fun=move_left)

screen.exitonclick()
