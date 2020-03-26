import configparser
import PySimpleGUI as sg
from infi.systray import SysTrayIcon
import ShibaeoUtlisLib as stl
import os
import ctypes
import webbrowser
import subprocess
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

#sections pour le parser qui recupère tout les compte pour la listBox

p = configparser.ConfigParser()
e = p.read("config.ini")
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
window = sg.Window('Steam account manager', layout, icon="icon.ico", no_titlebar=True, alpha_channel=1, grab_anywhere=True,)

#Creation du systemTray
menu_options = (("Show Window", None, shopwGUI),("Hide Window", None, hideGUI))
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options, on_quit=on_quit)


while True:
    systray.start()
    event, values = window.Read()
    if event is None:
        break
    elif event == '_BUTTON_KEY_':
        print(stl.listToString(values['_LISTBOX_']))
        sg.SystemTray.notify('Compte selectioner', stl.listToString(values['_LISTBOX_']))
    elif event == 'Exit':
        os._exit(0)
    elif event == "info":
        webbrowser.open('http://Shibaeo.quetel.pro/sam')
    elif event == 'Minimize':
        window.hide()
    elif event == "Steam path":
        text = sg.PopupGetFolder('Please enter a folder name')
        sg.Popup('Results', 'The value returned from PopupGetFolder', text)
    elif event == "Add Account":
        text = sg.popup_get_text('Title', 'Please input something')
        sg.popup('Results', 'The value returned from PopupGetText', text)
    elif event == "Reload app":
        stl.guiReload()


#theme :
#        Dark
#        DarkBlue2
#        DarkGrey
