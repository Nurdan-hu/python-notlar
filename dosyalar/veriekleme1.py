# a = open (f"rehber.txt","w")   #write ile yazıldığında öncekiler silinir.
a = open (f"rehber.txt","a")   #w yerine a kullanma sebebi: ekleme yapacak olmamız.
for b in range(10):
    a.write(f"{str(b)}\n")