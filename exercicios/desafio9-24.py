city = str(input('digite o nome de uma cidade: ')).strip()
#cit = city.split()
#ci = cit[0]
#c = ci.find('santo')
#c1 = c.replace('-1', 'verdadeiro')
cit = (city[:5].upper() == 'SANTO')
print(cit)