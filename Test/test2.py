import ShibaeoUtlisLib as stl
import configparserMod as configparser
import struct
import binascii

config = configparser.ConfigParser()
config.read('usr_db.ini')
a2 = config['sixthaccountcsgo']['steampseudo']

popUpAccount = "sixthaccountcsgo"


#stl.addIniAccount("usr_db.ini", popUpAccount, str(stl.regQuerryCurrenUser()), str(stl.vdfGrabSteamId(popUpAccount)), stl.pseudoToHex(popUpAccount))



#str(binascii.hexlify(mm.encode("utf8")))

def pseudoToHex(popUpAccount):
    pseudo = stl.vdfGrabPseudo(stl.vdfGrabSteamId(popUpAccount))
    pseudoHex = binascii.hexlify(pseudo.encode("utf8"))
    pseudoHexStr = str(pseudoHex)
    return pseudoHexStr

def hexToPseudo(hex):
    a = hex
    a = a2.replace("'", "")
    a = a[1 : : ]
    clearPseudo = binascii.unhexlify(a).decode("utf8")
    return clearPseudo


print(hexToPseudo(a2))
