class BankaKasasi():
    __KasadaKalanMiktar= 0  #kapsüllenmiş bilgi
class BankaMusterisi():
    adiSoyadi= "----"
    hesapNo= "Tanımlanmamıştır"
    __kalanParasi= 0

kasa1= BankaKasasi
kasa1.__KasadaKalanMiktar= 50000

musteri1= BankaMusterisi()
musteri1.adiSoyadi= "Nurdan KARA"
musteri1.hesapNo= "3483940239"
musteri1.__kalanParasi = 5000

print(f"\n\nBanka Kasasında Kalan Para Miktarı: {kasa1.__KasadaKalanMiktar}")
print(f"\n\nMüşteri Bilgileri:\n\
      Adı:\t {musteri1.adiSoyadi}\n\
      Hesap Numarası:\t {musteri1.hesapNo}\n\
      Kalan Parası: \t {musteri1.__kalanParasi}")