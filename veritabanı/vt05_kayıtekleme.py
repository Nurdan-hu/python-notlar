import mysql.connector

try:
  vts = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="na200905.", # Veritabanı sistemi(instance) şifresi
    database = "pythondersleri"
  )
  print("Bağlantı tamam:")

  try:
    secilen = vts.cursor()
    # secilen.execute("CREATE DATABASE pythondersleri") #pythondersleri adlı veritabanı sistemi oluşturdu.
    secilen.execute ("INSERT INTO ogrenciler(ad,telefon) VALUES ('Buse VAROL',9343903)")
    vts.commit()
    print("Kayıt eklendi.")

  except mysql.connector.Error as hata:
    print(f"Hata oluştu. Hata : {hata}")
except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
