import configparser

p = configparser.ConfigParser()

def accountIniRemove(file, section):
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.remove_section(section)
        configIni.seek(0)                          #Credit to : falsetru from https://stackoverflow.com/ for giving this code wiwh help me :)
        p.write(configIni)
        configIni.truncate()

def addIniAccount(file, section, accountName, accountValue, Hex, hexValue):
    with open(file, "r+") as configIni:
        p.read_file(configIni)
        p.add_section(section)
        p.set(section, accountName, accountValue)
        p.set(section, Hex, hexValue)
        configIni.seek(0)
        p.write(configIni)
        configIni.truncate()

addIniAccount("config.ini", "juelie", "accountName", "julie", "hexValue", "Hs2dq6")
accountIniRemove("config.ini", "juelie")
