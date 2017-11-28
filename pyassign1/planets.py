#!/usr/bin/env python3


"""planets.py: Imatation of the six planets' movement.
__author__ = "WangTong"
__pkuid__  = "1700011771"
__email__  = "1700011771@pku.edu.cn"
"""


import turtle
import math


def prepare(i,T,a,b,Color,size):
    """To generate the planets;T[i]:turtles;a,b:list of axes of ovals
    """
    t=T[i]
    x1=a[i]*math.cos(math.pi/3*i)+6
    y1=b[i]*math.sin(math.pi/3*i)
    t.color('red')
    t.pu()
    t.speed(0)
    t.goto(x1,y1)
    t.pendown()
    t.color(Color[i])
    t.shape("circle")
    t.shapesize(size[i])


def draw_oval(i,T,a,b,speed):
    """To draw ovals; list of speed:planets' speed
    """
    for j in range(6):
        x=a[j]*math.cos(math.pi*(i/330*speed[j]+j/3))+6
        y=b[j]*math.sin(math.pi*(i/330*speed[j]+j/3))
        T[j].goto(x,y)


def main():
    """main module
    """
    wn=turtle.Screen()
    t0=turtle.Turtle()
    t1=turtle.Turtle()
    t2=turtle.Turtle()
    t3=turtle.Turtle()
    t4=turtle.Turtle()
    t5=turtle.Turtle()
    wn.bgcolor("black")
    t0.dot(110,"red")
    T=[t0,t1,t2,t3,t4,t5]
    Color=["lightpink","gold","blue","peru","red","gold"]
    a=[80,105,140,175,225,270]
    b=[64,98,117,160,208,248]
    size=[0.6,1.3,1.1,0.9,2.6,2.3]
    speed=[2,1.8,1.6,1.4,1.2,1]
    for i in range(6):
        prepare(i,T,a,b,Color,size)
    for i in range(1000):
        draw_oval(i,T,a,b,speed)
    wn.exitonclick()

    
if __name__=='__main__':
    main()
