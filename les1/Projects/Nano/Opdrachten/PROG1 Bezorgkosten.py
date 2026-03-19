def basis_bezorgkosten(afstandKM):
    if afstandKM < 0:
        return 4.50
    elif 0 <= afstandKM <= 10:
        return 4.50
    elif 10 < afstandKM <= 30:
        return (4.50 + ((afstandKM - 10) * 0.25))
    else:
        return -1


def definitieve_bezorgkosten(klanttype, spoed, afstandKM):
    prijs = basis_bezorgkosten(afstandKM)
    if prijs == -1:
        return -1

    if klanttype == "premium":
        return prijs * 0.8
    elif klanttype == "zakelijk":
        if afstandKM >= 5:
            return prijs * 0.9
        else:
            return prijs
    elif klanttype == "normaal":
        if spoed == True:
            return prijs + 3
        else:
            return prijs

def test_bezorg_functies():
    print(definitieve_bezorgkosten("premium", True, 31))
    print(definitieve_bezorgkosten("premium", True, 30))
    print(definitieve_bezorgkosten("premium", True, 10))
    print(definitieve_bezorgkosten("premium", True, 11))
    print(definitieve_bezorgkosten("zakelijk", True, 10))
    print(definitieve_bezorgkosten("zakelijk", True, 11))
    print(definitieve_bezorgkosten("zakelijk", True, 4))
    print(definitieve_bezorgkosten("zakelijk", True, 5))
    print(definitieve_bezorgkosten("normaal", False, 31))
    print(definitieve_bezorgkosten("normaal", True, 30))

#test_bezorg_functies()



