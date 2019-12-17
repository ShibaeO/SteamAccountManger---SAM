import winreg
from PyVDF import PyVDF

# A bout but de changer deux valeurs dans le registre ("ActiveProcess") & ("AutoLoginUser")

dataActiveUser1 = 862238484 #sixthaccountcsgo
dataActiveUser2 = 184418774 #antoineditlolotte
dataStr1 = "antoineditlolotte"
dataStr2 = "sixthaccountcsgo"
curentLoggedAccount = "antoineditlolotte"

def regModAutologin (AccountName):
    regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regLastLogin, "AutoLoginUser", 0, winreg.REG_SZ, AccountName)
    account, index = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")
    print("le compte acctuelement connecter est : " + account)


def regModActiveProcess (accountValue):
    regActiveUser = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam\\ActiveProcess", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regActiveUser, "ActiveUser", 0, winreg.REG_DWORD, dataActiveUser2)
    decValue, idex = winreg.QueryValueEx(regActiveUser, "ActiveUser")
    print(decValue)


def regQuerryCurrenLogged():
        regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
        account, index = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")
        return account

regModAutologin(dataStr1)

if regQuerryCurrenLogged() == curentLoggedAccount:
    print("compte deja conecter")
    print(regQuerryCurrenLogged())
else:
    print("compte switché")
    print(regQuerryCurrenLogged())

# A pour but de changer le status dans le fichier ("loginusers.vdf") ce qui change le dernier utlisateur connectés

#vdf = PyVDF()
#vdf.load('loginusers.vdf')
#vdf.edit("users.76561198822504212.MostRecent", "0")
#vdf.write_file('loginusers.vdf')
#User = vdf["users"]["76561198822504212"]
#State = vdf["users"]["76561198822504212"]["MostRecent"]
#print(User)
#print(State)
