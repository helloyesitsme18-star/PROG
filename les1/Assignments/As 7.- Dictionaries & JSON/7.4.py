import json

print(f'Dit zijn de lange namen, codes en types van elk station: ')
with open('stations.json') as bestand:
    data = json.load(bestand)
    stations = data['payload']       #maakt stations een dictionary met alle stations gelist in payload

for station in stations:
    print(f"{station['namen']['lang']:<25}  - {station['code']:<10}   : {station['stationType']}")


meest_oost = int()
station_oost = None

for station in stations:
    ver_oost = station['lng']
    if ver_oost > meest_oost:
        meest_oost = ver_oost
        station_oost = station['namen']['lang']


print(f'\n\nHet meest oostelijk gelegen station is: {station_oost}')




