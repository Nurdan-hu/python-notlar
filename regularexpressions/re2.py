import re
xxx= "Ali al renkli bir şal aldı."

#tüm al ifadelerini listeler:
arananListe= re.findall("al",xxx)
print(f"al ifadesi listesi: ", len(arananListe),arananListe) #kaç tane al var onuyazar sonra da ard arda al'ları sıralar

#şal ifadesini ara:
print(re.search("şal",xxx))

#ala göre böl:
print(re.split("al",xxx))

#boşlukları zzz yap:
print(re.sub(" ","zzz",xxx))