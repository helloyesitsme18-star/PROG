def bereik(lst):
    maximum = max(lst)
    minimum = min(lst)
    resultaat = maximum - minimum
    return resultaat



result = bereik([1,2,3])          #Functies zoals deze, slaan het 'resultaat' op in het geheugen en dus print hij hem niet
print (result)
                                    #Als je 'm wilt printen moet je of printen, of returnen en het resultaat van return printen.
