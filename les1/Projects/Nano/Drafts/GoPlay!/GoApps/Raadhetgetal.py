import random

def genereer_getal(moeilijkheid):       #returnt het te raden getal
    if moeilijkheid == 1:
        getal = random.randint(1, 10)
        return getal
    elif moeilijkheid == 2:
        getal = random.randint(1, 50)
        return getal

    elif moeilijkheid == 3:
        getal = random.randint(1, 100)
        return getal

def max_pogingen(moeilijkheid):         #returnt 5,7 of 10
    if moeilijkheid == 1:
        return 5
    elif moeilijkheid == 2:
        return 7
    elif moeilijkheid == 3:
        return 10
    else:
        return None

def score(moeilijkheidsgraad, aantal_pogingen):        #returnt score
    result = (max_pogingen(moeilijkheidsgraad) - aantal_pogingen) * moeilijkheidsgraad
    return result

def advies_moeilijkheidsgraad(score):               #returnt advies op basis van score
    if score < 5:
        return ('Advies: Probeer een lagere moeilijkheidsgraad.')
    elif 5 <= score <= 12:
        return ('Advies: Houd deze moeilijkheidsgraad aan.')
    else:
        return ('Advies: Je kunt een hogere moeilijkheidsgraad aan!')

def raad_het_nummer():

    print(f'--- Raad het nummer ---')
#naam
    while True:
        try:
            naam = input(f'Voer AUB een naam in: ')
            if len(naam) > 16 or naam == '':
                raise ValueError
        except ValueError:
            print("Ongeldige invoer.")
            continue
        print(f'Welkom {naam}!')
        break
#keuze menu
    while True:
        print(f'Kies een moeilijkheid: ')
        print('1. Easy')
        print('2. Normal')
        print('3. Hard')

        try:
            keuze = input('Maak je keuze (1-3): ')
            if keuze == '':
                print("Spel sluit nu af, tot ziens!")
                return
            else:
                keuze = int(keuze)

            if keuze in (1,2,3):
                break #stopt hier met de loop
            else:
                print('Je invoer was ongeldig\n')

        except ValueError:
            print("Voer een getal in.\n")
            print('=======================================================================')

#variabelen
    moeilijkheid = keuze
    max_p = max_pogingen(moeilijkheid)
    raadgetal = genereer_getal(moeilijkheid)


    print('=======================================================================')
    if moeilijkheid == 1:
        print('Raad het getal tussen 1-10')
    elif moeilijkheid == 2:
        print('Raad het getal tussen 1-50')
    elif moeilijkheid == 3:
        print('Raad het getal tussen 1-100')
    print(f'Je hebt {max_p} pogingen.')

#gamelogica
    for poging in range(1, max_p + 1):

        while True:
            try:
                gok = input('Raad het getal: ')
                if gok == '':
                    print("Spel sluit nu af, tot ziens!")
                    return
                else:
                    gok = int(gok)
                    break
            except ValueError:
                print('Ongeldig antwoord, probeer nogmaals.')
                continue

        pogingen_over = max_p - poging
        eindscore = score(moeilijkheid, poging)
        advies = advies_moeilijkheidsgraad(eindscore)

        if gok == raadgetal:
            print('=======================================================================')
            print('Gefeliciteerd! Je hebt een getal geraden... en nu?')
            print(f'Je score was {eindscore}')
            print(advies)
            break
        else:
            if pogingen_over == 0:
                print('=======================================================================')
                print(f'Helaas, het getal was {raadgetal}')
                print(f'Je score was {eindscore}')

                print(advies)
                break
            else:
                if gok < raadgetal:
                    if (raadgetal - gok) <= 2:
                        print('Dichtbij!')
                    else:
                        print('Hoger!')
                elif gok > raadgetal:
                    if (gok - raadgetal) <= 2:
                        print('Dichtbij!')
                    else:
                        print('Lager!')

                print('=======================================================================')

            if pogingen_over > 0:
                print(f'Je hebt nog {pogingen_over} pogingen.')
                print(f'Je huidige score is {eindscore}')











