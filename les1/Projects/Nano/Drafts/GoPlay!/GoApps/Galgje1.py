import random

def lees_woorden(bestandsnaam):
    """
    Leest alle woorden.txt uit het woordenbestand en returnt een dictionary waarin het woord en diens moeilijkheid staat

    :param bestandsnaam:

    :return:
    Dictionary, woord en bijbehorende moeilijkheid
    """

    woorden = {         #dictionary NIET binnen de loop
        'makkelijk': [],
        'normaal': [],
        'moeilijk': []
    }

    with open(bestandsnaam, 'r') as bestand:

        for regel in bestand:
            regel = regel.strip()

            if regel == '':
                pass

            elif len(regel) <= 6:
                woorden['makkelijk'].append(regel)
            elif 7 <= len(regel) < 11:
                woorden['normaal'].append(regel)
            elif len(regel) >= 11:
                woorden['moeilijk'].append(regel)


    return woorden

def sla_woorden_op(bestandsnaam, dict):
    """
    Schrijft de volledigde woordenlijst terug naar het bestand en returnt niets.
    """
    with open(bestandsnaam, 'w') as bestand:
        for lijst in dict:      #loopt over geheel dictionary, pakt individuele lijsten eruit
            moeilijkheid = dict[lijst]      #moeilijkheid wordt hier direct een lijst
            for woord in moeilijkheid:
                bestand.write(woord + '\n')

        #for woord in dict['makkelijk']:
            #bestand.write(woord + '\n')
        #for woord in dict['normaal']:
            #bestand.write(woord + '\n')
        #for woord in dict['moeilijk']:
            #bestand.write(woord + '\n')

def bereken_score(aantal_levens_over, moeilijkheid):
    if moeilijkheid == 'makkelijk':
        moeilijkheid = 1
    elif moeilijkheid == 'normaal':
        moeilijkheid = 2
    elif moeilijkheid == 'moeilijk':
        moeilijkheid = 3



    score = aantal_levens_over * moeilijkheid

    return score

def voeg_score_toe(naam, woord, score):
    """
    Schrijft spelernaam, woord en bijbehorende score naar het score bestand
    """
    with open('../scores.txt', 'a') as bestand:
        bestand.write(f'{naam}, {woord}, {score}\n')

def toon_tussenstand(woord, geraden_letters):
    """
    Toont de geraden letters als volgt V _ _ R _ E E L D van het woord "voorbeeld"

    :param woord:
    :param geraden_letters:

    Return:
    de string met gerade letters zoals bovenstaand voorbeeld
    """
    stand = []
                                # check toevoegen voor hoofdletters (misschien .isupper ofso)
    for letter in woord:
        if letter in geraden_letters:
            stand.append(letter)
        else:
            stand.append('_')

    string = ' '.join(stand)

    return string

def kies_woord(woorden_dict, moeilijkheid):
    """
    :param woorden_dict:
    :param moeilijkheid:

    Returnt random gekozen woord met gekozen moeilijkheidsgraad
    """
    galgje_woord = woorden_dict[moeilijkheid]

    return random.choice(galgje_woord)

def speelsessie(woorden):
    """
    Vraagt om de moeilijkheidsgraad
    Kiest een random woord met de juiste moeilijkheidsgraad
    Laat gebruiker raden via console
    Houdt pogingen bij
    Logt resultaat van gebruiker in het scorebestand

    :return:
    """

    print("\n==============")
    while True:
        print('Maak je keuze:')
        print('1. Makkelijk')
        print('2. Normaal')
        print('3. Moeilijk')

        moeilijkheid = input(f'Keuze (1-3): ').strip()

        if moeilijkheid not in ['1','2','3']:
            print('Invoer niet herkend, probeer nogmaals.')
            continue
        else:
            break

    if moeilijkheid == '1':
        moeilijkheid = 'makkelijk'
        levens = 10
    elif moeilijkheid == '2':
        moeilijkheid = 'normaal'
        levens = 8
    elif moeilijkheid == '3':
        moeilijkheid = 'moeilijk'
        levens = 6

    galgje_woord = kies_woord(woorden, moeilijkheid)

    #naam invoer daarna pas tussenstand om spelen te starten etc.
    while True:                                           #naam input vragen
        speler_naam = input(f'Je naam: ').strip()
        if len(speler_naam) > 16:
            print('Max. 16 karakters AUB')
            continue
        elif speler_naam == '':
            print('Leeg veld, probeer nogmaals.')
            continue
        else:
            break

    print(f'Woord gekozen.')
    print(f'Difficulty: {moeilijkheid}, je hebt {levens} levens!\n')
    letters_geraden = []
    letters_fout = []
    poging = 0

    while True:
        print('\n')
        print(toon_tussenstand(galgje_woord, letters_geraden))
        resultaat = -1

        if letters_fout:
            print(f'Letters gebruikt: {", ".join(letters_fout)}')
        else:
            pass

        gok = input("Raad een letter (Enter om te stoppen): ").lower()

        if gok == '':
            break
        elif gok in letters_fout:
            print('Al gehad, probeer nogmaals.')
            continue

        elif len(gok) == 1 and gok.isalpha():
            if gok in galgje_woord:
                if gok in letters_geraden:          # deze check kan ook samen met letters_fout check (niet per se nodig)
                    print('Al gehad, probeer nogmaals.')
                    continue
                letters_geraden.append(gok)
                poging += 1
                print(f'Goed! | Levens: {levens}')



                for letter in galgje_woord:
                    if letter not in letters_geraden:
                        break

                else:
                    print(f'Je hebt gewonnen! Gefeliciteerd ')
                    resultaat = 'WIN'

                    score = bereken_score(levens, moeilijkheid)

                    print(f"\n{'====Sessie Score!====':^20}")
                    print(f'Woord: {galgje_woord} | Resultaat: {resultaat}' )
                    print(f'Pogingen: {poging} | Levens resterend: {levens}')
                    print(f'Score: {score}')

                    voeg_score_toe(speler_naam, galgje_woord, score)
                    break

            else:
                levens -= 1
                print(f'Mis! Levens: {levens + 1} → {levens}')
                poging += 1
                letters_fout.append(gok)
                if levens == 0:
                    resultaat = 'VERLIES'
                    print(f'Helaas, je hebt het niet geraden.')
                    print(f"\n{'====Sessie Score!====':^20}")
                    print(f'Woord: {galgje_woord} | Resultaat: {resultaat}')
                    print(f'Pogingen: {poging} | Levens resterend: {levens}')

                    voeg_score_toe(speler_naam, galgje_woord, 0)
                    break
                continue
        else:
            print('Ongeldige invoer, probeer nogmaals.')
            continue


def menu(woorden):
    """
    menu om code overzichtelijker te houden
    woorden als parameter meegeven zodat hij realtime aanpassingen kan maken

    :return:
    """
    print(f"{'====Galgje!====':^25}")
    print(f"{'Maak een keuze om te beginnen':^15}")

    while True:
        print(f"\nOpties:")
        print(f"1. Speel Galgje!")
        print(f"2. Verwijder een woord in de woordenlijst")
        print(f"3. Voeg woord toe aan de woordenlijst")
        print(f"4. Toon aantal woorden in de woordenlijst")
        print(f"5. Exit")

        optie = input('Optie: ').strip()
        if optie == "":
            print('Leeg veld, probeer nogmaals')
            continue
        elif optie not in ['1','2','3','4','5']:
            print('Optie niet herkend, probeer nogmaals')
            continue


        if optie == '1':
            speelsessie(woorden)

        elif optie == '2':
            while True:
                a = input(f'Typ het woord dat je wilt verwijderen: ')
                verwijder_woord = a.strip()

                if verwijder_woord == '':
                    print('Leeg veld, probeer nogmaals')
                    continue

                elif verwijder_woord in woorden['makkelijk']:
                    woorden['makkelijk'].remove(verwijder_woord)
                    print(f'Woord verwijderd.')
                    sla_woorden_op('woorden.txt', woorden)

                    break

                elif verwijder_woord in woorden['normaal']:
                    woorden['normaal'].remove(verwijder_woord)
                    print(f'Woord verwijderd.')
                    sla_woorden_op('woorden.txt', woorden)

                    break

                elif verwijder_woord in woorden['moeilijk']:
                    woorden['moeilijk'].remove(verwijder_woord)
                    print(f'Woord verwijderd.')
                    sla_woorden_op('woorden.txt', woorden)

                    break

                else:
                    print(f'Woord niet gevonden, probeer nogmaals')
                    continue




        elif optie == '3':
            while True:
                nieuw_woord = input(f'Voeg woord toe: ')
                nieuw_woord = nieuw_woord.strip()


                if nieuw_woord.isalpha():
                    if len(nieuw_woord) > 16:
                        print('Maximaal 16 letters AUB')
                        continue
                    if nieuw_woord in woorden['makkelijk'] or nieuw_woord in woorden['normaal'] or nieuw_woord in woorden['moeilijk']:
                        print('Woord bestaat al in het systeem.')
                        continue

                    else:
                        break
                else:
                    print('Ongeldige invoer, probeer nogmaals')
                    continue



            if len(nieuw_woord) <= 6:
                woorden['makkelijk'].append(nieuw_woord)
                sla_woorden_op('woorden.txt', woorden)
            elif 7 <= len(nieuw_woord) < 11:
                woorden['normaal'].append(nieuw_woord)
                sla_woorden_op('woorden.txt', woorden)
            else:
                woorden['moeilijk'].append(nieuw_woord)
                sla_woorden_op('woorden.txt', woorden)




        elif optie == '4':
            aantal_woorden = len(woorden['makkelijk']) + len(woorden['normaal']) + len(woorden['moeilijk'])
            print(f'Er zitten {aantal_woorden} woorden in het bestand.')

        if optie == '5':
            print('Tot ziens!')
            break

woorden = lees_woorden("woorden.txt")






