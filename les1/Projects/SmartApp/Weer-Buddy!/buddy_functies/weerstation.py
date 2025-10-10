def Fahrenheit(temp_celsius):
    return temp_celsius * 1.8 + 32

def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    return temp_celsius - (luchtvochtigheid / 100) * windsnelheid

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    temp_gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if temp_gevoel < 0 and windsnelheid > 10:
        return (f'Het is heel koud en het stormt! Verwarming helemaal aan!')
    elif temp_gevoel < 0 and windsnelheid <= 10:
        return (f'Het is behoorlijk koud! Verwarming aan op de benedenverdieping!')
    elif 0 <= temp_gevoel < 10 and windsnelheid > 12:
        return (f'Het is best koud en het waait; verwarming aan en roosters dicht!')
    elif 0 <= temp_gevoel < 10 and windsnelheid < 12:
        return (f'Het is een beetje koud, elektrische kachel op de benedenverdieping aan!')
    elif 10 <= temp_gevoel < 22:
        return (f'Heerlijk weer, niet te koud of te warm.')
    else:
        return(f'Warm! Airco aan!')

def weerstation():
    temp_celsius_hist = []  # lijst om gem.temp te op te slaan


    for dag in range(1,8):

#Temperatuur
        while True:
            temp_1 = input(f'Hoeveel graden is het op dag {dag}? (°C): ')
            if temp_1 == '':
                print("Leeg vak, het programma stopt nu.")
                return
            try:
                temp_celsius = float(temp_1)
                break

            except ValueError:
                print('Probeer opnieuw, onjuist type invoer')

#Windsnelheid
        while True:
            wind = input (f'Wat is de windsnelheid op dag {dag}? (m/s): ')
            if wind == '':
                print("Leeg vak, het programma stopt nu.")
                return
            try:
                windsnelheid = float(wind)
                break
            except ValueError:
                print('Probeer opnieuw, onjuist type invoer')

#Luchtvochtigheid
        while True:
            vochtigheid = input (f'Wat is de luchtvochtigheid op dag {dag}? (%): ')
            if vochtigheid == '':
                print("Leeg vak, het programma stopt nu.")
                return
            try:
                luchtvochtigheid = float(vochtigheid)
                if luchtvochtigheid < 0 or luchtvochtigheid > 100:
                    print('Invoer moet tussen 0-100 liggen, probeer nogmaals.')
                    continue
                break
            except ValueError:
                print('Probeer opnieuw, onjuist type invoer')


        temp_celsius_hist.append(temp_celsius)
        gem_temp = sum(temp_celsius_hist) / len(temp_celsius_hist)
        print(f'Het is {temp_celsius:.1f}C en {Fahrenheit(temp_celsius):.1f}F')
        print(weerrapport(temp_celsius, windsnelheid, luchtvochtigheid))
        print(f'De gemiddelde temperatuur is vandaag {gem_temp:.1f}C')
        print("=======================================================================")