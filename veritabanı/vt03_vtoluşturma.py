import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="na200905." # Veritabanı sistemi(instance) şifresi
  )
  print("Bağlantı tamam:")
  print(mydb)

  try:
    secilen = mydb.cursor()
    secilen.execute("CREATE DATABASE pythondersleri") #pythondersleri adlı veritabanı sistemi oluşturdu.
    print("Veritabanı oluşturuldu.")
  except mysql.connector.Error as hata:
    print(f"Veri tabanı oluşturulamadı. Hata : {hata}")
except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
