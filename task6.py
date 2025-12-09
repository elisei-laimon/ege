from turtle import *

screensize(4000,4000)
size = 50
lt(90)
tracer(0)
down()
for i in range(0,12):
    rt(60)
    fd(1*size)
    rt(60)
    fd(1*size)
    rt(270)
up()
for x in range(-50,50):
    for y in range(-50,50):
        setpos(x*size, y*size)
        dot(4,'red')
done()
answer:38