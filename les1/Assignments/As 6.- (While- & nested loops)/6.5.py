woord = str()
while len(woord) != 4:
    woord = input(f'Geef een string van vier letters: ')
    if len(woord) == 4:
        break
    print(f'{woord} heeft {len(woord)} letters')

print(f'Inlezen van correcte string: {woord} is geslaagd')

