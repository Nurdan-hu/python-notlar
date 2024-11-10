urunler = [
    ["Kurşun Kalem",40],
    ["Tükenmez Kalem",30],
    ["Renkli Kağıt",150],
]
kdvOrani = 10
# urunlerKDVli= []
# def kdvEkle(oran):
#     for u in urunler:
#         yeniUrun = [u[0],oran*100/u[1]*1.10]
#         urunlerKDVli.append(yeniUrun)
urunlerKDVli = list(map(lambda x: [x[0],x[1]+kdvOrani],urunler))
# kdvEkle(kdvOrani)
print(urunler)
print(urunlerKDVli)
