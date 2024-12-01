import mysql.connector
try: 
    vts = mysql.connector.connect(host = "localhost", user = "root" , password = "na200905." , database = "deneme")
    print("Bağlantı tamam")
    secilen = vts.cursor()
    alinan_liste = secilen.execute("select * from derslervenotlar")
    xxx = secilen.fetchall()
    for a in xxx :
        print(a)
except:
    print("Veritabanına bağlanırken bir hata oluştu.")