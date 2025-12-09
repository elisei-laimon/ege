# m=[]
# for n in range(1000000000,1789456123):
#     s = bin(n)[2:]
#     h = n % 4
# m.append(n + h)
# print(len(m))
from turtle import *

screensize(4000,4000)
size = 50
lt(90)
tracer(0)
down()
for i in range(0,7):
    fd(10*size)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        setpos(x*size,y*size)
        dot(5,'red')
done()

