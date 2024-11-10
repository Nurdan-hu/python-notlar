a=5 
def xx():
    # print(a)
    global a  #global demek koddaki a'ların hepsini defin içindeki a'ya yani 6'ya tanımlar.
    a= 6
    print(a)

xx()
print(a)

a=10
xx()