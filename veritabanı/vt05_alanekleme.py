# python -m pip install mysql-connector-python
import mysql.connector

try:
  mydb = mysql.connector.connect(host="localhost", user="root",     password="na200905.", database = "ots" )
  print("Bağlantı tamam:")
  
  try:
    secilen = mydb.cursor()
    secilen.execute("ALTER TABLE milletvekilleri ADD COLUMN doğumtarihi VARCHAR(10)") #tabloya doğum tarihi sütunu ekledik.
  except:
    pass


except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
