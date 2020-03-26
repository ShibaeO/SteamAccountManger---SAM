def listToString(s):
    str1 = " "
    return (str1.join(s))

def accountIniRemove(file, section):
    import configparser
    p = configparser.ConfigParser()
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.remove_section(section)
        configIni.seek(0)                          #Credit to : falsetru from https://stackoverflow.com/ for giving this code wiwh help me :)
        p.write(configIni)
        configIni.truncate()

def addIniAccount(file, section, accountName, accountValue, Hex, hexValue):
    import configparser
    p = configparser.ConfigParser()
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.add_section(section)
        p.set(section, accountName, accountValue)
        p.set(section, Hex, hexValue)
        configIni.seek(0)
        p.write(configIni)
        configIni.truncate()

def regModAutologin (AccountName):
    import winreg
    regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regLastLogin, "AutoLoginUser", 0, winreg.REG_SZ, AccountName)
    account, index = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")
    print("le compte acctuelement connecter est : " + account)


def regModActiveProcess (accountValue):
    import winreg
    regActiveUser = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam\\ActiveProcess", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regActiveUser, "ActiveUser", 0, winreg.REG_DWORD, accountValue)
    decValue, idex = winreg.QueryValueEx(regActiveUser, "ActiveUser")
    print(decValue)


def regQuerryCurrenLogged():
        import winreg
        regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
        account, index = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")
        return account

def guiReload():
        import subprocess
        import os
        subprocess.Popen("GUI.py 1", shell=True)
        os._exit(0)
