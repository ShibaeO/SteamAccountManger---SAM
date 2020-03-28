import ShibaeoUtlisLib as stl
import configparser
import time

#config ConfigParser recuper
config = configparser.ConfigParser()
config.read('config.ini')
steamPath = config['config']['steamPath']

#note dans config le curreznt User
stl.setIniValue("config.ini", "config", str(stl.regQuerryCurrenLogged()))

#variable diverse
popUpAccount = "antoineditlolotte"
oldAccount = "sixthaccountcsgo"

#->   kill steam
print("#->    kill steam")

if stl.checkIfProcessRunning("Steam.exe"):
    stl.killSteam()


stl.regModAutologin(popUpAccount)
stl.regModRemPass(0)
time.sleep(3)

current = config['config']['currentuser']
print(current)

#programe
print("#->    lancement steam")

stl.startWithAccount(steamPath, popUpAccount)
time.sleep(2)
stl.regModAutologin(oldAccount)
print("#->    current est : " + current)

while True:
    #print("current est : " + current + "reg est : " + stl.regQuerryCurrenUser())
    if stl.regQuerryCurrenLogged() == current:
        None
    else:
        time.sleep(5)
        print(stl.regQuerryCurrenLogged())
        time.sleep(10)
        stl.addIniAccount("usr_db.ini", popUpAccount, str(stl.regQuerryCurrenUser()), "dd")
        break

#3364b714


# au dessus caca
# en dessous bien

import ShibaeoUtlisLib as stl
import time

#b = stl.vdfGrabSteamId("antoineditlolotte")
#a = stl.vdfGrabMostRecent(b)
#
#if a == "1":
#    print("ouii")

#print(stl.vdfGrabSteamId("antoineditlolotte"))

#while True:
#    a = stl.vdfGrabSteamId("antoineditlolotte")
#    print(a)
#    b = stl.vdfGrabMostRecent(a)
#    time.sleep(2)
#    if b == "1":
#        print("#->    Adding usr in usr_db")
#        break

#stl.vdfedit("76561198144684502")


if "antoineditlolotte" in stl.vdfSections():
    print("#->  {} Est deja dans present")
    stl.vdfGrabSteamId("antoineditlolotte")
    stl.vdfedit(stl.vdfGrabSteamId("antoineditlolotte"))

if popUpAccount in stl.vdfSections():
    print("#->  {} Est deja dans present")
    stl.vdfGrabSteamId(popUpAccount)
    stl.vdfedit(stl.vdfGrabSteamId(popUpAccount))
