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

#Command pour retirer le shell quand on lance l'app
#ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def long_operation_thread(popUpAccount):
    #config configparserMod recuper
    config = configparser.ConfigParser()
    config.read('config.ini')
    steamPath = config['config']['steamPath'].replace("/", "\\")
    current = config['config']['currentuser']

    #->   kill steam
    print("#->    Cheking steam thread status")
    if stl.checkIfProcessRunning("Steam"):
        stl.killSteam()
        print("#->    kill steam")
    else:
        print("#->    Steam Already stoped")
    time.sleep(3)
    stl.regModAutologin(popUpAccount)
    stl.regModRemPass(0)

    print("#->    lanching steam with {}".format(popUpAccount))
    stl.startWithAccount(steamPath, popUpAccount)
    time.sleep(30)
    print("#->    Adding usr in usr_db")
    stl.addIniAccount("usr_db.ini", popUpAccount, str(stl.regQuerryCurrenUser()), str(stl.vdfGrabSteamId(popUpAccount)), stl.pseudoToHex(popUpAccount))
    print("#->    reloading GUI")
    stl.guiReload()
    print("#->   Stopping Thread")

def the_gui():
    #sections pour le parser qui recupère tout les compte pour la listBox

    p = configparser.ConfigParser()
    e = p.read("usr_db.ini")
    e = p.sections()

    #section pour le systemTray pour un-hide la window et quiter le program

    def shopwGUI(systray):
        window.un_hide()

    def on_quit(systray):
        os._exit(0)

    def hideGUI(systray):
        window.hide()

    #section pour le layout, design de l'app

    sg.theme('Dark')

    menu_layout = [
    ['Menu', ['Add Account', 'Remove selected Account', '---', 'Minimize', 'Exit',]],
    ['setting', ['Steam path','Reload app']],
    ['About', ['info']],
    ]

    frame_layout = [
                     [sg.Listbox(values=e, size=(60, 10), no_scrollbar=True, select_mode="single", auto_size_text=True, key="_LISTBOX_", pad=(2/2, 5/1))],
                   ]

    layout =       [

                     [sg.Menu(menu_layout)],
                     [sg.Frame('Steam Account list', frame_layout, relief="solid", border_width="1")],
                     [sg.Button('Switch to selected account', key='_BUTTON_KEY_', border_width="0", button_color=("WHITE", "#27ae60"), focus=False, pad=((5, 15),(0,0)), size=(26,0)),sg.Button('Get info of selected account', focus=False, key='_BUTTON_KEY_', border_width="0", button_color=("WHITE", "#f1c40f"), pad=((6, 0),(0,0)), size=(26,0))]
                   ]

    #initialisation de la fenetre
    window = sg.Window('Steam account manager', layout, icon="icon.ico", no_titlebar=True, grab_anywhere=True,)

    #Creation du systemTray
    menu_options = (("Show Window", None, shopwGUI),("Hide Window", None, hideGUI))
    systray = SysTrayIcon("icon.ico", "Steam account manager", menu_options, on_quit=on_quit)

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
                thread = threading.Thread(target=long_operation_thread, args=(str(text),), daemon=True)
                thread.start()
                sg.SystemTray.notify('Adding :', stl.listToString(text))
        elif event == '_BUTTON_KEY_':
            print(stl.listToString(values['_LISTBOX_']))
            sg.SystemTray.notify('Compte selectioner', stl.listToString(values['_LISTBOX_']))
        elif event == 'Exit':
            break
        elif event == "info":
            webbrowser.open('http://Shibaeo.quetel.pro/sam')
        elif event == 'Minimize':
            window.hide()
        elif event == "Steam path":
            text = sg.PopupGetFolder('Please enter a folder name', no_titlebar=True, grab_anywhere=True,)
            sg.Popup('Results', 'The value returned from PopupGetFolder', text)
        elif event == "Reload app":
            stl.guiReload()
        elif event == "Remove selected Account":
            stl.accountIniRemove("usr_db.ini", stl.listToString(values['_LISTBOX_']))
            stl.guiReload()



    window.close()
    os._exit(0)



if __name__ == '__main__':
    the_gui()
    print('Exiting Program')
