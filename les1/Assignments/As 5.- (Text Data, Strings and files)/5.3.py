def grootkaartnr_print():
    """

    Returns:
        string:
        Deze file telt 6 regels
Het grootste kaartnummer is: 645345 en dat staat op regel 4
    """
    bestand = open('oefening_5_2_generated.txt')
    regels = bestand.readlines()
    aantal_regels = len(regels)

    max_kaartnr = 0
    regelnr = 1
    regel_max = 0


    for regel in regels:

        kaartnr, naam = regel.strip().split(', ')
        kaartnr = int(kaartnr)

        if kaartnr > max_kaartnr:
            max_kaartnr = kaartnr
            regel_max = regelnr

        regelnr = regelnr + 1



    resultaat = f'Deze file telt {aantal_regels} regels\nHet grootste kaartnummer is: {max_kaartnr} en dat staat op regel {regel_max}'
    bestand.close()
    return resultaat

print(grootkaartnr_print())







