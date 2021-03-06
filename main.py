import os
import time
import ctypes
import threading
import webbrowser
import PySimpleGUI as sg
import ShibaeoUtlisLib as stl
from infi.systray import SysTrayIcon
import configparserMod as configparser

#Faire quelque chose pour les gens qui qui on leur steampath dans C:/Progra file (problem avec le fait qui est des espace)
#check si usr_db et config sont present est si non cree
#pour le reload gui chezck le nom du main et extension pour eviter de le changer a la main

#steam path check and set
config = configparser.ConfigParser()
config.read('config.ini')
sp = str(config['config']['steampath'].replace(",", "").replace("'", "").replace('"',''))
rsp = str(stl.regQuerryCurrenSteamPath()).replace(")", "").replace("(", "").replace("1", "").replace(",", "").replace("'", "").replace('"','')

if sp in rsp:
    print("#->     Steam Path is the same continue")
else:
    print("#->     Steam path has changed here the new one -> {} ".format(str(stl.regQuerryCurrenSteamPath())))
    stl.setIniValueValue('config.ini', 'config', "steampath", str(stl.regQuerryCurrenSteamPath()).replace(")", "").replace("(", "").replace("1", "").replace(",", ""))



#ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def mainAddAccount(popUpAccount):
    #config configparserMod recuper
    os.system("cls")
    config = configparser.ConfigParser()
    config.read('config.ini')
    steamPath = config['config']['steamPath']

    #->   kill steam
    print("#->     Cheking steam thread status")
    if stl.checkIfProcessRunning("Steam.exe"):
        stl.killSteam()
        print("#->     kill steam")
    else:
        print("#->     Steam Already stoped")

    print("#->     Cheking if {} is present in config.vdf".format(popUpAccount))
    if popUpAccount in stl.vdfSections():
        print("#->     {} is present ins config.vdf".format(popUpAccount))
        stl.vdfedit(stl.vdfGrabSteamId(popUpAccount))

    time.sleep(3)
    print("#->     Writing in registry of AutoLoginUser & RememberPassword")
    stl.regModAutologin(popUpAccount)
    stl.regModRemPass(0)

    print("#->     lanching steam with account :  {}".format(popUpAccount))
    stl.startWithAccount(steamPath)
    print("#->     Lancement Checker")
    while True:
        print("#->     Checking new compte")
        time.sleep(2)
        os.system("cls")
        if popUpAccount in stl.vdfSections():
            print("#->     {} is present ins config.vdf".format(popUpAccount))
            a = stl.vdfGrabSteamId(popUpAccount)
            b = stl.vdfGrabMostRecent(a)
            if b == "1":
                print("#->     Adding usr in usr_db")
                stl.addIniAccount("usr_db.ini", popUpAccount, str(stl.regQuerryCurrenUser()).replace(")", "").replace("(", "").replace("4", "").replace(",", ""), str(stl.vdfGrabSteamId(popUpAccount)), stl.pseudoToHex(popUpAccount))
                break
    print("#->     reloading GUI")
    stl.guiReload()
    print("#->     Stopping Thread")



def mainChangeAccount(name, value=None):
    os.system("cls")
    data = configparser.ConfigParser()
    data.read('usr_db.ini')
    config.read('config.ini')
    regHex = data[name]["hexvalue"]
    steamPath = config['config']['steamPath']

    currentLogged = str(stl.regQuerryCurrenLogged())


    print("#->     Cheking steam thread status")
    if stl.checkIfProcessRunning("Steam.exe"):
        stl.killSteam()
        print("#->     kill steam")
    else:
        print("#->     Steam Already stoped")

    print("#->     Modif registre")
    stl.regModActiveUser(int(regHex))
    stl.regModAutologin(str(name))

    print("#->     lanching steam with account :  {}".format(name))
    stl.startWithAccount(steamPath)
    while True:
        print("#->     Checking change")
        time.sleep(2)
        os.system("cls")
        if name in stl.vdfSections():
            print("#->     {} is present ins config.vdf".format(name))
            a = stl.vdfGrabSteamId(name)
            b = stl.vdfGrabMostRecent(a)
            if b == "1":
                if regHex in str(stl.regQuerryCurrenUser()).replace(")", "").replace("(", "").replace("4", "").replace(",", ""):
                    print("#->     Reghex didnt change")
                    break
                else:
                    value = str(stl.regQuerryCurrenUser()).replace(")", "").replace("(", "").replace("4", "").replace(",", "")
                    stl.setIniValueValue('usr_db.ini', name, "hexvalue", value)
                    print('#->     Reghex isnt the same, reghex changed to {}'.format(value))
                    break


        print("#->     Stopping Thread")


def the_gui():
    #sections pour le parser qui recupère tout les compte pour la listBox
    print("#->     Loading usr_db.ini")
    p = configparser.ConfigParser()
    e = p.read("usr_db.ini")
    e = p.sections()

    #section pour le systemTray pour un-hide la window et quiter le program

    def shopwGUI(systray):
        window.un_hide()
        print("#->     re-showing the window")

    def on_quit(systray):
        os._exit(0)

    def hideGUI(systray):
        window.hide()

    #section pour le layout, design de l'app

    sg.theme('Dark')

    menu_layout = [
    ['Menu', ['Add Account', 'Remove selected Account', '---', 'Minimize', 'Exit',]],
    ['setting', ['Steam path', 'Steam API key', 'Reload app']],
    ['About', ['info']],
    ]

    frame_layout = [
                     [sg.Listbox(values=e, size=(60, 10), no_scrollbar=True, select_mode="single", auto_size_text=True, key="_LISTBOX_", pad=(2/2, 5/1))],
                   ]

    layout =       [

                     [sg.Menu(menu_layout)],
                     [sg.Frame('Steam Account list', frame_layout, relief="solid", border_width="1")],
                     [sg.Button('Switch to selected account', border_width="0", button_color=("WHITE", "#27ae60"), focus=False, pad=((5, 15),(0,0)), size=(26,0)),sg.Button('Get info of selected account', focus=False, key='_BUTTON_KEY_', border_width="0", button_color=("WHITE", "#f1c40f"), pad=((6, 0),(0,0)), size=(26,0))]
                   ]

    #initialisation de la fenetre
    print("#->     setting up main window")
    window = sg.Window('Steam account manager', layout, icon="icon.ico", no_titlebar=True, grab_anywhere=True,)

    #Creation du systemTray
    print("#->     setting up systemTray")
    menu_options = (("Show Window", None, shopwGUI),("Hide Window", None, hideGUI))
    systray = SysTrayIcon("icon.ico", "Steam account manager", menu_options, on_quit=on_quit)
    print("#->     starting systemTray")
    print("#->     Starting window")

    thread = None

    while True:
        systray.start()
        event, values = window.read(timeout=200)
        if event in (None, 'Exit'):
            break
        elif event.startswith('Add') and not thread:
            config = configparser.ConfigParser()
            config.read('usr_db.ini')
            text = sg.popup_get_text('Please input desired Steam account :', 'get steam name', no_titlebar=True, grab_anywhere=True,)
            if text == None or "":
                print("#->     Exiting popup")
            elif text in config.sections():
                print("#->     conpte deja ajouter")
                sg.popup_error('Account already added', no_titlebar=True, grab_anywhere=True,)
            else:
                thread = threading.Thread(target=mainAddAccount, args=(str(text),), daemon=True)
                print("#->     Sarting addAccount thread")
                thread.start()
                sg.SystemTray.notify('Adding account :', stl.listToString(text))
        elif event.startswith('Switch') and not thread:
            currentLogged = str(stl.regQuerryCurrenLogged())
            value = str(values['_LISTBOX_']).replace("[", "").replace("]", "").replace("'", "")
            if value in currentLogged:
                print('#->     ERRROR : account Already connected ')
                sg.popup_error('Account already connected', no_titlebar=True, grab_anywhere=True,)
            else:
                thread = threading.Thread(target=mainChangeAccount, args=(str(value), str(value),), daemon=True)
                thread.start()
                print('#->     Changing account to : {}'.format(value))
                sg.SystemTray.notify('Changing account :', stl.listToString(values['_LISTBOX_']))
        elif event == 'Exit':
            print("#->     Stopping the app")
            break
        elif event == "info":
            print("#->     Opening info web page")
            webbrowser.open('http://Shibaeo.quetel.pro/sam')
        elif event == 'Minimize':
            print("#->     Minimizing window")
            window.hide()
        elif event == "Steam path":
            text = sg.PopupGetFolder('Please enter steam path if the actual one is different of yours', default_path=sp, no_titlebar=True, grab_anywhere=True,)
            stl.setIniValueValue("config.ini", "config", "steampath", str(text))
            stl.guiReload()
        elif event == "Steam API key":
            text = sg.popup_get_text('Please enter your steam API key to gain acces to some feature', no_titlebar=True, grab_anywhere=True,)
        elif event == "Reload app":
            print("#->     reloading GUI")
            stl.guiReload()
        elif event == "Remove selected Account":
            print("#->     removing user {} and reload GUI".format('_LISTBOX_'))
            stl.accountIniRemove("usr_db.ini", stl.listToString(values['_LISTBOX_']))
            sg.SystemTray.notify('Removing account :', stl.listToString(values['_LISTBOX_']))
            print("#->     removing user {} and reload GUI".format('_LISTBOX_'))
            stl.guiReload()



    window.close()
    os._exit(0)



if __name__ == '__main__':
    the_gui()
    print('Exiting Program')
