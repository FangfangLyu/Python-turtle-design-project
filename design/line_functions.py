from turtle import *
from random import randint

def jump(t,x,y):
    penup()
    goto(x,y)
    pendown()
def background(t):
    forward(800)
    left(90)
    forward(400)
    left(90)
    forward(800)
    left(90)
    forward(400)

def square(t,d):
    for times in range(4):
        fd(d)
        rt(90)
def star(t,d,a):
    rt(a)
    for times in range(5):
        fd(d)
        rt(144)
