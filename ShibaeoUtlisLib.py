def listToString(s):
    str1 = " "
    return (str1.join(s))


def vdfedit(mostRecentValue, steamPath):
    from PyVDFmod import PyVDF
    vdf = PyVDF(steamPath, mostRecentValue)
    vdf.load("{]\\config\\loginusers.vdf".format(steamPath))
    vdf.edit("users.76561198822504212.MostRecent", mostRecentValue)
    vdf.write_file("{]\\config\\loginusers.vdf".format(steamPath))

def vdfGrabSteamId(steamPath, account):
    from PyVDFmod import PyVDF
    vdf = PyVDF()
    vdf.load("{}/config/config.vdf".format(steamPath))
    usr = vdf["InstallConfigStore.Software.Valve.Steam.Accounts.{}.SteamID".format(account)]
    print(usr)

def vdfGrabPseudo(steamPath, steamId64):
        from PyVDFmod import PyVDF
        vdf = PyVDF()
        vdf.load("{}/config/loginusers.vdf".format(steamPath))
        pseudo = vdf["users.{}.PersonaName".format(steamId64)]
        print(pseudo)

def accountIniRemove(file, section):
    import configparser
    p = configparser.ConfigParser()
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.remove_section(section)
        configIni.seek(0)                          #Credit to : falsetru from https://stackoverflow.com/ for giving this code wiwh help me :)
        p.write(configIni)
        configIni.truncate()

def addIniAccount(file, accountId, hexValue, steamIdValue):
    import configparser
    p = configparser.ConfigParser()
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.add_section(accountId)
        p.set(accountId, "accountName", accountId)
        p.set(accountId, "hexValue", hexValue)
        p.set(accountId, "vacBanned", "False")
        p.set(accountId, "GameBanned", "False")
        p.set(accountId, "steamId", steamIdValue)
        configIni.seek(0)
        p.write(configIni)
        configIni.truncate()

def setIniValue(file, section, value):
    import configparser
    p = configparser.ConfigParser()
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.set(section, "currentuser", value)
        configIni.seek(0)
        p.write(configIni)
        configIni.truncate()

def regModAutologin(AccountName):
    import winreg
    regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regLastLogin, "AutoLoginUser", 0, winreg.REG_SZ, AccountName)
    account, index = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")
    print("le compte acctuelement connecter est : " + account)


def regModActiveUser(accountValue):
    import winreg
    regActiveUser = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam\\ActiveProcess", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regActiveUser, "ActiveUser", 0, winreg.REG_DWORD, accountValue)
    decValue, idex = winreg.QueryValueEx(regActiveUser, "ActiveUser")
    print(decValue)

def regModRemPass(value):
    import winreg
    regActiveUser = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regActiveUser, "RememberPassword", 0, winreg.REG_DWORD, value)
    decValue, idex = winreg.QueryValueEx(regActiveUser, "RememberPassword")
    print(decValue)


def regQuerryCurrenLogged():
        import winreg
        regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
        account, index = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")
        return account

def regQuerryCurrenUser():
        import winreg
        regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam\\ActiveProcess", access=winreg.KEY_ALL_ACCESS)
        account, index = winreg.QueryValueEx(regLastLogin, "ActiveUser")
        return account



def checkIfProcessRunning(processName):
    import psutil
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def guiReload():
        import subprocess
        import os
        subprocess.Popen("GUI.py 1", shell=True)
        os._exit(0)

def killSteam():
    import os
    os.system("taskkill.exe /F /IM steam.exe")

def startWithAccount(SteamPath, accountId):
    import subprocess
    #subprocess.Popen("{}\\Steam.exe -login {} null".format(SteamPath, accountId), shell=True)
    subprocess.Popen("{}\\Steam.exe".format(SteamPath), shell=True)
