import turtle as t
import random as r

t.speed()
renkler = ["olive","tomato","red","blue","purple"]
for b in range (9):
    t.color(r.choice(renkler))

    t.penup()

    t.goto(r.randint(-200,200), r.randint(-200,200))
    t.pendown()
    kenar = r.randint(-100,100)
    for a in range(4):
        t.forward(kenar)
        t.right(90)

input()