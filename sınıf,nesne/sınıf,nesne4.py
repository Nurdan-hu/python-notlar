class Calısan:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim 
        self.soyisim = soyisim
        self.yas = yas
    def show_info(self):
            print(f"Ad:{self.isim}   Soyad:{self.soyisim}    Yaş:{self.yas} ")

calısan1 = Calısan("Ali","DOĞAN", 20)
print(calısan1.isim, calısan1.soyisim, calısan1.yas)

calısan2 = Calısan("Nurdan", "ANKARALI", 15)
print(calısan2.isim, calısan2.soyisim, calısan2.yas)
#veya daha kolayı:
calısan1.show_info()
