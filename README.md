
# Bank system
Bank system with Python, using txt files as a database.

This project implements a comprehensive banking system with python to manage customer accounts and perform various operations such as opening an account, depositing money, withdrawing money, transferring money, capitalizing account, and consulting account history. The system comprises of accounts, owners, branches, and operations that support multiple types of accounts and currency exchange. The bank can track various statistics, including customer information, deposit amounts, and branch performance.


## Author

- [@Mohamed Sagou](https://www.github.com/medsagou)


## Screenshots

![Screenshot](/demo.JPG)


## Usage/Examples

```python
def creer_compte(self):
        compteFichier = C_Fichier('db/compte.txt', ';')
        clientFichier = C_Fichier('db/client.txt', ';')
        client = Client()
        date = Date()
        
        
        while(True):
            N =  str(randint(1000000, 9999999))
            T = compteFichier.existe_element_fichier2(N)
            if not T:
                self.N_compte = N
                self.historique.append(str(date.date_now()) + " Creation de Compte")
                break
        
        client.get_client_informations()
        T = clientFichier.existe_element_fichier3(client.cin)
        if T[0]:
            clientInf = clientFichier.str_to_liste(T[1])
            comptes_id = clientFichier.str_to_liste2(clientInf[-1])
            comptesINF = []
            for i in range(len(comptes_id)):
                compteINFO = compteFichier.existe_element_fichier3(comptes_id[i])
                comptesINF.append(compteINFO[1])
            for i in range(len(comptesINF)):
                L = compteFichier.str_to_liste(comptesINF[i].replace('\n',''))
                if self.agence in L:
                    self.N_compte = L[0]
                    self.proprietaire = compteFichier.str_to_liste2(L[1])
                    self.compte_type = L[2]
                    self.solde = L[3]
                    self.agence = L[4]
                    self.historique = compteFichier.str_to_liste2(L[5])
                    
                    
                    print("\nVous avez deja un compte dans notre agence, information sur le compte :\n")
                    self.afficher_compte() 
                    return
            #si le client n'a pas de compte dans notre agence
            print("\nVous avez deja un compte dans une autre agence, voulez-vous continuer? \n")
            menu_continue = Menu(["continue", "Quitter"])
            C = int(menu_continue.afficher_menu())
            if C == 1:
                return
        self.proprietaire = [str(client.nom) +" "+ str(client.prenom)]
        self.deposer_argent()
        
        menu_compte_type = Menu(self.compte_types)
        self.compte_type = int(menu_compte_type.afficher_menu())
        
        print("\n-------Votre compte a ete bien creer!! , Merci Pour Votre Confiance -------\n")
        print("Les information De Votre Compte :\n")
        self.afficher_compte()
        
        
        #enregistrer les information,
        if T[0]:
            clientFichier.ajouter_a_la_fin_de_la_ligne(client.cin,self.N_compte,"+")
        else:
            clientList = [client.cin, str(client.nom) + " " + str(client.prenom),client.adresse,self.N_compte]
            compteList = [self.N_compte,compteFichier.Liste_to_Str2(self.proprietaire) ,self.compte_type,self.solde,self.agence,compteFichier.Liste_to_Str2(self.historique)]
            
            clientFichier.Liste_to_str_to_Fichier(clientList)
            compteFichier.Liste_to_str_to_Fichier(compteList)
            return
        
        return
```

# How to use gulp v3 and v4 on your sass files - Underscores the starter theme folder - Mohamed Sagou

This tutorial will show you how to install gulp on your project and how to use it in the right way. If you are usint underscores starter theme folder, in this folder you will find the right methode to use gulp in your project.

## Table of contents
- [Author](#author)



### Menus Structure

This is the menu structure that we used in this project,
```
.
└── Main program
    ├── Gestion de Compte
    │   ├── Creer un nouvau compte
    │   ├── Accéder à un compte
    │   ├── Retour 
    │   └── Quitter
    │
    │
    ├── Banque
    │   ├── Nombre total de clients
    │   ├── Nombre de clients par agence
    │   ├── Frequence d'ouverture de compte
    │   ├── Montant déposé par un client durant une période
    │   ├── Montant déposé dans chaque agence durant une période
    │   ├── Montant depose globalement dans toutes les agences durant une période
    │   ├── Nombre d'opérations / mois
    │   ├── Nombre d'opérations / mois pour chaque agence
    │   ├── Retour 
    │   └── Quitter
    │
    │
    ├── Agence
    │   ├── Ouvrir un compte pour un client
    │   ├── Fermer un compte pour un client dans notre agence
    │   ├── Déposer de l'argent dans le compte d'un client
    │   ├── Retirer de l'argent du compte d'un client
    │   ├── Transférer de l'argent d'un compte à un autre compte
    │   ├── Afficher le solde d'un compte d'un client
    │   ├── Consulter l'historique d'un compte d'un client
    │   ├── Afficher le nombre de clients de l'agence
    │   ├── Afficher le montant déposé par les clients de l'agence durant une période
    │   ├── Afficher le nombre total des opérations effectuées par les clients de l'agence par mois
    │   ├── Retour 
    │   └── Quitter
    │
    │
    └── Statistiques
        ├── Nombre des clients Total
        ├── cNombre des clients par Agence
        ├── Pourcentage des clients par Agence
        ├── La moyenne des soldes des comptes
        ├── Nombre des operation par mois
        ├── Nombre des operation par mois par agence
        ├── Retour 
        └── Quitter
```


### Directory Structure

```
.
└── Dossier du programme
    │  
    ├── db (data base)
    │   ├── agence.txt
    │   ├── bank_historique.txt
    │   ├── client.txt
    │   ├── compte.txt
    │   └── menu.txt
    │
    ├── All.py
    │  
    ├── class_agence.py
    │  
    ├── class_bank.py
    │  
    ├── class_client.py
    │  
    ├── class_compte.py
    │  
    ├── class_fichier.py
    │  
    ├── class_menu.py
    │  
    ├── main.py
    │  
    ├── Modele_date.py
    │  
    ├── Module_Classe_Liste.py
    │  
    ├── main.py
    │    
    ├── Agence
    │
    └── README.txt (Ce Fichier)
```




## Author

- Website - [@medsagou](https://github.com/medsagou)
- Frontend Mentor - [@medsagou](https://www.frontendmentor.io/profile/medsagou)
- Twitter - [@sagoumohamed](https://www.twitter.com/sagoumohamed)
- stackoverflow - [@medsagou](https://stackoverflow.com/users/19887099/mohamed-sagou)
