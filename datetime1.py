import datetime
print("Bugün:", datetime.date.today())

print("Şimdi =", datetime.datetime.now())

print("Tarih, Saat:", datetime.datetime.now().strftime("%Y,%m")) #büyük y yılı yazar m ise ayı yazar.
