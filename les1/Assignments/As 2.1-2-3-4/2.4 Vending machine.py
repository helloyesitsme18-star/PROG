import random
prijs = random.randint(40,150)
print('De prijs van dit product is ' + str(prijs) + ' cent.')

betaald = int(input('Wat heb je betaald?:'))
terug = betaald - prijs
print('Je krijgt ' + str(terug) + ' cent terug.')

munten50 = terug//50
terug = terug - (munten50 * 50)
munten20 = terug//20
terug = terug - (munten20 * 20)
munten10 = terug//10
terug = terug - (munten10 * 10)
munten5 = terug//5
terug = terug - (munten5 * 5)
munten2 = terug//2
terug = terug - (munten2 * 2)
munten1 = terug//1
terug = terug - (munten1 * 1)


print('aantal munten van 50 cent is ' + str(munten50))
print('aantal munten van 20 cent is ' + str(munten20))
print('aantal munten van 10 cent is ' + str(munten10))
print('aantal munten van 5 cent is ' + str(munten5))
print('aantal munten van 2 cent is ' + str(munten2))
print('aantal munten van 1 cent is ' + str(munten1))