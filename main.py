import winreg
from PyVDF import PyVDF

# A bout but de changer deux valeurs dans le registre ("ActiveProcess") & ("AutoLoginUser")

regActiveUser = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam\\ActiveProcess", access=winreg.KEY_ALL_ACCESS)

dataActiveUser1 = 862238484
dataActiveUser2 = 184418774

winreg.SetValueEx(regActiveUser, "ActiveUser", 0, winreg.REG_DWORD, dataActiveUser1)
decValue, idex = winreg.QueryValueEx(regActiveUser, "ActiveUser")
print(decValue)

dataStr1 = "antoineditlolotte"
dataStr2 = "sixthaccountcsgo"

regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(regLastLogin, "AutoLoginUser", 0, winreg.REG_SZ, dataStr2)
account, index = winreg.QueryValueEx(regLastLogin, "AutoLoginUser")
print("le compte acctuelement connecter est : " + account + " sa value decimal est : " + str(decValue))

# A pour but de changer le status dans le fichier ("loginusers.vdf") ce qui change le dernier utlisateur connectés

vdf = PyVDF()
vdf.load('loginusers.vdf')
vdf.edit("users.76561198822504212.MostRecent", "0")
vdf.write_file('loginusers.vdf')
User = vdf["users"]["76561198822504212"]
State = vdf["users"]["76561198822504212"]["MostRecent"]
print(User)
print(State)
