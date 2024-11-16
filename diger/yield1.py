#RETURN İLE DEĞER DÖNDÜRME
# meyveler = ["elma","muz","dut"]

# def xxx (aa):
#     for b in aa:
#         return b
# sonuc = xxx(meyveler)
# print(sonuc)

#RETURN YERİNE YİELD İLE DEĞER ÜRETME

meyveler = ["elma","muz","dut"]

def xxx (aa):
    for b in aa:
        yield b
        
sonuc = xxx(meyveler)
print(sonuc)
print(next(sonuc))
print(next(sonuc))