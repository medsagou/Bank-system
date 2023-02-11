# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:20:07 2023

@author: HP
"""

from class_fichier import C_Fichier
from class_compte import Compte
from Modele_date import Date
from Modele_date import *

class Client:
    
    def __init__(self, cin="", nom="", prenom="", adresse="",comptes = []):
        self.nom = nom
        self.prenom = prenom
        self.cin = cin
        self.adresse = adresse
        self.comptes = []
    
    
    def montant_deposer_client_period(self):
        self.get_client()
        
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
                print('Le montant deposee par Mr. {}'.format(self.Nom+" " +self.prenom))
                for i in range(len(self.comptes)):
                    compte = Compte(self.comptes[i])
                    compte.get_compte2()
                    compte.deposit_period_compte2(start_date,end_date)
        return
    
    def get_client(self):
            clientFichier = C_Fichier('db/client.txt', ';')
            while True:
                try:
                  client_cin = input("Entrer le CIN de Client: ")
                  assert len(client_cin) >= 3
                except AssertionError:
                  print("! Le CIN inserer est invalid !.\n")        
                else:
                    client = clientFichier.existe_element_fichier3(str(client_cin))
                    if client[0]:
                        L = clientFichier.str_to_liste(client[1].replace('\n',''))
                        self.cin = L[0]
                        self.nom = L[1].split(" ",1)[0]
                        self.prenom = L[1].split(" ",1)[1]
                        self.adresse = L[2]
                        self.comptes = clientFichier.str_to_liste2(L[3])
                        break
                    else:
                        print("Le CIN que vous avez tapee n'existe pas !!!")
                        
    def get_client2(self):
            clientFichier = C_Fichier('db/client.txt', ';')
            if self.cin != '':
                client = clientFichier.existe_element_fichier3(str(self.cin))
                if client[0]:
                    L = clientFichier.str_to_liste(client[1].replace('\n',''))
                    self.cin = L[0]
                    self.nom = L[1].split(" ",1)[0]
                    self.prenom = L[1].split(" ",1)[1]
                    self.adresse = L[2]
                    self.comptes = clientFichier.str_to_liste2(L[3])
                    
                        
    def get_client_informations(self):
        while True:
                
            try:
                cin =input("Entrer le cin du client : ")
                assert len(cin) > 3;
            except AssertionError:
                print('\nLe cin n\'est pas valid!')
            else:
                self.cin = cin
                break
        while True:
                
            try:
                nom =input("Entrer le nom du client : ")
                assert len(nom) > 3;
            except AssertionError:
                print('\nLe nom n\'est pas valid!')
            else:
                self.nom = nom
                break
        
        while True:
                
            try:
                prenom =input("Entrer le prenom du client : ")
                assert len(prenom) > 3;
            except AssertionError:
                print('\nLe prenom n\'est pas valid!')
            else:
                self.prenom = prenom
                break
                
        while True:
                
            try:
                adresse =input("Entrer le adresse du client : ")
                assert len(adresse) > 3;
            except AssertionError:
                print('\nLe adresse n\'est pas valid!')
            else:
                self.adresse = adresse
                break    
    
    def afficher_client_information(self):
        print('CIN: {}\nNom: {} \nPrenom: {}\nAdresse: {}\nComptes:'.format(self.cin,self.nom,self.prenom,self.adresse))
        if self.comptes != []:
            for i in range(len(self.comptes)):
                print('---> {}'.format(self.comptes[i]))
    
 