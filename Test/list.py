import configparser
import PySimpleGUI as sg

p = configparser.ConfigParser()
e = p.read("config.ini")

e = p.sections()
#while True:
#    print(e)
#    r = input('dd : ')
#    g = int(r) - 1
#    if r == r:
#        g + 1
#        print(e[g])
#        #changeAccount(g) g qui est renvoie le nom du compte
#
#        #kill Steam
#        #recup regValue
#        #modifier regValue
#        #modifier vdf
#        #demarer steam
