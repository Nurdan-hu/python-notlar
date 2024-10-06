m1='Şehirler'
m2='Ankara'
m3='İzmir'
m4=f'İller {m3}-- {m2}'
m5=f'{m1} {m4} {m2}'
print (m4)
print (m5)

print(f'şehirler: {m2},{m3}')

print('şehirler: {},{}'.format (m2,m3)) #üsttekinin aynısıdır.
print('şehirler: %s,%s' % (m2,m3))      #üsttekinin aynısıdır.
input()
