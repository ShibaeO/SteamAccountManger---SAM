import winreg

# A pour but de changer deux valeurs dans le registre ("ActiveProcess") & ("AutoLoginUser")

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
    winreg.SetValueEx(regActiveUser, "ActiveUser", 0, winreg.REG_DWORD, accountValue)
    decValue, idex = winreg.QueryValueEx(regActiveUser, "ActiveUser")
    print(decValue)


def regQuerryCurrenLogged():
        regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
        account, index = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")
        return account
