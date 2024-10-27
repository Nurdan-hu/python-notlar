# ogrenci1_sınav1= 60
# ogrenci1_sınav2= 90
# ogrenci1_ortalama= 75

# ogranci2_sınav1= 70
# ogrenci2_sınav2= 90
# ogrenci2_ortalama= 80

# okul_ortalaması = (ogrenci1_ortalama+ogrenci2_ortalama)/2
# print(okul_ortalaması)

class Ogrenci:
    adi = "Mustafa"
    soyadi = "ALP"
    numarasi = "547"
    class AldigiDersler:
        ders1 = "matematik"
        ders2 = "fizik"
    class SaglikDurumu:
        boy = 174
        kilo = 67
ogrenci1 = Ogrenci
ogrenci2 = Ogrenci

print("Öğrenci Bilgisi: ",Ogrenci.adi, Ogrenci.soyadi)
print("Öğrenci Bilgisi: ",ogrenci1.adi, ogrenci1.soyadi)
print("Öğrencinin aldığı dersler:",
     Ogrenci.AldigiDersler.ders1,
     Ogrenci.AldigiDersler.ders2) 
