class İlan():
    fiyat = "Tanımsız"
    ilanNo= "Yok"
    adres= "Girilmedi"
    ilanTarihi= "Henüz Girilmedi"
    def __init__(ilan,fiyatı=  fiyat,numarası= ilanNo, adresi= adres, Tarih= ilanTarihi):
        ilan.fiyat= fiyatı
        ilan.ilanNo= numarası
        ilan.adres= adresi
        ilan.ilanTarihi= Tarih

ilan1= İlan("Ücretsiz Sahiplendirme","452","Çankaya/Ankara","10.11.2024")
print(ilan1)
print(f"Fiyat:{ilan1.fiyat}\nİlan Numarası:{ilan1.ilanNo}\nAdres:{ilan1.adres}\nİlan Tarihi:{ilan1.ilanTarihi}")

class Hayvan(İlan):  #ilan sınıfını getirdik buraya
    tür= "Girilmedi"
    cins= "Bilinmiyor"
    yas= "Yok"
    cinsiyet= "Henüz Girilmedi"
    def __init__(hayvan,türü= tür, cinsi= cins, yası= yas, cinsiyeti= cinsiyet):
        hayvan.tür = türü
        hayvan.cins= cinsi
        hayvan.yas= yası
        hayvan.cinsiyet= cinsiyeti
sh1= Hayvan("Kedi","Van Kedisi","7 Aylık","Dişi")
print(f"Hayvanın:\nTürü:{sh1.tür}\nCinsi:{sh1.cins}\nYaşı:{sh1.yas}\nCinsiyeti:{sh1.cinsiyet}")




class Otomobil(İlan):
    marka= "Girilmedi"
    seri= "Yok"
    model= "Bilinmiyor"
    km= "Henüz Girilmedi"
    def __init__(araç,markası= marka,serisi= seri,modeli=model,kmsi= km):
        araç.marka= markası
        araç.model= modeli
        araç.seri= serisi
        araç.km= kmsi
araç1= Otomobil("Honda","Civic","1.6i VTEC Eco Elegance","100.000")
print(f"Aracın:\nMarkası:{araç1.marka}\nModeli:{araç1.model}\nSerisi:{araç1.seri}\nKilometresi:{araç1.km}")

class Emlak(İlan):
    odasayısı="Girilmedi"
    binayasi= "Yok"
    bulunduğukat= "Bilinmiyor"
    katsayısı= "Henüz Girilmedi"
    def __init__(ev,ossi= odasayısı,bysi= binayasi,bksi= bulunduğukat,kssi=katsayısı):
        ev.odasayısı= ossi
        ev.binayasi= bysi
        ev.bulunduğukat= bksi
        ev.katsayısı= kssi

ev1= Emlak("4+1","3 yıl","14","16")
print(f"Evin:\nOda Sayısı:{ev1.odasayısı}\nBinanın Yaşı:{ev1.binayasi}\nBulunduğu Kat:{ev1.bulunduğukat}\nKat Sayısı:{ev1.katsayısı}")