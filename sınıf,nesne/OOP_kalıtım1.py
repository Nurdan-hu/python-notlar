class Personel():
    sicilNo= "--"
    adiSoyadi= "Tanımsız"
class İdareci(Personel):
    İdariGorev= "Girilmemiştir"
class KatPersonel(Personel):
    gorevliOlduğuKat= 4
class Veli():
    ogrencisininAdi= "Henüz girilmemiştir"
class CokluYetkiliPersonel(İdareci,Veli):              #hem yetkili hem veli
    pass

personel1= İdareci()
print(personel1.sicilNo)         #-- yazar

personel2= CokluYetkiliPersonel()
print("İdari Görevi:",personel2.İdariGorev,"\nÖğrenci Adı:",personel2.ogrencisininAdi)