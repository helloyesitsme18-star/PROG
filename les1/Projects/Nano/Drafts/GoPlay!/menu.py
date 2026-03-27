from GoApps import lees_woorden, menu
from GoApps import raad_het_nummer, advies_moeilijkheidsgraad
import pyfiglet
from utilities import weer_utrecht

def GoApp():

    woorden = lees_woorden('woorden.txt')

    print('Welkom bij GoPlay! Entertainment voor onderweg :) ')
    print('=======================================================================')


    while True:
        print('\nMaak uw keuze: ')
        print('1. Galgje!')
        print('2. Raad het getal!')
        print('3. Huidig weer bekijken')
        print('4. Programma stoppen')


        keuze = input('Maak uw keuze (1-4): ').strip()

        if keuze == '1':
            menu(woorden)

        elif keuze == '2':
            raad_het_nummer()

        elif keuze == '3':
            try:

                weer = weer_utrecht()
                if weer:
                    print(f"Huidige temperatuur in Utrecht: {weer['temperature']} °C")
                    print(f"Windsnelheid: {weer['windspeed']} km/u")
                    print(f'=================================================================')
            except:
                print("Kan weergegevens niet ophalen, probeer later opnieuw.")


        elif keuze == '4':
            print('Programma afgesloten.')
            break
        else:
            print(f'Invoer niet herkend, probeer nogmaals')
            continue

GoApp()