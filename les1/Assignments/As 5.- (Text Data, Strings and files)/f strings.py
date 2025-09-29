jaarloon = 5000
maandloon = jaarloon / 12

boodschap = f'Uw maandloon : {maandloon}.'
x = f'Uw maandloon: {maandloon:8.4f}'
print(boodschap)
print(x)

uur, minuut, seconde = 15, 37, 59
#print(uur + (minuut) + \n(seconde))/
print(f'{uur}\n{minuut}\n{seconde}')