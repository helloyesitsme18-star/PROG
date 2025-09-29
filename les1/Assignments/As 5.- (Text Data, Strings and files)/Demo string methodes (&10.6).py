tekst = input("Een zin? ")

tekst = tekst.strip()
print(tekst)

tekst = tekst.upper()
print(tekst)

tekst = tekst.lower()
print(tekst)

x = tekst.find("De")
y = tekst.split()
z = tekst.split("&")

nieuw = "#".join(y)
tekst = tekst.replace("o", "e")
print(x, y, z, nieuw, tekst, sep="\n")

text = '1-2-3-4'
parts = text.split('-')
for part in parts:
    print(part)

