#for a in range(10):
   #print(a,".sayı", sep="") #sep koymqmızın sebebi rakam ile sayının arasında boşluk olmasını istememem.

#for b in range(5,20): print (b)



#for c in range(10,30,2): print(c)

#for zzz in range(100,10,-10): print(zzz)
#for x in 'Erdinç': print(x)
#for x in "Selam": print(x, end="\n")

#kelime = "Merhaba"
#for x in kelime: print(x)

#for a in range (1,11):
#    for b in range (1,11):
#        print(a,"x",b,"=",a*b)
#    print()                                   #çarpım tablosu kodu

#for a in range (1,11):
#    if a ==3 : continue             #a'nın üç olduğu durumları atlar ve devam eder
#    for b in range (1,11):
#        print(a,"x",b,"=",a*b)
#    print()   

for a in range (1,11):
    for b in range (1,11):
        if b % 2 == 0 : continue    #b'nin ikiye bölümünden kalanın sıfır olduğu durumları yani çift sayıları atlar.
        print(a,"x",b,"=",a*b)
    print()   

    # continue yerine break komutu yazarak bitirebiliriz.