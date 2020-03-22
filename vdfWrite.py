from PyVDF import PyVDF

vdf = PyVDF()
vdf.load("loginusers.vdf")

vdf.edit("users.76561198822504212.MostRecent", "4")
vdf.write_file("loginusers.vdf")
User = vdf["users"]["76561198822504212"]
State = vdf["users"]["76561198822504212"]["MostRecent"]
print(User)
print(State)
