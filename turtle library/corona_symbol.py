from turtle import *

co = Turtle()
s=Screen()
co.speed(0)
s.bgcolor("black")
co.pensize(4)

#virus center
co.color("green","green")
co.begin_fill()
co.up()
co.setpos(0,-100)
co.down()
co.circle(120)
co.end_fill()

#virus bumps method
def bumps(x,y):
    co.up()
    co.setpos(x,y)
    co.down()
    co.fd(30)
    co.rt(90)
    co.fd(10)
    co.lt(90)
    co.fd(10)
    co.lt(90)
    co.fd(30)
    co.lt(90)
    co.fd(10)
    co.lt(90)
    co.fd(10)
    co.rt(90)
    co.fd(30)

#calls a bumps method
bumps(120,0)
bumps(-120,0)
co.lt(90)
bumps(0,140)
bumps(0,-100)
co.lt(-45)
bumps(96,96)
bumps(-76,-76)
co.lt(110)
bumps(-96,96)
bumps(76,-76)

#virus eyes
#left eye
co.up()
co.setpos(90,50)
co.down()
co.lt(293)
co.color("black","white")
co.begin_fill()
co.circle(35,-180)
co.end_fill()

#right eye
co.up()
co.setpos(-90,50)
co.down()
co.color("black","white")
co.begin_fill()
co.circle(35,180)
co.end_fill()

#virus mouth
co.up()
co.setpos(35,-70)
co.down()
co.color("white","white")
co.begin_fill()
co.circle(35,180)
co.end_fill()

co.ht()
done()