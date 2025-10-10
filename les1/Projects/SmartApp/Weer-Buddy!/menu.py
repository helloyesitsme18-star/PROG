from buddy_functies import overwrite_settings, Fahrenheit, gevoelstemperatuur, weerrapport, weerstation, aantal_dagen, auto_bereken
import pyfiglet
from utilities import weer_utrecht

def smart_app_controller():
    inputFile = 'inputFile.txt'
    outputFile = 'outputFile.txt'

    print(r"""░██       ░██                                        ░████████                     ░██        ░██            ░██ 
░██       ░██                                        ░██    ░██                    ░██        ░██            ░██ 
░██  ░██  ░██  ░███████   ░███████  ░██░████         ░██    ░██  ░██    ░██  ░████████  ░████████ ░██    ░██ ░██ 
░██ ░████ ░██ ░██    ░██ ░██    ░██ ░███     ░██████ ░████████   ░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██ ░██ 
░██░██ ░██░██ ░█████████ ░█████████ ░██              ░██     ░██ ░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██ ░██ 
░████   ░████ ░██        ░██        ░██              ░██     ░██ ░██   ░███ ░██   ░███ ░██   ░███ ░██   ░███     
░███     ░███  ░███████   ░███████  ░██              ░█████████   ░█████░██  ░█████░██  ░█████░██  ░█████░██ ░██ 
                                                                                                         ░██     
                                                                                                   ░███████      
                                                                                                                 """)

    print('Welkom bij Weer-Buddy, de handigste buddy-app voor in huis! ')


    while True:
        print("=======================================================================")
        print('\nMaak uw keuze: ')
        print('1. Weerstation')
        print('2. Aantal dagen tellen met opgeslagen data')
        print('3. Aanbevolen instellingen berekenen')
        print('4. Instellingen handmatig overschrijven')
        print('5. Huidige weer in Utrecht')
        print('6. Programma afsluiten')

        keuze = input('Maak uw keuze (1-6): ').strip()


        if keuze == '1':
            weerstation()
        elif keuze == '2':
            resultaat = aantal_dagen(inputFile)
            if resultaat == -1:
                print('Het bestand kon niet worden gevonden.')
            else:
                print(f'Aantal dagen in het bestand: {resultaat}')

        elif keuze == '3':
            auto_bereken(inputFile, outputFile)
            print(f'Automatische berekening voltooid. Resultaat opgeslagen in {outputFile}.')

        elif keuze == '4':
            resultaat = overwrite_settings(outputFile)
            if resultaat == 0:
                print('Instelling succesvol aangepast.')
            elif resultaat == -1:
                print('Gekozen datum niet gevonden in bestand.')
            elif resultaat == -3:
                print('Ongeldige invoer of keuze.')

        elif keuze == '5':
            weer = weer_utrecht()

            if weer:
                print(f'Huidige temperatuur in Utrecht: {weer['temperature']} °C')
                print(f'Windsnelheid: {weer['windspeed']} km/u')


            else:
                print('Weerdata niet gevonden.')


        elif keuze == '6':
            print('Programma afgesloten.')
            break

        else:
            print('Ongeldige keuze. Probeer opnieuw.')

smart_app_controller()