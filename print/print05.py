meyveler= ['elma','muz','nar','dut']
print(meyveler)
print(*meyveler)
print(*meyveler, sep = ',') # aralarında herhangi bir şey koymak için kullanılır.
print(*meyveler, sep = '\n')

print('Van', 'Muş', 'Çan', 'Bor')
print('Van', 'Muş', 'Çan', 'Bor', sep = '')
print('Van', 'Muş', 'Çan', 'Bor', sep = '-')

print('Van', 'Muş', 'Çan', 'Bor', end='')
print('Van', 'Muş', 'Çan', 'Bor', sep = '-', end='')
#end parametresi print ile yazdıktan sonra ne yapılacağını belirtir.
input()
