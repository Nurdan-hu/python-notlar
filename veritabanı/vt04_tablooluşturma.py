import mysql.connector

try:
  vts = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="na200905.", # Veritabanı sistemi(instance) şifresi
    database="ots"
  )

  try:
    secilen = vts.cursor()
    # secilen.execute("DROP Table milletvekilleri tabloyu siler
    secilen.execute("CREATE Table milletvekilleri(isim VARCHAR(50),TCno VARCHAR(11),Görevİli VARCHAR(20),okuduğubölüm VARCHAR(20))")
    print("Tablo oluşturuldu.")
  
  except mysql.connector.Error as hata:
    print(f"Tablo tabanı oluşturulamadı. Hata : {hata}")
except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
