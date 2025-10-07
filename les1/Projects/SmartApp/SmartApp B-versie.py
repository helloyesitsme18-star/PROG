def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - (luchtvochtigheid / 100.0) * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gt = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gt < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gt < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gt < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gt < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gt < 22:
        return "Heerlijk weer, niet te koud of te warm."
    return (f"Warm! Airco aan!{gt}")


def weerstation():
    temps = []

    for dag in range(1, 8):

        while True:
            temp1 = input(f"Wat is op dag {dag} de temperatuur: ")
            if temp1 == "":
                print("Lege invoer ontvangen, programma stopt.")
                return
            try:
                temp_c = float(temp1)
                break
            except ValueError:
                print("Ongeldige invoer voor temperatuur. Vul een getal in. Probeer opnieuw.")


        while True:
            winds = input(f"Wat is op dag {dag} de windsnelheid(m/s): ")
            if winds == "":
                print("Lege invoer ontvangen, programma stopt.")
                print("Programma klaar!")
                return
            try:
                windsnelheid = float(winds)
                break
            except ValueError:
                print("Ongeldige invoer voor windsnelheid. Vul een getal in. Probeer opnieuw.")

        while True:
            s = input(f"Wat is op dag {dag} de vochtigheid(%) (0-100): ")
            if s == "":
                print("Lege invoer ontvangen, programma stopt.")
                print("Programma klaar!")
                return
            try:
                luchtvochtigheid = int(s)
                if not (0 <= luchtvochtigheid <= 100):
                    print("Vochtigheid moet tussen 0 en 100 liggen. Probeer opnieuw.")
                    continue
                break
            except ValueError:
                print("Ongeldige invoer voor vochtigheid. Vul een geheel getal (0-100). Probeer opnieuw.")


        temps.append(temp_c)
        temp_f = Fahrenheit(temp_c)
        rapport = weerrapport(temp_c, windsnelheid, luchtvochtigheid)
        gem_temp = sum(temps) / len(temps)


        print(f"Het is {round(temp_c, 1)}C ({round(temp_f, 1)}F)")
        print(rapport)
        print(f"De gemiddelde temp tot nu toe is: {round(gem_temp, 1)}")
        print("=======================================================================")

    print("Programma klaar!")

weerstation()