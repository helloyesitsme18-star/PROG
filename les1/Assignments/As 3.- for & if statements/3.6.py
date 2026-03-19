s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinker = ('aeiou')

for letter in s:
    if letter in klinker:
        print(letter)

