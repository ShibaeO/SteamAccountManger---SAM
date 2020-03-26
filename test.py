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
