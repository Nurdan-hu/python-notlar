sayac = 0
def biteneKadarHarca(para):
    global sayac
    sayac += 1
    harcanan = para * .1
    kalan = para - harcanan
    print("Paranız:",para,"Haracanan:",harcanan,"Kalan:",kalan)
    if kalan>10:biteneKadarHarca(kalan) #recursive fonksiyonlarda ne kadar çalışacağı belirtilmek zorundadır. Yoksa python yorumlayıcısı hafıza için bu işlemi sonlandırır.
biteneKadarHarca(10000)
print(f"Paranızdan {sayac} harcama sonunda 10 lira kaldı")

# def kalk(saat):
#     print(f"Saat {saat}, zamanında kalkıldı")
#     kalk(7)
# kalk(7)