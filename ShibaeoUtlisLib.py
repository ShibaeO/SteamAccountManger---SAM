def listToString(s):
    str1 = " "
    return (str1.join(s))


def vdfedit(mostRecentValue, steamPath):
    from PyVDFmod import PyVDF
    vdf = PyVDF(steamPath, mostRecentValue)
    vdf.load("{]\\config\\loginusers.vdf".format(steamPath))
    vdf.edit("users.76561198822504212.MostRecent", mostRecentValue)
    vdf.write_file("{]\\config\\loginusers.vdf".format(steamPath))

def vdfGrabSteamId(account):
    from PyVDFmod import PyVDF
    import configparserMod as configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    steamPath = config['config']['steamPath'].replace('"', '').replace("'", "")
    vdf = PyVDF()
    vdf.load("{}/config/config.vdf".format(steamPath))
    usr = vdf["InstallConfigStore.Software.Valve.Steam.Accounts.{}.SteamID".format(account)]
    return usr

def vdfGrabPseudo(steamId64):
        from PyVDFmod import PyVDF
        import configparserMod as configparser
        config = configparser.ConfigParser()
        config.read('config.ini')
        steamPath = config['config']['steamPath'].replace('"', '').replace("'", "")
        vdf = PyVDF()
        vdf.load("{}/config/loginusers.vdf".format(steamPath))
        pseudo = vdf["users.{}.PersonaName".format(steamId64)]
        return pseudo

def accountIniRemove(file, section):
    import configparserMod as configparser
    p = configparser.ConfigParser()
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.remove_section(section)
        configIni.seek(0)                          #Credit to : falsetru from https://stackoverflow.com/ for giving this code wiwh help me :)
        p.write(configIni)
        configIni.truncate()

def addIniAccount(file, accountId, hexValue, steamIdValue, steamPseudo):
    import configparserMod as configparser
    p = configparser.ConfigParser()
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.add_section(accountId)
        p.set(accountId, "accountName", accountId)
        p.set(accountId, "steamPseudo", steamPseudo)
        p.set(accountId, "steamid", steamIdValue)
        p.set(accountId, "hexValue", hexValue)
        p.set(accountId, "vacBanned", "False")
        p.set(accountId, "GameBanned", "False")
        configIni.seek(0)
        p.write(configIni)
        configIni.truncate()

def setIniValueValue(file, section, name, value):
    import configparserMod as configparser
    p = configparser.ConfigParser()
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.set(section, name, value)
        configIni.seek(0)
        p.write(configIni)
        configIni.truncate()

def regModAutologin(AccountName):
    import winreg
    regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regLastLogin, "AutoLoginUser", 0, winreg.REG_SZ, AccountName)
    regLastLogin = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")


def regModActiveUser(regValue):
    import winreg
    regModActiveUser = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam\\ActiveProcess", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regModActiveUser, "ActiveUser", 0, winreg.REG_DWORD, regValue)
    regModActiveUser = winreg.QueryValueEx(regModActiveUser, "ActiveUser")


def regModRemPass(value):
    import winreg
    regModRemPass = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(regModRemPass, "RememberPassword", 0, winreg.REG_DWORD, value)
    regModRemPass = winreg.QueryValueEx(regModRemPass, "RememberPassword")



def regQuerryCurrenLogged():
        import winreg
        regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
        CurrenLogged = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")
        return CurrenLogged




def regQuerryCurrenUser():
        import winreg
        regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam\\ActiveProcess", access=winreg.KEY_ALL_ACCESS)
        CurrenUser = winreg.QueryValueEx(regLastLogin, "ActiveUser")
        return CurrenUser

def regQuerryCurrenSteamPath():
        import winreg
        regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
        CurrenSteamPath = winreg.QueryValueEx(regLastLogin, "SteamPath")
        return CurrenSteamPath




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
        subprocess.Popen("main.py 1", shell=True)
        os._exit(0)

def killSteam():
    import os
    os.system("taskkill.exe /F /IM steam.exe")

def startWithAccount(SteamPath):
    import subprocess
    #subprocess.Popen("{}\\Steam.exe -login {} null".format(SteamPath, accountId), shell=True)
    subprocess.Popen("{}\\Steam.exe".format(str(SteamPath).replace("'", "").replace("/", "\\")), shell=True)

def pseudoToHex(popUpAccount):
    import binascii
    pseudo = vdfGrabPseudo(vdfGrabSteamId(popUpAccount))
    pseudoHex = binascii.hexlify(pseudo.encode("utf8"))
    pseudoHexStr = str(pseudoHex)
    return pseudoHexStr

def hexToPseudo(hex):
    import binascii
    a = hex
    a = a2.replace("'", "")
    a = a[1 : : ]
    clearPseudo = binascii.unhexlify(a).decode("utf8")
    return clearPseudo


#def addAccount(popUpAccount):
#    import configparserMod as configparser
#    import time
#    import binascii
#    import PySimpleGUI as sg
#    #config configparserMod recuper
#    config = configparser.ConfigParser()
#    config.read('config.ini')
#    steamPath = config['config']['steamPath'].replace("/", "\\")
#    current = config['config']['currentuser']
#
#    #->   kill steam
#    print("#->    kill steam")
#    killSteam()  #check si steam est open
#    time.sleep(3)
#    regModAutologin(popUpAccount)
#    regModRemPass(0)
#
#    print("#->    lancement steam")
#    startWithAccount(steamPath, popUpAccount)
#    print("#->    current est : " + current)
#    time.sleep(30)
#    print("#->    Ajout dans usr_db")
#    addIniAccount("usr_db.ini", popUpAccount, str(regQuerryCurrenUser()), str(vdfGrabSteamId(popUpAccount)), pseudoToHex(popUpAccount))
#    sg.SystemTray.notify('Compte Ajouter', listToString(popUpAccount))
#    #reload gui
#    window.un_hide()
#    guiReload()
