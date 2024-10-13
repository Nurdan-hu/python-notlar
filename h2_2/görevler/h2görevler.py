#Sayının 100den büyük olduğunu bilen uygulama
#print("Bu program girilen sayının 100'den büyük olup olmadığını hesaplar.")
#sayı = int(input('Sayı giriniz:'))
#if sayı > 100 : print("Bu sayı 100'den büyüktür.")
#if sayı < 100 : print("Bu sayı 100'den küçüktür.")



#nasılsın diye soran uygulama
ad =input("İsmin ne?")
print(f'Nasılsın {ad}?')
cevap = input()
if cevap == 'iyiyim' or cevap == 'iyi' or cevap == 'fena değil':
    print('Allah iyilik versin.')
    
if cevap in ['kötü', 'kötüyüm', 'çok kötüyüm', 'kendimi iyi hissetmiyorum']:
    print('Sebebi nedir?')
cev = input()    
if cev in ['Sınavım kötü geçti', 'Babamla tartıştım']:
    print('Takma kafana halledersin')
if cev in ['Otobüsü kaçırdım', 'Uçağı kaçırdım']:
    print ('Nasip, bir dahakine inşAllah.')
