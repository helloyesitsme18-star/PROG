cijferMOD = 8.2
cijferPROG = 7.8
cijferPROJA = 7.1

gemiddelde = (cijferMOD + cijferPROJA + cijferPROG) / 3
beloning = (cijferMOD + cijferPROJA + cijferPROG) * 30
overzicht = ('Mijn gemiddelde cijfer is een ' + str(round((gemiddelde),1))+ ' en mijn beloning wordt ' + str(round((beloning),1)) + ' euro!')

print(overzicht)