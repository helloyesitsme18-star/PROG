def Fahrenheit(temp_celsius):
    return temp_celsius * 1.8 + 32

def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    return (temp_celsius - luchtvochtigheid) / 100 * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    temp_gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if temp_gevoel > 0 and windsnelheid > 10:
        return (f'Het is heel koud en het stormt! Verwarming helemaal aan!')
    elif temp_gevoel > 0 and windsnelheid < 10:
        return (f'Het is behoorlijk koud! Verwarming aan op de benedenverdieping!')
    elif 0 <= temp_gevoel < 10 and windsnelheid > 12:
        return (f'Het is een beetje koud, elektrische kachel op de benedenverdieping aan!')
    elif 10 <= temp_gevoel < 22:
        return (f'Heerlijk weer, niet te koud of te warm.')
    else:
        return(f'Warm! Airco aan!')

temp_celsius_hist = []  #lijst om gem.temp te pakken
#temp_celsius_hist.append()

def weerstation():
    temp_celsius_hist = []  # lijst om gem.temp te pakken


    for dag in range(1,8):

        while True:
            temp_celsius = input(f'Hoeveel graden is het op dag {dag}? (°C): ')
            if temp_celsius == '':
                print("Leeg vak, probeer opnieuw")
            try:
                temp_celsius = int()
            except ValueError:
                print('')


        while True:
            windsnelheid = input (f'Wat is de windsnelheid op dag {dag}? (m/s): ')
            if temp_celsius == '':
                print("Leeg vak, probeer opnieuw")

            luchtvochtigheid = input (f'Wat is de luchtvochtigheid op dag {dag}? (%): ')
            if temp_celsius == '':
                print("Leeg vak, probeer opnieuw")

            dag += 1
            print("=======================================================================")
            temp_celsius_hist.append(temp_celsius)

   # if temp_celsius:



# IF temp_celsius or windsnelheid or luchtvochtigheid == ' ' BREEEAAAAKKK

