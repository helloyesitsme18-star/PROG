print('Start')
def kwadraat(getal):
    result = getal * getal
    return result

for getal in range(1,6):
    print('Het kwadraat van ' + str(getal) + ' = ' + str(kwadraat(getal)))
print('Einde')