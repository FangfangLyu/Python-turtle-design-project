from turtle import *
from random import randint

def jump(t,x,y):
    penup()
    goto(x,y)
    pendown()
    
def maple_leave(t,d):
    begin_fill()
    for times in range(5):
        fd(d)
        lt(45)
        fd(d/2)
        lt(90)
        fd(d/2)
        lt(45)
        fd(d)
        rt(36)
    end_fill()
    
def leave_rain(t,times):
    for times in range(20):
        x=randint(-800,800)
        y=randint(-400,400)
        size=randint(5,40)
        penup()
        goto(x,y)
        pendown()
        r=randint(238,255)
        g=randint(0,105)
        b=randint(0,105)
        color(r,g,b)
        maple_leave(t,40-times)



def leave_rain_f(t,times):
    for times in range(20):
        x=randint(-800,800)
        y=randint(-400,400)
        penup()
        goto(x,y)
        pendown()
        color('white')
        maple_leave(t,times)


def snow(t):
    size=randint(1,4)
    maple_leave(t,size)
        

def fff(t,f):
    for times in range(255):
        color(255-times,105,times)
        circle(times,times)
        fd(20)
        bk(40)
        rt(35)

        
