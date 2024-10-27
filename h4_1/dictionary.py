# ogrenciler = ["Sude Akyol","Rahime Kara"]
# ortalamalar = [79,89]
# ogrenciOrtalamaları= {
#     "adı1": "Sude Akyol", "ortalaması1": 80,
#     "adı2": "Rahime Kara", "ortalaması2": 90}
# print(ogrenciOrtalamaları)["adı1"],ogrenciOrtalamaları["ortalaması1"]

ogrenciOrtalamaları= {
    "25463493090": {"adı":"Sude Akyol", "ortalaması": 80},
    "54948549210": {"adı":"Rahime Kara", "ortalaması": 90}}
aranacak = input("Hangi öğrenci bilgileri?")
print(ogrenciOrtalamaları[aranacak]["adı"])