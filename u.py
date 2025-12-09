from turtle import *

screensize(4000,4000)
size = 50
lt(90)
tracer(0)
down()
for i in range(0,4):
    fd(9*size)
    rt(90)
for h in range(0,3):
    fd(9 * size)
    rt(120)
up()
for x in range(-50,50):
    for y in range(-50,50):
        setpos(x*size, y*size)
        dot(4,'red')
done()
#answer:34