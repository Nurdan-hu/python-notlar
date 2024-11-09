import re
metin1= "Bugün hava çok soğuk"
metin2= "Bursa çok sıcak"
metin3= "Bugün hava soğuk"

aranan= "^Bu.*sıcak$" #başında bu olan ve sıcak ile biten

print(re.search(aranan,metin1))  #metin birde aranan özellik var mı
print(re.search(aranan,metin2))  #metin ikide aranan özellik var mı
print(re.search(aranan,metin3))  #metin üçte aranan özellik var mı