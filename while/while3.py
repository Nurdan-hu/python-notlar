x = " "
while x != "":
    x = int(input("Bir tam sayı giriniz:"))
    if x > 0:
        print("Pozitif sayıdır.")
    elif x < 0:
        print("Negatif sayıdır.")
    else:
        print("Sıfıra eşittir.")