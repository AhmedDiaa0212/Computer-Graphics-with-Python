from turtle import *

fl = Turtle()
s = Screen()
fl.speed("fastest")
s.bgcolor("black")
fl.pensize(4)

#flower stalk
fl.color("green")
fl.rt(90)
fl.circle(300,90)
fl.up()
fl.setpos(-53,-260)
fl.down()
fl.circle(100,90)

#Input number of petals
num_petals=int(s.numinput("flower petals", "please enter number of the petals to draw a flower :      \
    \r Note: The best flower shape has thirteen petals "))

#flower petals
fl.lt(270)
fl.up()
fl.setpos(0,0)
fl.down()
for i in range(num_petals):
        fl.color("maroon","navajo white")
        fl.begin_fill()
        fl.lt(30)
        fl.fd(100)   
        for j in range(58):
            fl.fd(4)
            fl.lt(4)
        fl.lt(8)
        fl.fd(107)
        fl.lt(120)
        fl.end_fill()

#flower center
fl.dot(68,"maroon")
fl.dot(63,"coral")

fl.ht()
done()