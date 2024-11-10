sayilar= [11,20,3,6,7]  #listedeki şartı sağlayanları alıp yeni bir liste oluşturuyor.
print(sayilar)

# def tekMi(xx):
#     return  xx%2==1
# yeniDizi = list(filter(lambda x: True, sayilar))
yeniDizi= list(filter(lambda x: x%2==1,sayilar))
# yeniDizi = list(filter(tekMi,sayilar))
print(yeniDizi)