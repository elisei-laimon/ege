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
# # 48384
# # список удовлетворяющих результатов
# result = []
# # перебираем все возможные x и y
# for x in "012345678":
#     for y in "012345678":
#         # вычисляем арифметическое выражение в 10 СС
#         r = int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)
#         # проверяем условие по задаче
#         if r % 61 == 0:
#             # если результат удовлетворяет, то добавляем в список результатов
#             result.append(r // 61)
#
# # выводим наименьший результат
# print(min(result))

