import json

bestand = 'oefening_7_5_inloggers.json'

try:                                        #probeert de functies die erna volgen, als deze niet lukken dan except:
    with open(bestand, 'r') as file:
        inlog = json.load(file)
except:
    inlog = []              #maakt van inlog een lijst indien er nog niks in staat/bestand niet bestaat


while True:
    naam = input("Wat is je achternaam? ")
    if naam == 'einde':
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    gebruiker = {
                'naam': naam,
                'voorl': voorl,
                'gbdatum': gbdatum,
                'email': email
            }

    inlog.append(gebruiker)    #voegt gebruiker-data toe aan bestaande lijst
    with open(bestand, 'w') as file:
        json.dump(inlog, file, indent=5)            #stopt volledige nieuwe lijst in file




    # Maak een dictionary van de gegevens van deze gebruiker. Zie ook het voorbeeldbestand onderaan de pagina.
    # wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file.


