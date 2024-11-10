print((lambda x:x**2)(5)) #Lambda satır içi basit fonksiyon demek

karesi = lambda n:n**2
print (karesi(4))

sayilar = [11,22,3]
def carp(xx): 
    return xx*2
yeniDizi = list(map(carp,sayilar))
print(yeniDizi)

sayilar = [11,22,3]
print(list(map(lambda a:a*2,sayilar)))