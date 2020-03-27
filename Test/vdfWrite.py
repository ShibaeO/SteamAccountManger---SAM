#from PyVDF import PyVDF
#
#vdf = PyVDF()
#vdf.load("loginusers.vdf")
#
#vdf.edit("users.76561198822504212.MostRecent", "4")
#vdf.write_file("loginusers.vdf")
#User = vdf["users"]["76561198822504212"]
#State = vdf["users"]["76561198822504212"]["MostRecent"]
#print(User)
#
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


vdfGrabPseudo("j:/Steam", 76561198822504212)
#fix vdfGrabSteamId() qui trouve pas le steam id des name avec @
