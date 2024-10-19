import turtle
#turtle.circle(100) #yarıçapı 100 piksel olan bir daire çizer.
#turtle.circle(100,90)  #yarıçapı 100piksel olan bir daire çizdikten sonra fareyi 90derece ileriye götürür.
#turtle.circle(100, steps = 6) #altıgen çizer ancak bir önce çizdiği dairenin içinde olur.
#turtle.reset()   #bir öncekileri çizdikten sonra siler ve devam eder.
#turtle.circle(100, steps= 6)  #altıgen çizer ancak daire sıfırlandığı için sadece altıgen görünür.
#turtle.reset()


#turtle.speed(100)
#for i in range(100):
    #if i % 2== 0:
        #turtle.color("blue","green")
        #turtle.circle(i)
    #else :
        #turtle.color("red","yellow")     #mavi, üst üste çizilmiş yarıçapları birbirinden farklı 100 adet daire çizer.
turtle.speed(10)
for i in range(100):
    if i % 2 == 0:
        turtle.color("blue")
        turtle.circle(i)
    elif i% 5 == 0:
        turtle.color("green")
        turtle.circle(i)
    else :
        turtle.color("red")
        turtle.circle(i)






input()