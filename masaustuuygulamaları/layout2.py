import sys
from PyQt5.QtWidgets import * 

app = QApplication(sys.argv)
masa = QMainWindow()

buyuk_tepsi= QVBoxLayout()
yatayicerik = QHBoxLayout()

dikeyicerik3 = QVBoxLayout()
dikeyicerik3.addWidget(QLabel("Ad:"))
dikeyicerik3.addWidget(QLabel("Soyad:"))

dikeyicerik4 = QVBoxLayout()
dikeyicerik4.addWidget(QLineEdit())
dikeyicerik4.addWidget(QLineEdit())

yi5 = QHBoxLayout()
yi5.addWidget(QPushButton("Giriş yap"))
yi5.addWidget(QPushButton("Çıkış"))

yatayicerik.addLayout(dikeyicerik3)
yatayicerik.addLayout(dikeyicerik4)

buyuk_tepsi.addLayout(yatayicerik)
buyuk_tepsi.addLayout(yi5)

sunumtepsisi= QWidget()
sunumtepsisi.setLayout(buyuk_tepsi)

masa.setCentralWidget(sunumtepsisi)

masa.show()
app.exec()           #layout1'de yaptığımızın aynısı sadece class'sız hali