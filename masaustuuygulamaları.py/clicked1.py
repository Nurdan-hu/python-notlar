from PyQt5.QtWidgets import *
class Girişekranı(QMainWindow):
    def __init__(self):
        super().__init__()
        def xxx():
            mesaj =("Giriş düğmesine tıklandı.")
            print(mesaj)
            dig = QMessageBox(self)
            dig.setWindowTitle("DİKKAT")
            dig.setText(mesaj)
            dig.exec()

        def kontrol(self):
            print("Giriş düğmesine tıklandı")
            


        def yyy():
            print("Vazgeç düğmesine tıklandı.")
            aaa = QMessageBox(self)
            aaa.setWindowTitle("Aman dikkat!")
            aaa.setText("Vazgeç düğmesine tıklandı")
            aaa.exec()

        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Kullanıcı Adı:"))
        dikeyicerik3.addWidget(QLabel("Şifresi:"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())
        
        yi5= QHBoxLayout()
        dugme1= QPushButton("Giriş yap")
        yi5.addWidget(dugme1)
        dugme1.clicked.connect(kontrol) 
        
        dugme2= QPushButton("Vazgeç")
        yi5.addWidget(dugme2)
        dugme2.clicked.connect(yyy)

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)

        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)



aa = QApplication([])
pencere = Girişekranı()
pencere.show()
aa.exec()