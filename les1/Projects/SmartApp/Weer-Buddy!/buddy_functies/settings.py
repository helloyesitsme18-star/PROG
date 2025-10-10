def overwrite_settings(outputFile):
    try:
        with open(outputFile, 'r') as bestand:
            regels = bestand.readlines()

    except FileNotFoundError:
        print("Het bestand bestaat nog niet. Voer eerst optie 2 uit om het bestand aan te maken.")
        return None

    user_datum = input('Voer een datum in (dd-mm-yyyy): ')
    print('1. CV Ketel instellen\n2. Ventilatie instellen\n3. Bewatering instellen')
    keuze_menu = input('Maak uw keuze: ' + '\n')

    while True:
        try:
            if keuze_menu == '1':
                aanpassing = input('Geef een nieuwe waarde op (0-100): ')

                if 0 <= int(aanpassing) <= 100:
                    break
                else:
                    print('Waarde buiten bereik, probeer opnieuw.')

            if keuze_menu == '2':
                aanpassing = input('Geef een nieuwe waarde op (MAX: 4): ')

                if 0 <= int(aanpassing) <= 4:
                    break
                else:
                    print('Waarde buiten bereik, probeer opnieuw.')

            if keuze_menu == '3':
                aanpassing = input('Geef een nieuwe waarde op (0-1): ')

                if int(aanpassing) == 1 or int(aanpassing) == 0:
                    break
                else:
                    print('Waarde buiten bereik, probeer opnieuw.')
        except ValueError:
            print('Ongeldige type invoer, probeer opnieuw.')



    nieuw = []
    datum_ok = False

    for dag in regels:
        data = dag.strip().split(';')
        datum = data[0]

        if datum == user_datum:
            datum_ok = True

            if keuze_menu == '1':
                try:
                    waarde = int(aanpassing)
                    if 0 <= waarde <= 100:
                        data[1] = str(waarde)
                    else:
                        return -3
                except ValueError:
                    return -3

            elif keuze_menu == '2':
                try:
                    waarde = int(aanpassing)
                    if 0 <= waarde <= 4:
                        data[2] = str(waarde)
                    else:
                        return -3
                except ValueError:
                    return -3

            elif keuze_menu == '3':
                if aanpassing == '0':
                    data[3] = 'False'
                elif aanpassing == '1':
                    data[3] = 'True'
                else:
                    return -3
        nieuw.append(';'.join(data) + '\n')

    if not datum_ok:
        return -1

    with open(outputFile, 'w') as bestand:
        bestand.writelines(nieuw)

    return 0