class Ogrenci(): #büyük veri tipi
    ad = "tanımlanmamıştır"
    tc=  "tanımlanmamıştır"
    ortalamasi= 0

print(Ogrenci.ad)
print(type(Ogrenci.ad))

ogrenci1= Ogrenci()
print(type(ogrenci1.ad))
print(ogrenci1.ad)
ogrenci1.ad= "M. Ali"
print(ogrenci1.ad)

print(Ogrenci)