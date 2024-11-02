#input() Burada girilen bilgi işe yaramaz.
# a = input () Bu şekilde olunca kullanıcı bir şey girmesi gerektiğini bilemez.
#print(a*5)
#print('Bu program girilen şeyi 5 kere yazar.')
#a = input('Bir şeyler giriniz: ')
#print(a*5)


# print('Bu program kaç yıl yaşadığını hesaplar.')
# a = input ('Doğum yılın nedir?')
# a = int(a)
# print (2024-int(a))
# a = input ('Doğum yılın nedir')
print('Bu program kaç yıl yaşadığını hesaplar')
ad = input ('Adın nedir?')
a = int(input(f'{ad} doğum yılın nedir?'))
print(f"Demek {2024-a} yaşındasın {ad}.")
if 2024-a > 50 : print('Yaşlısın.')
elif 2024-a > 30 : print ('Orta yaşlısın.')
elif 2024-a > 15 : print ('Gençsin.')
input()
