getal_a = range(1,11)
for getal in getal_a:
    print(f'Tafel van {getal}:')
    for getal_b in range(1,11):
        tafel = getal * getal_b
        print(f'{getal} x {getal_b} = {tafel}')
    print()
