import turtle
from turtle import *
from line_functions import *
from random import randint
turtle.colormode(255)

speed(0)
bgcolor('black')

pensize(2)
jump(turtle,0,0)
r1=0
g1=15
b1=28
for times in range(50):
    b1+=1
    c=(r1,g1,b1)
    color(c)
    star(turtle,400-times,45)
    fd(2)
    right(2)


pensize(1)
for times in range(200):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    color(r,g,b)
    x=randint(-350,370)
    y=randint(-180,180)
    size=randint(4,15)
    jump(turtle,x,y)
    square(turtle,size)
    x2=randint(-800,800)
    y2=randint(-400,400)
    jump(turtle,x2,y2)
    begin_fill()
    square(turtle,size)
    end_fill()
    jump(turtle,x,y)
    color(r,g,b)
    starsize=randint(10,35)
    begin_fill()
    star(turtle,starsize,35)
    end_fill()


done()

















        
