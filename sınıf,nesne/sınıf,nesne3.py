class Ogrenci():      #kalıp
    adı= "--"
    ortalaması= 50

ogrenci1 = Ogrenci()
ogrenci1.adı = "Buse DOĞAN"
ogrenci1.ortalaması= 80

ogrenci2 = Ogrenci()
ogrenci2.adı = "Ebru GÜNDEŞ"
ogrenci2.ortalaması = 90

print(ogrenci2)
print(ogrenci2.adı)
print(ogrenci2.ortalaması)



class Ogretmen():
    adı= "girilmedi"
    soyadı= "girilmedi"
    branşı="girilmedi"
    telno="girilmedi"

ogretmen1= Ogretmen()
ogretmen1.adı= "Davut"
ogretmen1.soyadı= "AKSOY"
ogretmen1.branşı = "Matematik öğretmeni"
ogretmen1.telno= 5053032343
print(ogretmen1.adı, ogretmen1.soyadı)
print(ogretmen1.branşı)
print(ogretmen1.telno)

ogretmen2= Ogretmen()
ogretmen2.adı= "Meryem"
ogretmen2.soyadı= "ÇETE"
ogretmen2.branşı = "Fen Bilimleri Öğretmeni"
ogretmen2.telno= 5553409320
print(ogretmen2.adı,ogretmen2.soyadı )
print(ogretmen2.branşı)
print(ogretmen2.telno)