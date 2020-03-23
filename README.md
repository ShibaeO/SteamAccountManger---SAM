# Steam Account Manager

Logiciel développer en Python3, permettant de changer de compte rapidement sans rentrer le code Steam guard,
ce-ci est possible grâce au **`ConnectCache token`**, en effet en cochant **Remember my password** lors de la connexion au compte, il suffit de récupérer certains valeurs dans le registre Windows, et une modification dans un ficher de steam (**.VDF**). Ansi en faisant une sauvegarde simple de c'est valeur et en les modifiant cela permet une passage d'un compte a l'autre rapidement et en toute securité en effet le ***Steam Account Manager*** ne stock et récupère  aucun **Mot De Passe**.

## Exemple :

|Liste des valeurs | |
|--|--|
|\HKEY_CURRENT_USER\Software\Valve\Steam\ActiveProcess | ActiveUser = `3364b714` |
| \HKEY_CURRENT_USER\Software\Valve\Steam | AutoLoginUser = `Nom du compte` |
|\Steam\config\LoginUser.vdf|"MostRecent" = `"1"`|

## To-do :

 - [x] **Changer** valeur du registre & les récupérer
 - [x] **Changer** valeur .vdf & les récupérer
 - [x] Fichier pour **stocker** les compte
 - [x] **Ajouter** & **retirer** compte dans fichier
 - [x] **Afficher** avec menu simple tout les compte
 - [ ] **Kill** le processus de Steam
 - [ ] Fonction mère pour **Ajouter** un compte
 - [ ] Fonction mère pour **supprimer** un compte
 - [ ] Fonction mère pour **changer** de compte
 - [ ] **Crée** GUI

