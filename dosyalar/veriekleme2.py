# a = open(f"rehber.txt","w", encoding="utf8") encoding="utf8" demek türkçe karakterleri oku demek.
# a.write("Çarşamba")

a = open(f"rehber.txt","r",encoding= "utf8") #mod belirtilmezse (w,a,r) r(read) olarak kabul edilir.
print(a)
okunan = a.read()
print(okunan)        #dosyanın içini terminalde yazar.

