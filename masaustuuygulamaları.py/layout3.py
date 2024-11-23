from PyQt5.QtWidgets import *
class Girişekranı(QMainWindow):
    def __init__(self):
        super().__init__()
        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Kullanıcı Adı:"))
        dikeyicerik3.addWidget(QLabel("Şifresi:"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())
        
        yi5= QHBoxLayout()
        yi5.addWidget(QPushButton("Giriş Yap")) 
        yi5.addWidget(QPushButton("Vazgeç")) 

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)

        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)

class AnaEkran(QMainWindow):
    def __init__(self):
        super().__init__()
        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Gideceğiniz Yerin İsmini Yazınız:"))
        dikeyicerik3.addWidget(QLabel("İsminizi Yazınız:"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())

        baslıkBolumu = QHBoxLayout()
        baslıkBolumu.addWidget(QLabel("==UYGULAMA ANA EKRANI=="))
        
        yi5= QHBoxLayout()
        yi5.addWidget(QPushButton("Giriş Yap")) 
        yi5.addWidget(QPushButton("Vazgeç")) 

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(baslıkBolumu)
        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)

        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)

aa = QApplication([])
pencere = Girişekranı()
pencere.show()

ana= AnaEkran()
ana.show()
aa.exec()