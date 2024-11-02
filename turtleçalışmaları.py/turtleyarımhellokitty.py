import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_hello_kitty():
    # Baş
    draw_circle("white", 100, 0, 0)

    # Kulaklar
    draw_circle("white", 40, -70, 70)  # Sol kulak
    draw_circle("white", 40, 70, 70)   # Sağ kulak
    draw_circle("pink", 30, -70, 80)   # Sol kulak içi
    draw_circle("pink", 30, 70, 80)    # Sağ kulak içi

    # Gözler
    draw_circle("black", 10, -35, 30)  # Sol göz
    draw_circle("black", 10, 35, 30)   # Sağ göz
    draw_circle("white", 5, -35, 35)    # Sol göz beyazı
    draw_circle("white", 5, 35, 35)     # Sağ göz beyazı

    # Burun
    draw_circle("yellow", 8, 0, 20)

    # Ağız
    turtle.penup()
    turtle.goto(-20, 10)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(20, 120)

    # Bıyıklar
    turtle.penup()
    turtle.goto(-40, 0)
    turtle.pendown()
    turtle.goto(-20, 0)
    turtle.penup()
    turtle.goto(-40, -10)
    turtle.pendown()
    turtle.goto(-20, -10)
    turtle.penup()
    turtle.goto(-40, -20)
    turtle.pendown()
    turtle.goto(-20, -20)

    turtle.hideturtle()
    turtle.done()

# Turtle ayarları
turtle.speed(3)
draw_hello_kitty()
