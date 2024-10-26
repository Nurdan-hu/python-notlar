meyveler1=["muz","dut","nar"]          #list türü collection
meyveler2=("elma","armut","kivi")      #tuple türü collection
meyveler3=["havuç","portakal","greyfurt"] 
print(meyveler1)
print(meyveler2)

#print(meyveler1+meyveler2      tipleri farklı olduğu için hata verir.)
m4 = meyveler1+meyveler3
meyveler1 += meyveler3         #meyveler3'ü meyveler1'e geçirir.
print(m4)

print(meyveler1)
meyveler1.append("karpuz")     #meyveler1'e karpuzu da ekler.
print(meyveler1) 

meyveler1.insert(1,"Bostan")   #Birinci yere bostan yazar ve diğer maddeleri yana kaydırır.
print(meyveler1)

meyveler1.pop()                #son elemanı siler.
print(meyveler1)