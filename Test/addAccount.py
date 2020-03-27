import configparserMod as configparser
import time
import binascii
import PySimpleGUI as sg
import ShibaeoUtlisLib as stl

#config configparserMod recuper
config = configparser.ConfigParser()
config.read('config.ini')
steamPath = config['config']['steamPath'].replace("/", "\\")
current = config['config']['currentuser']

#->   kill steam
print("#->    kill steam")
stl.killSteam()  #check si steam est open
time.sleep(3)
stl.regModAutologin(popUpAccount)
stl.regModRemPass(0)

print("#->    lancement steam")
stl.startWithAccount(steamPath, popUpAccount)
print("#->    current est : " + current)
time.sleep(30)
print("#->    Ajout dans usr_db")
stl.addIniAccount("usr_db.ini", popUpAccount, str(stl.regQuerryCurrenUser()), str(stl.vdfGrabSteamId(popUpAccount)), stl.pseudoToHex(popUpAccount))
sg.SystemTray.notify('Compte Ajouter', stl.listToString(popUpAccount))
#reload gui

srl.guiReload()
