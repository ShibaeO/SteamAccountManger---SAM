import configparser

p = configparser.ConfigParser()
e = p.read("config.ini")

e = p.sections()
print(e)
while True:
    print(e)
    r = input('dd : ')
    g = int(r) - 1
    if r == r:
        g + 1
        print(e[g])
        #changeAccount(g) g qui est renvoie le nom du compte
