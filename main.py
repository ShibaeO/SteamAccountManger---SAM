#!/usr/bin/python3
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

if rsp == sp:
    print("#->  Steam Path is the same continue")
else:
    print("#->    Steam path has changed here the new one -> {} ".format(str(stl.regQuerryCurrenSteamPath())))
    stl.setIniValueValue('config.ini', 'config', "steampath", str(stl.regQuerryCurrenSteamPath()).replace(")", "").replace("(", "").replace("1", "").replace(",", ""))


#Command pour retirer le shell quand on lance l'app
#ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def mainAddAccount(popUpAccount):
    #config configparserMod recuper
    config = configparser.ConfigParser()
    config.read('config.ini')
    steamPath = config['config']['steamPath']

    #->   kill steam
    print("#->    Cheking steam thread status")
    if stl.checkIfProcessRunning("Steam.exe"):
        stl.killSteam()
        print("#->    kill steam")
    else:
        print("#->    Steam Already stoped")

    print("#-> Cheking if {} is present in config.vdf".format(popUpAccount))
    if popUpAccount in stl.vdfSections():
        print("#->  {} is present ins config.vdf".format(popUpAccount))
        stl.vdfedit(stl.vdfGrabSteamId(popUpAccount))

    time.sleep(3)
    print("#->    Writing in registry of AutoLoginUser & RememberPassword")
    stl.regModAutologin(popUpAccount)
    stl.regModRemPass(0)

    print("#->    lanching steam with account :  {}".format(popUpAccount))
    stl.startWithAccount(steamPath)
    #si popUpAccount est deja dans login ou config alors quand on ajoute le compte ancien system pour les autre avec le most recent
    print("#->  Lancement Checker")
    while True:
        print("#->  Checking new compte")
        a = stl.vdfGrabSteamId("antoineditlolotte")
        b = stl.vdfGrabMostRecent(a)
        time.sleep(2)
        if b == "1":
            print("#->    Adding usr in usr_db")
            stl.addIniAccount("usr_db.ini", popUpAccount, str(stl.regQuerryCurrenUser()).replace(")", "").replace("(", "").replace("4", "").replace(",", ""), str(stl.vdfGrabSteamId(popUpAccount)), stl.pseudoToHex(popUpAccount))
            break
    print("#->    reloading GUI")
    stl.guiReload()
    print("#->   Stopping Thread")

    #check si regex du compte est vide et si vide suprime le compte et msg "ajout du compte failed"
    #check si le compte qu'on tente d'add est deja ajouter
    #trouver une autre moyen de detect la conenxion ou nouveau compte pour declancher l'enregistrement des valeurs
    #


def mainChangeAccount(name, value=None):
    data = configparser.ConfigParser()
    data.read('usr_db.ini')
    config.read('config.ini')
    regHex = data[name]["hexvalue"]
    steamPath = config['config']['steamPath']

    currentLogged = str(stl.regQuerryCurrenLogged())

    if name in currentLogged:
        print('#-> ERRROR : account Already connected ')
    else:
        print("#->    Cheking steam thread status")
        if stl.checkIfProcessRunning("Steam.exe"):
            stl.killSteam()
            print("#->    kill steam")
        else:
            print("#->    Steam Already stoped")

        print("#->  Modif registre")
        stl.regModActiveUser(int(regHex))
        stl.regModAutologin(str(name))

        print("#->    lanching steam with account :  {}".format(name))
        stl.startWithAccount(steamPath)

        print("#->    reloading GUI")
        stl.guiReload()
        print("#->   Stopping Thread")


def the_gui():
    #sections pour le parser qui recupère tout les compte pour la listBox
    print("#->    Loading usr_db.ini")
    p = configparser.ConfigParser()
    e = p.read("usr_db.ini")
    e = p.sections()

    #section pour le systemTray pour un-hide la window et quiter le program

    def shopwGUI(systray):
        window.un_hide()
        print("#->    re-showing the window")

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
    print("#->    setting up main window")
    window = sg.Window('Steam account manager', layout, icon="icon.ico", no_titlebar=True, grab_anywhere=True,)

    #Creation du systemTray
    print("#->    setting up systemTray")
    menu_options = (("Show Window", None, shopwGUI),("Hide Window", None, hideGUI))
    systray = SysTrayIcon("icon.ico", "Steam account manager", menu_options, on_quit=on_quit)
    print("#->    starting systemTray")
    print("#->    Starting window")

    thread = None

    while True:

        systray.start()

        event, values = window.read(timeout=200)
        if event in (None, 'Exit'):
            break
        elif event.startswith('Add') and not thread:
            text = sg.popup_get_text('Please input desired Steam account :', 'get steam name', no_titlebar=True, grab_anywhere=True,)
            if text == None or "":
                print("#->  Exiting popup")
            else:
                thread = threading.Thread(target=mainAddAccount, args=(str(text),), daemon=True)
                print("#->    Sarting addAccount thread")
                thread.start()
                sg.SystemTray.notify('Adding :', stl.listToString(text))
        elif event.startswith('Switch') and not thread:
            #print(stl.listToString(values['_LISTBOX_']))
            value = str(values['_LISTBOX_']).replace("[", "").replace("]", "").replace("'", "")
            thread = threading.Thread(target=mainChangeAccount, args=(str(value), str(value),), daemon=True)
            #print(type(value))
            #print(value)
            thread.start()
            sg.SystemTray.notify('Compte selectioner', stl.listToString(values['_LISTBOX_']))
        elif event == 'Exit':
            print("#->    Stopping the app")
            break
        elif event == "info":
            print("#->    Opening info web page")
            webbrowser.open('http://Shibaeo.quetel.pro/sam')
        elif event == 'Minimize':
            print("#->    Minimizing window")
            window.hide()
        elif event == "Steam path":
            text = sg.PopupGetFolder('Please enter steam path if the actual one is different of yours', default_path=sp, no_titlebar=True, grab_anywhere=True,)
            stl.guiReload()
        elif event == "Steam API key":
            text = sg.popup_get_text('Please enter your steam API key to gain acces to some feature', no_titlebar=True, grab_anywhere=True,)
        elif event == "Reload app":
            print("#->    reloading GUI")
            stl.guiReload()
        elif event == "Remove selected Account":
            print("#->    removing user {} and reload GUI".format('_LISTBOX_'))
            stl.accountIniRemove("usr_db.ini", stl.listToString(values['_LISTBOX_']))
            print("#->    removing user {} and reload GUI".format('_LISTBOX_'))
            stl.guiReload()



    window.close()
    os._exit(0)



if __name__ == '__main__':
    the_gui()
    print('Exiting Program')
