# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 16:14:52 2023

@author: HP


### La Structure Global

La Stucture Global de Menu utilise dans ce project

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

"""
from class_compte import Compte
from class_bank import Bank
from class_menu import Menu
from class_client import Client
from class_agence import Agence


def main():
    aurevoir_msg = '''
                       _____                           _          
     /\               |  __ \                         (_)         
    /  \     _   _    | |__) |   ___  __   __   ___    _   _ __   
   / /\ \   | | | |   |  _  /   / _ \ \ \ / /  / _ \  | | | '__|  
  / ____ \  | |_| |   | | \ \  |  __/  \ V /  | (_) | | | | |     
 /_/    \_\  \__,_|   |_|  \_\  \___|   \_/    \___/  |_| |_|     
                                                                  
                                                                  
'''
    while True:
        
        start_menu = Menu()
        start_menu.get_menu_db('0')
        choix1 = start_menu.afficher_menu()
        
        if choix1 == 0:
            T = True
            while T == True:
                first_menu = Menu()
                first_menu.get_menu_db('00')
                choix2 = first_menu.afficher_menu()
                
                if choix2 == 0:
                    nvCompte = Compte()
                    nvCompte.choix_agence()
                    nvCompte.creer_compte()
                    
                    T2 = True
                    while T2 == True:
                        print('\n----> Operations disponible sur le Compte numero {}'.format(nvCompte.N_compte))
                        compte_menu = Menu()
                        compte_menu.get_menu_db('01')
                        choix3 = compte_menu.afficher_menu()
                        
                        if choix3 == 0:
                            nvCompte.deposer_argent()
                        elif choix3 == 1:
                            nvCompte.retirer_argent()
                        elif choix3 == 2:
                            nvCompte.transferer_argent()
                        elif choix3 == 3:
                            nvCompte.afficher_solde()
                        elif choix3 == 4:
                            nvCompte.afficher_proprietaires()
                        elif choix3 == 5:
                            nvCompte.afficher_historique()
                        elif choix3 == 6:
                            nvCompte.afficher_compte()
                        elif choix3 == 7:
                            confirmation = ['Feremer le compte','Annuler']
                            confiamtionMenu = Menu(confirmation)
                            choixConf = confiamtionMenu.afficher_menu()
                            if choixConf == 0:
                                nvCompte.fermer_compte()
                        elif choix3 == 8:
                            T2 = False
                        
                        elif choix3 == 9:
                            print(aurevoir_msg)
                            return
                        
                        
                elif choix2 == 1:
                    compte = Compte()
                    compte.get_compte()
                    T3 = True
                    while T3 == True:
                        print('\n----> Operations disponible sur le Compte numero {}'.format(compte.N_compte))
                        compte_menu = Menu()
                        compte_menu.get_menu_db('01')
                        choix3 = compte_menu.afficher_menu()
                        
                        if choix3 == 0:
                            compte.deposer_argent()
                        elif choix3 == 1:
                            compte.retirer_argent()
                        elif choix3 == 2:
                            compte.transferer_argent()
                        elif choix3 == 3:
                            compte.afficher_solde()
                        elif choix3 == 4:
                            compte.afficher_proprietaires()
                        elif choix3 == 5:
                            compte.afficher_historique()
                        elif choix3 == 6:
                            compte.afficher_compte()
                        elif choix3 == 7:
                            confirmation = ['Feremer le compte','Annuler']
                            confiamtionMenu = Menu(confirmation)
                            choixConf = confiamtionMenu.afficher_menu()
                            if choixConf == 0:
                                compte.fermer_compte()
                        elif choix3 == 8:
                            T3 = False
                        
                        elif choix3 == 9:
                            print(aurevoir_msg)
                            return
                elif choix2 == 2:
                    T = False
                elif choix2 == 3:
                    print(aurevoir_msg)
                    return
                
        elif choix1 == 1:
            T11 = True
            while T11 == True:
                bank_menu = Menu()
                bank_menu.get_menu_db('10')
                choix11 = bank_menu.afficher_menu()
                
                banque = Bank()
                client = Client()
                if choix11 == 0:
                    banque.nbr_clients_total()
                elif choix11 == 1:
                    banque.nbr_clients_par_agence()
                elif choix11 == 2:
                    banque.frequence_ouverture_compte()
                elif choix11 == 3:
                    client.montant_deposer_client_period()
                elif choix11 == 4:
                    banque.get_deposit_amount_periode_par_agence()
                elif choix11 == 5:
                    banque.get_deposit_amount_periode()
                elif choix11 == 6:
                    banque.nomber_operation_par_mois()
                elif choix11 == 7:
                    banque.nomber_operation_par_mois_par_agence()
                elif choix11 == 8:
                    T11 = False
                
                elif choix11 == 9:
                    print(aurevoir_msg)
                    return
                
        elif choix1 == 2:
            agence = Agence()
            agence.choix_agence()
            T21 = True
            while T21 == True:
                agence_menu = Menu()
                agence_menu.get_menu_db('20')
                choix21 = agence_menu.afficher_menu()
                
                if choix21 == 0:
                    nvCompte = Compte()
                    nvCompte.agence = agence.agence_id
                    nvCompte.creer_compte()
                elif choix21 == 1:
                    compte = Compte()
                    while True:
                        compte.get_compte()
                        if compte.agence == agence.agence_id:
                            break
                        else:
                            print('\n! Le numero de compte n\'existe pas dans notre agence !')
                    confirmation = ['Feremer le compte','Annuler']
                    confiamtionMenu = Menu(confirmation)
                    choixConf = confiamtionMenu.afficher_menu()
                    if choixConf == 0:
                        compte.fermer_compte()
                elif choix21 == 2:
                    compte = Compte()
                    while True:
                        compte.get_compte()
                        if compte.agence == agence.agence_id:
                            break
                        else:
                            print('\n! Le numero de compte n\'existe pas dans notre agence !')
                    compte.deposer_argent()
                    
                elif choix21 == 3:
                    compte = Compte()
                    while True:
                        compte.get_compte()
                        if compte.agence == agence.agence_id:
                            break
                        else:
                            print('\n! Le numero de compte n\'existe pas dans notre agence !')
                    compte.retirer_argent()
                elif choix21 == 4:
                    compte = Compte()
                    while True:
                        compte.get_compte()
                        if compte.agence == agence.agence_id:
                            break
                        else:
                            print('\n! Le numero de compte n\'existe pas dans notre agence !')
                    compte.transferer_argent()
                elif choix21 == 5:
                    compte = Compte()
                    while True:
                        compte.get_compte()
                        if compte.agence == agence.agence_id:
                            break
                        else:
                            print('\n! Le numero de compte n\'existe pas dans notre agence !')
                    compte.afficher_solde()
                elif choix21 == 6:
                    while True:
                        compte.get_compte()
                        if compte.agence == agence.agence_id:
                            break
                        else:
                            print('\n! Le numero de compte n\'existe pas dans notre agence !')
                    compte.afficher_historique()
                elif choix21 == 7:
                    agence.nbr_clients_agence()
                elif choix21 == 8:
                    agence.get_deposit_amount_periode_agence
                elif choix21 == 9:
                    agence.nbr_operation_mois_agence2()
                elif choix21 == 10:
                    T12 = False
                
                elif choix21 == 11:
                    print(aurevoir_msg)
                    return
                
        
        elif choix1 == 3:
            T3 = True
            while T3 == True:
                stat_menu = Menu()
                stat_menu.get_menu_db('30')
                choix4 = stat_menu.afficher_menu()
                banque = Bank()
                if choix4 == 0:
                    banque.nbr_clients_total()
                elif choix4 == 1:
                    banque.nbr_clients_par_agence()
                elif choix4 == 2:
                    banque.pourcentage_client_par_agence()
                elif choix4 == 3:
                    banque.moyenne_global_des_soldes()
                elif choix4 == 4:
                    banque.nomber_operation_par_mois()
                elif choix4 == 5:
                    banque.nomber_operation_par_mois_par_agence()
                elif choix4 == 6:
                    T3 = False
                elif choix4 == 7:
                    print(aurevoir_msg)
                    return
        elif choix1 == 5 or choix1 == 4:
            print(aurevoir_msg)
            return
    
    
        
if __name__ == "__main__":
    main()