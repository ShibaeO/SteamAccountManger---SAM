import ShibaeoUtlisLib as stl
import configparser
import time

#config ConfigParser recuper
config = configparser.ConfigParser()
config.read('config.ini')
steamPath = config['config']['steamPath']
current = config['config']['currentuser']

#note dans config le curreznt User
stl.setIniValue("config.ini", "config", str(stl.regQuerryCurrenLogged()))

#variable diverse
popUpAccount = "antoineditlolotte"

#->   kill steam
print("#->    kill steam")
stl.killSteam()
stl.regModAutologin(popUpAccount)
stl.regModRemPass(0)

print("#->    lancement steam")
stl.startWithAccount(steamPath, popUpAccount)
print("#->    current est : " + current)
time.sleep(25)
stl.addIniAccount("usr_db.ini", popUpAccount, str(stl.regQuerryCurrenUser()), "dd")


#3364b714
