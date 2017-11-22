import turtle
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
orbit=[80,105,140,175,225,270]
b=[64,98,117,160,208,248]
size=[0.6,1.3,1.1,0.9,2.6,2.3]
p=6
import math
for i in range(6):
    t=T[i]
    t.color("red")
    t.speed(0)
    r1=orbit[i]
    r2=b[i]
    x1=r1*math.cos(math.pi/3*i)+p
    y1=r2*math.sin(math.pi/3*i)
    t.pu()
    t.goto(x1,y1)
    t.pendown()
    t.color(Color[i])
    t.shape("circle")
    t.shapesize(size[i])
for i1 in range(1201):
        t0.goto(p+80*math.cos(math.pi/330*i1*2),64*math.sin(math.pi/330*i1*2))
        t1.goto(p+105*math.cos(math.pi/330*i1*1.8+math.pi/3),98*math.sin(math.pi/330*i1*1.8+math.pi/3))
        t2.goto(p+140*math.cos(math.pi/330*i1*1.6+math.pi/3*2),117*math.sin(math.pi/330*i1*1.6+math.pi/3*2))
        t3.goto(p+175*math.cos(math.pi/330*i1*1.4+math.pi/3*3),160*math.sin(math.pi/330*i1*1.4+math.pi/3*3))
        t4.goto(p+225*math.cos(math.pi/330*i1*1.2+math.pi/3*4),208*math.sin(math.pi/330*i1*1.2+math.pi/3*4))
        t5.goto(p+270*math.cos(math.pi/330*i1+math.pi/3*5),248*math.sin(math.pi/330*i1+math.pi/3*5))
wn.exitonclick()
