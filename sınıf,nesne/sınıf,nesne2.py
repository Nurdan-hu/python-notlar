class Ogrenci():
    adi= "--"
    ortalaması =50
print(Ogrenci)
print(Ogrenci.adi)
print(Ogrenci.ortalaması)

ogrenci1= Ogrenci()   #ogrenci1 nesne oluyor.
print(ogrenci1)
print(ogrenci1.adi)
print(ogrenci1.ortalaması)

ogrenci1.adi= "Nurdan SARI"
print(ogrenci1.adi)

ogrenci2 = Ogrenci()
print(ogrenci2.adi)
print(Ogrenci.adi)

ogrenci2.adi="Ömer AYBAK"
print(ogrenci2.adi)
print(ogrenci1.adi)