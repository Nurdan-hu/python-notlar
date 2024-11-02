# open("deneme","w")  ismi deneme olan bir dosya oluşturur.,

# for a in range(5):
#     open (f"deneme{a}","w") #deneme,deneme0,deneme1... diye dosyalar oluşturu

open(f"rehber.txt","w")
open(f"rehber.txt","w").write("Bu dosyada Ayşe Nurdan ANKARALI'NIN geçen seneki ders notları yazmaktadır.")
open(f"rehber.txt","a").write("Matematik:90") #write veri ekleme için kullanılır.
