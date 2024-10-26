sorular = [
    "Su yutmuş toprağa ne denir?",
    "Ağır suya ne denir?", 
    "Ateş değil ama yanar, kanatları yok ama uçar, ayakları yok ama koşar.",
] 
cevaplar = [
    "Çamur"
    "Buz"
    "Güneş"
]
def menu():
    print("BİLMECELER")
    print("1-bilmece sor")
    print("2-bilmece listesi")
    print("3-bilmece cevapları")
    secim = input()
    if secim == "1":
        pass
    if secim == "2":
        print(*sorular, sep="\n")
    
    




menu()