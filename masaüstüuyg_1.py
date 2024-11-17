import tkinter as tk
import keyboard
from pynput import keyboard
from pynput.keyboard import Listener
pencere = tk.Tk()
pencere['bg']="black"
pencere.geometry("350x200") #350x450
pencere.title("Hesap Makinesi")
islem = tk.Label(text="", bg="black", fg="yellow")
islem.place(x=13, y=10)
butonislem = []

def islemeşittir():
    global butonislem
    karakterdizisi = ""
    for x in butonislem:

        karakterdizisi = karakterdizisi + x
    islemeval = eval(karakterdizisi)
    islem['text']= str(islemeval)
    butonislem.clear()

def islem0():
    global butonislem
    islem['text'] = islem['text'] + buton0['text']
    butonislem.append(buton0['text'])
def islem1():
    global butonislem

    islem['text'] = islem['text'] + buton1['text']
    butonislem.append(buton1['text'])

def islem2():
    global butonislem
    islem['text'] = islem['text'] + buton2['text']
    butonislem.append(buton2['text'])
def islem3():
    global butonislem
    islem['text'] = islem['text'] + buton3['text']
    butonislem.append(buton3['text'])

butonlar123 = []
buton1 = tk.Button(text="1", width=3, command=islem1)
buton2 = tk.Button(text="2", width=3, command=islem2)
buton3 = tk.Button(text="3", width=3, command=islem3)
butonlar123.append(buton1)
butonlar123.append(buton2)
butonlar123.append(buton3)
xdeger123 = 13
ydeger123 = 45

for x in butonlar123:

    x.place(x=xdeger123, y=ydeger123)
    xdeger123 += 31

butonlar456 = []
def islem4():
    global butonislem
    islem['text'] = islem['text'] + buton4['text']
    butonislem.append(buton4['text'])
def islem5():
    global butonislem
    islem['text'] = islem['text'] + buton5['text']
    butonislem.append(buton5['text'])
def islem6():
    global butonislem
    islem['text'] = islem['text'] + buton6['text']
    butonislem.append(buton6['text'])
buton4 = tk.Button(text="4", width=3, command=islem4)
buton5 = tk.Button(text="5", width=3,  command=islem5)
buton6 = tk.Button(text="6", width=3,  command=islem6)
butonlar456.append(buton4)
butonlar456.append(buton5)
butonlar456.append(buton6)
xdeger456 = 13 #15
ydeger456 = 80
for x in butonlar456:

    x.place(x=xdeger456, y=ydeger456)
    xdeger456 += 31

def islem7():
    global butonislem
    islem['text'] = islem['text'] + buton7['text']
    butonislem.append(buton7['text'])
def islem8():
    global butonislem
    islem['text'] = islem['text'] + buton8['text']
    butonislem.append(buton8['text'])
def islem9():
    global butonislem
    #islem['text']=""
    islem['text'] = islem['text'] + buton9['text']
    butonislem.append(buton9['text'])
butonlar789 = []
buton7 = tk.Button(text="7", width=3, command=islem7)
buton8 = tk.Button(text="8", width=3, command=islem8)
buton9 = tk.Button(text="9", width=3, command=islem9)
buton7.place(x=15, y=115)
butonlar789.append(buton7)
butonlar789.append(buton8)
butonlar789.append(buton9)
xdeger789 = 13 #15
ydeger789 = 115
for x in butonlar789:

    x.place(x=xdeger789, y=ydeger789)
    xdeger789 += 31
def islemartı():
    global butonislem
    islem['text']= ""
    butonislem.append(artı['text'])
def islemeksi():
    global butonislem
    islem['text'] = ""
    butonislem.append(eksi['text'])
def islemçarpma():
    global  butonislem
    islem['text'] = ""
    butonislem.append("*")
def islembölme():
    global butonislem
    islem['text'] = ""
    butonislem.append("/")
def islembuton():
    islem['text'] = islem['text'].rstrip(islem['text'][-1])
buton = tk.Button(text="C", width=3, height=8, command=islembuton)
buton.place(x=155, y=ydeger123)
artı = tk.Button(text="+",width=3, command=islemartı)
artı.place(x=115, y=ydeger123)
eksi = tk.Button(text="-", width=3, command=islemeksi)
eksi.place(x=115, y=ydeger456)
çarpma = tk.Button(text="X", width=3, command=islemçarpma)
çarpma.place(x=115, y=ydeger789)
bölme  = tk.Button(text="÷", width=3, command=islembölme)
bölme.place(x=115, y=ydeger789+(ydeger789-ydeger456))
buton0 = tk.Button(text="0", width=3, command=islem0)
buton0.place(x=13, y=ydeger789+((ydeger789-ydeger456)))
#b = tk.Button(text="qwjwn", command=lambda : print(*butonislem))
#b.pack()
eşittir  = tk.Button(text="=", width=7, command=islemeşittir)
eşittir.place(x=44,y=ydeger789+((ydeger789-ydeger456)) )

pencere.mainloop()              #hesap makinesini googledan aldım.