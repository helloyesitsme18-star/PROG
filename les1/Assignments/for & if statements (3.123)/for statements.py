lst = [1,2,6,-1]
for cijfer in lst:
    absoluut = abs(cijfer)
    print(absoluut)

for letter in "banaan":
    print(letter)

for i in range(2,16,  2):  #1st and 2nd number to determine range (skips last number), 3rd number to take steps of 2
    print(i)
    # range generates a list/tuple
woord = 'banaan'
for index in range(0, len(woord), 2):
    print(woord[index])