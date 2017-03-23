#Fangfang Lyu
#design project


import turtle
from turtle import*
from functions import *
from random import randint
colormode(255)
speed(0)
bgcolor('black')


jump(turtle,0,0)
x=255
for times in range(255):
    color(255-x,105,x)
    circle(times,x)
    fd(10)
    bk(40)
    rt(35)
    x-=1

jump(turtle,0,0)
y=255
for times in range(255):
    color(255-y,105,y)
    circle(times,y)
    fd(20)
    bk(40)
    rt(35)
    y-=1

jump(turtle,0,0)
for times in range(50):
    color('white')
    x=randint(-800,800)
    y=randint(-400,400)
    snow(turtle)
    jump(turtle,x,y)

leave_rain(turtle,25)


leave_rain_f(turtle,25)



done()
