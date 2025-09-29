wordlist = ["appel", "doerian", "banaan", "doerian", "appel", "kers", "kers", "mango", "appel",
"appel", "kers", "doerian", "banaan", "appel", "appel", "appel", "appel", "banaan", "appel"]

dict = {}
for fruit in wordlist:
    if fruit in dict:
        dict[fruit] += 1
    else:
        dict[fruit] = 1

print(dict)
