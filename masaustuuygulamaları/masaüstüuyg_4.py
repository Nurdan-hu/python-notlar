import sys
from PyQt5.QtWidgets import * 

app = QApplication(sys.argv)
masa = QMainWindow()

tepsi1 = QVBoxLayout() #vertical yani dikey dizilmesini sağlar
#tepsi1= QHBocLayout yazsaydım yatay dizilirdi(hertical)

tepsi1.addWidget(QLabel("Kullanıcı adı:"))
tepsi1.addWidget(QLineEdit()) #kullanıcının doldurması için boş satır

tepsi1.addWidget(QLabel("Şifre:"))
tepsi1.addWidget(QLineEdit())

tepsi1.addWidget(QPushButton("Giriş")) #giriş düğmesi oluşturur.
tepsi1.addWidget(QCheckBox("Beni Hatırla")) #beni hatırlaya basarsan tik olur

sunumtepsisi= QWidget()
sunumtepsisi.setLayout(tepsi1)

masa.setCentralWidget(sunumtepsisi)

masa.show()
app.exec()