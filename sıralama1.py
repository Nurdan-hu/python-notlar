# meyveler = ["Muz","Dut","Nar","Elma","Armut","Kiraz"]
# print(meyveler)

# meyveler.sort()     #alfabetik sıralama
# print(meyveler)    

# meyveler.sort(reverse=True)   #tersten alfabetik sıralama
# print(meyveler)

# if "Karpuz" in meyveler: print("var")
# else: print("yok")

import random
sayilar = []
max = 1000000
for a in range(max):
    sayilar.append(random.randint(1,max))
print(sayilar)

print("SIRALAMA İŞLEMİ BAŞLADI")
sayilar.sort()
print(sayilar)
