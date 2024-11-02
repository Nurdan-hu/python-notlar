import random
import time

print ("Önünde iki tane mağara var.")
time.sleep(1)
print ("Bunlardan birisinde hazinesini seninle paylaşacak arkadaş canlısı bir ejderha var")
time.sleep(2)
print ("Diğerinde ise doymak bilmeyen ve karnı aç bir ejderha yaşıyor. O seni hemen yiyecek!")
time.sleep(1)
magara = int(input('Hangi mağaraya (1 or 2) gideksin?'))
print ("Mağaraya yaklaşıyorsun")
time.sleep(1)
print ("İçerisi karanlık ve korkutucu")
time.sleep(1)
print ("Büyük bir ejderha önünde beliriyor! Ağzını açıyor ve…")
time.sleep(1)

arkadas_magarasi = random.randint(1, 2)

if magara == arkadas_magarasi:
    print ("Hazinesini paylaşır.")
else :
      print("Seni bir çırpıda yer.")