# python -m pip install mysql-connector-python
import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="na200905." # Veritabanı sistemi(instance) şifresi
  )
  print("Bağlantı tamam:")
  print(mydb)
except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
