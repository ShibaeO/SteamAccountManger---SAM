

# Steam Account Manager 1.7.4-beta ----> dont try to use it until release

Logiciel développer en Python3, permettant de changer de compte rapidement sans rentrer le code Steam guard,
ce-ci est possible grâce au **`ConnectCache token`**, en effet en cochant **Remember my password** lors de la connexion au compte, il suffit de récupérer certains valeurs dans le registre Windows, et une modification dans un ficher de steam (**.VDF**). Ansi en faisant une sauvegarde simple de c'est valeur et en les modifiant cela permet une passage d'un compte a l'autre rapidement et en toute securité en effet le ***Steam Account Manager*** ne stock et récupère  aucun **Mot De Passe**.

## Exemple :

|Liste des valeurs | |
|--|--|
|\HKEY_CURRENT_USER\Software\Valve\Steam\ActiveProcess | ActiveUser = `3364b714` |
| \HKEY_CURRENT_USER\Software\Valve\Steam | AutoLoginUser = `Nom du compte` |
|\Steam\config\LoginUser.vdf|"MostRecent" = `"1"`|

## Dependencies

 - `configparser==4.0.2 (Modified)`
 - `winreg`
 - `PyVDF==2.0.0`
 - `infi==0.0.1`
 - `infi.systray==0.1.12`
 - `PySimpleGUI 4.18.0`
 - `time`
 - `osv`
 - `ctypes`
 - `threading`
 - `webbrowser`
 - `PyVDF (forked by ProjectSky Modified by me)`


## To-do :

 - [x] **Changer** valeur du registre & les récupérer
 - [x] **Changer** valeur .vdf & les récupérer
 - [x] Fichier pour **stocker** les compte
 - [x] **Ajouter** & **retirer** compte dans fichier
 - [x] **Afficher** avec menu simple tout les compte
 - [x] **Kill** le processus de Steam
 - [x] Fonction mère pour **Ajouter** un compte
 - [x] Fonction mère pour **supprimer** un compte
 - [x] Fonction mère pour **changer** de compte
 - [x] **Crée** GUI
 - [ ] **Crée** installation
 - [ ] **Crée** onglet info de compte
 - [ ] finaliser en .exe et tout en un pour le partage
 
