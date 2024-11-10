def fonksiyonu1():
    yield "Hello"
    yield 51
    yield "Good Bye"

x= fonksiyonu1()

print(x)

for z in x:
    print(z)