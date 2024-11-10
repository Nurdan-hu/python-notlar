sayilar = [11,20,3]
def carp(xx):
    return xx*2

# b= []
# for a in sayilar:
#     b.append(carp(a))
# print(b)
yeniDizi = list(map(carp,sayilar))
print(yeniDizi)       #yukarıdakiyle aynı görevi görür
