def namen():
    namen_dict = {}

    while True:
        naam = input(f'Volgende naam: ')
        if naam == '':
            for student in namen_dict:
                if namen_dict[student] == 1:
                    print(f'Er is 1 student met de naam {student}.')
                else:
                    print(f'Er zijn {namen_dict.get(student)} studenten met de naam {student}.')
            return


        if naam in namen_dict:
            aantal = namen_dict.get(naam)              #Aantal is hier een EXTRA variabele, dit hoeft niet.
            aantal += 1                                 # namen_dict[naam] += 1 is ook mogelijk
            namen_dict[naam] = aantal
        else:
            namen_dict[naam] = 1


namen()