import turtle
turtle.speed(10)
turtle.penup()                #kalemi kaldırıyor çizmiyor
turtle.goto(-200,200)         #başlangıç yerini değiştiriyorum    
turtle.pendown()              #kalemi başlaması gerek yerte götürfükten sonra indiriyor
for cc in range(8) :          #sekiz adet çiziyor
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50)
    turtle.left(90)

input()