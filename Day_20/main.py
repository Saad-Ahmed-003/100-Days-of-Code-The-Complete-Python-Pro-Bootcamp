import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen .setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for i in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(i)
    segments.append(new_segment)

game_is_on = Turtle

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)


