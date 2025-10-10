def aantal_dagen(inputFile):

    try:
        with open(inputFile) as bestand:
            regels = bestand.readlines()
            dagen = len(regels) - 1
            return dagen

    except FileNotFoundError:  #Als het deze foutmelding geeft crasht het bestand niet hierdoor en returnt hij -1
        return -1

def auto_bereken(inputFile, outputFile):
    

    with open(inputFile, 'r') as bestand1:
        regel = bestand1.readlines()[1:] #slaat de headerregel over dmv indexeren

    with open(outputFile, 'w') as bestand2:
        for dag in regel:
            data = dag.strip().split()

            datum = data[0]
            numPeople = int(data[1])
            tempSetpoint = float(data[2])
            tempOutside= float(data[3])
            precip = float(data[4])

            cv_stand = -1

            cvketel = tempSetpoint - tempOutside
            if cvketel >= 20:
                cv_stand = 100
            elif 10 <= cvketel < 20:
                cv_stand = 50
            elif cvketel < 10:
                cv_stand = 0

            ventilatie = numPeople + 1
            if ventilatie > 4:
                ventilatie = 4


            if precip < 3:
                bewatering = True
            elif precip >= 3:
                bewatering = False

            bestand2.write(f'{datum};{cv_stand};{ventilatie};{bewatering}\n')