#!/usr/local/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for stap in range(15):
    write(stap, align='center')
    right(90)
    forward(10)
    pendown()
    for dot in range(5):
        pendown()
        forward(20)
        penup()
        forward(10)
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

cor = Turtle()
cor.color('green')
cor.shape('turtle')

cor.penup()
cor.goto(-160, 40)
cor.pendown()

dan = Turtle()
dan.color('yellow')
dan.shape('turtle')

dan.penup()
dan.goto(-160, 10)
dan.pendown()

for draai in range(10):
    ada.right(36)
    bob.right(36)
    cor.right(36)
    dan.right(36)

for draai in range(100):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    cor.forward(randint(1, 5))
    dan.forward(randint(1, 5))

exitonclick()