import winreg



regActiveUser = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam\\ActiveProcess", access=winreg.KEY_ALL_ACCESS)

dataActiveUser1 = 862238484
dataActiveUser2 = 184418774

winreg.SetValueEx(regActiveUser, "ActiveUser", 0, winreg.REG_DWORD, dataActiveUser2)
print(winreg.QueryValueEx(regActiveUser, "ActiveUser"))

dataStr1 = "antoineditlolotte"
dataStr2 = "sixthaccountcsgo"

regLastLogin = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam", access=winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(regLastLogin, "AutoLoginUser", 0, winreg.REG_SZ, dataStr1)
print(winreg.QueryValueEx(regLastLogin, "AutoLoginUser"))
