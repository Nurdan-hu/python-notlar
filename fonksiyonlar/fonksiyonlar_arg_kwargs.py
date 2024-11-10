# def selamla(gelen): 
#     gelen.append("Nur") yazarsak Nur'u gelen'e ekler.
#     print(gelen)
#     for a in gelen:
#         print("Merhaba", a)

# ogrenciler= ["Ali","Can","Cem"]
# selamla(ogrenciler)

def selamla(*gelen):   #yıldız koymazsak hata verir
    print(gelen)       #("Ali","Can","Cem")'yi yazar. Tuple türü fonksiyon olduğu için append kullanarak bir şey ekleyemeyiz.
    for a in gelen:
        print("Merhaba", a)

selamla("Ali","Can","Cem")