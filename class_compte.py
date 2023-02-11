# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:57:19 2023

@author: sagou
"""

from random import randint
from class_fichier import C_Fichier
from class_client import Client
from Modele_date import Date
from Modele_date import *
from class_menu import Menu
from class_agence import Agence
import numpy as np

class Compte():
    
    
    def __init__(self, N_compte = "", proprietaire = [], ct = 0, solde = 0, agence = ""):
        self.N_compte = N_compte
        self.proprietaire = proprietaire
        self.historique = []
        self.compte_type = ct
        self.agence = agence
        self.solde=solde
        self.compte_types = ["courant","épargne"]
        
    def compte_types_function(self):
        return self.compte_types[int(self.compte_type)]
    
    def choix_agence(self):
        agenceFcihier = C_Fichier('db/agence.txt')
        menuAgence = []
        L = agenceFcihier.Fichier_to_Liste()
        print('\n Choisir L agence: \n')
        for i in range(len(L)):
            agence = agenceFcihier.str_to_liste(L[i])
            menuAgence.append('ID : '+ agence[0] + '\nVille : '+ agence[1]+'\nNom: '+agence[2] )
            
        menu = Menu(menuAgence)
        choix = menu.afficher_menu()
        self.agence = L[choix].split(';')[0]
        return
        
        
        
    def deposit_period_compte(self):
        amounts = []
        depot_text = 'Dépôt de'
        depot_historiques = []
        while True:
            try:
                start_date = Date()
                print("\n Entrer la Date de depart :")
                start_date.saisirDate()
                
                end_date = Date()
                print("\n Entrer la Date de finale :")
                end_date.saisirDate()
                assert comparer_Date(end_date,start_date) != False # verifier si la date de depart et plus grand que la date finale.
            except AssertionError:
                print('\nDate de Depart est supieure ou egale a la date finale!!')
            else:
                 self.deposit_period_compte2(start_date, end_date)
                 return
             
    def deposit_period_compte2(self, start_date,end_date):
        amounts = []
        depot_text = 'Dépôt de'
        depot_historiques = []
        compteFichier = C_Fichier('db/compte.txt')
        L=compteFichier.Fichier_to_Liste()
        for i in range(len(L)) :
            C = L[i].split(';')
            if C[0] == self.N_compte:
                historiques = C[-1].split('+')
                for historique in historiques:
                    if depot_text in historique:
                        depot_historiques.append(historique)
        
        for i in range(len(depot_historiques)):
            historique = depot_historiques[i].split(" ")
            
            date_historique_object = Date()
            
            date_historique = historique[0]
            date_historique_object.StrToDate(date_historique)
            
            if comparer_Date(end_date, date_historique_object) and comparer_Date(date_historique_object, start_date) :
                
                try:
                     montant = float(historique[-1])
                except ValueError:
                    continue
                else:
                    amounts.append(montant)
        if amounts != []:
            sum_montants_par_period = np.sum(amounts)
            print("Le montant global deposee entre {} et {} par le compte {} est : {:.2f} DH".format(start_date.DateToStr(), end_date.DateToStr(),self.N_compte,sum_montants_par_period))
        else:
            print("\nIl n'y a aucune operation de deposition entre {} et {} .".format(start_date.DateToStr(), end_date.DateToStr()))
            
                
        return
             
    def get_compte(self):
        compteFichier = C_Fichier('db/compte.txt', ';')
        while True:
            try:
              compte_id = int(input("Entrer le Numero de Compte: "))
              assert compte_id >= 0
            except ValueError:
              print("! Veuillez saisir un nombre entier.\n")
            except AssertionError:
              print("! Le nombre saisi doit être supérieur ou égal à 0.\n")        
            else:
                compteINFO = compteFichier.existe_element_fichier3(str(compte_id))
                if compteINFO[0]:
                    L = compteFichier.str_to_liste(compteINFO[1].replace('\n',''))
                    self.N_compte = L[0]
                    self.proprietaire = compteFichier.str_to_liste2(L[1])
                    self.compte_type = L[2]
                    self.solde = float(L[3])
                    self.agence = L[4]
                    self.historique = compteFichier.str_to_liste2(L[5])
                    return
                else:
                    print("Le compte que vous avez tapee n'existe pas !!!")
                
        
        
    def get_compte2(self):
        compteFichier = C_Fichier('db/compte.txt', ';')
        if self.N_compte != '':
            compte_id = self.N_compte
            compteINFO = compteFichier.existe_element_fichier3(str(compte_id))
            if compteINFO[0]:
                L = compteFichier.str_to_liste(compteINFO[1].replace('\n',''))
                self.N_compte = L[0]
                self.proprietaire = compteFichier.str_to_liste2(L[1])
                self.compte_type = L[2]
                self.solde = float(L[3])
                self.agence = L[4]
                self.historique = compteFichier.str_to_liste2(L[5])
                return
            else:
                print("Le compte que vous avez tapee n'existe pas !!!")
        
                
            
    
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
    
    def afficher_proprietaires(self):
        for i in range(len(self.proprietaire)):
            print("---", self.proprietaire[i])
        return
        
    
    
    def afficher_solde(self):
        print(" - Solde: {}\n".format(self.solde))
        return
    def ajouter_proprietaire(self):
       """Ajouter proprietaire."""
       
       B = input("Est ce un compte de famille ? Tapez « O » ou « N »")
       proprietaire = input("Donner le nom du 1ème propriétaire : ")
       self.propriétaires.append(proprietaire)
       if( B == "O" ): # Si c'est un compte familial, nous allons demander le nom du 2ème propriètaire
          self.nature = 'familial'
          proprietaire2 = input("Donner le nom du 2ème propriétaire : ")
          self.propriétaires.append(proprietaire2)
       else:
          self.nature = 'personnel'
       
    def deposer_argent(self):
        date = Date()
        compteFichier = C_Fichier('db/compte.txt')
        while True:             
            try:
              montant = float(input("Entrer le solde a deposer en DH: "))
              assert montant >= 0
            except ValueError:
              print("! Veuillez saisir un nombre.\n")
            except AssertionError:
              print("! Le nombre saisi doit être supérieur ou égal à 0.\n")        
            else:
              self.solde += montant
              self.historique.append(str(date.date_now()) + " Dépôt de {}".format(montant))
              compteFichier.modiffier_ligne(self.N_compte,self.compte_to_str())
              print("Vous avez déposé {} sur le compte de {}.".format(montant,self.N_compte))
              break 
        return
    
    
    def deposer_argent2(self,montant):
        date = Date()
        self.solde += montant
        self.historique.append(str(date.date_now()) + " Dépôt de {}".format(montant))
            
        return
    
    def retirer_argent(self):
        date = Date()
        compteFichier = C_Fichier('db/compte.txt')
        while True:             
            try:
              montant = float(input("Entrer le solde a transferer en DH: "))
              assert montant >= 0 and montant < self.solde
            except ValueError:
              print("! Veuillez saisir un nombre.\n")
            except AssertionError:
              print("! Le nombre saisi doit être supérieur ou égal à 0 et inferieur ou égal a {} DH.\n".format(self.sold))        
            else:
              self.solde -= montant
              self.historique.append(str(date.date_now()) + " Retrait de {}".format(montant))
              compteFichier.modiffier_ligne(self.N_compte,self.compte_to_str())
              print("Vous avez retiré {} sur le compte de {}.".format(montant,self.N_compte))
              break 
        return
        
    def transferer_argent(self):
        date = Date()
        compte_destination = Compte()
        self.get_compte2()
        compteFichier = C_Fichier("db/compte.txt")
        
        while True:             
            try:
              montant = float(input("Entrer le solde a transferer en DH: "))
              assert montant >= 0 and montant < self.solde
            except ValueError:
              print("! Veuillez saisir un nombre.\n")
            except AssertionError:
              print("! Le nombre saisi doit être supérieur ou égal à 0 et inferieur ou égal a {} DH.\n".format(self.solde))        
            else:
              compte_destination.get_compte()
              self.solde -= montant
              self.historique.append(str(date.date_now()) + " Retirer de {}".format(montant))
              #print("Vous avez retiré {} sur le compte de {}.".format(montant,self.N_compte))
              
              compte_destination.deposer_argent2(montant)
              
              compteFichier.modiffier_ligne(compte_destination.N_compte,compte_destination.compte_to_str())
              compteFichier.modiffier_ligne(self.N_compte,self.compte_to_str())
              
              print("Vous avez transferee un montant de {} vers le compte {}".format(montant,compte_destination.N_compte))
              break
        return          
        
        
            
        
    
    def compte_to_str(self):
        compte=[]
        compteFichier = C_Fichier("db/compte.txt")
        compte.append(self.N_compte)
        C = compteFichier.Liste_to_Str2(self.proprietaire)
        compte.append(C)
        compte.append(self.compte_type)
        compte.append(self.solde)
        compte.append(self.agence)
        H = compteFichier.Liste_to_Str2(self.historique)
        compte.append(H)
        return compteFichier.Liste_to_Str1(compte)
        
    
    def afficher_compte(self):
        print("Informations du compte de {}:\n".format(self.N_compte))
        print("Numéro du compt : {}\n".format(self.N_compte))
        
        print("proprietaire : ")
        self.afficher_proprietaires()
        print("")
        
        print("Comtpte type: {}\n".format(self.compte_types_function()))
        agence = Agence(self.agence)
        agence.get_agence_info()
        print("Agence: {}\n".format(agence.agence_name))
        self.afficher_solde()
        self.afficher_historique()
    
        return
    
    def afficher_historique(self):
        print("Historique des transactions :")
        for transaction in self.historique:
            print("-->",transaction)
        return
    
    
    def fermer_compte(self):
        compteFichier = C_Fichier('db/compte.txt', ';')
        clientFichier = C_Fichier('db/client.txt', ';')
        
        ch = clientFichier.Fichier_to_str()
        if str("+" + self.N_compte + "+") in ch or str("+" + self.N_compte) in ch:
            ch = ch.replace("+" + self.N_compte,"",1)
            clientFichier.str_to_fichier(ch)
        elif str(self.N_compte + "+") in ch:
            ch = ch.replace(self.N_compte + "+","",1)
            clientFichier.str_to_fichier(ch)
        elif str(self.N_compte) in ch:
            clientFichier.supprimer_ligne_fichier2(self.N_compte)
            print('------------')
        compteFichier.supprimer_ligne_fichier(self.N_compte)
        print("Le compte {} a été fermé.".format(self.N_compte))
        return
