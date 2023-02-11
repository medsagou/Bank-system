# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:32:20 2023

@author: Sagou
"""
from class_fichier import C_Fichier
from Modele_date import Date
from Modele_date import *
from class_menu import Menu
import numpy as np

class Agence:
    
    def __init__(self, agence_id="", agence_name = "", agence_ville = ""):
        self.agence_id = agence_id
        self.agence_ville = agence_ville
        self.agence_name = agence_name
        self.separateur = ';'
        self.separateur2 = '+'
        self.separateur3 = ' '
    
    
    def get_agence_info(self):
        if self.agence_id != "":
            agenceFichier = C_Fichier('db/agence.txt', ';')
            agence_id = self.agence_id
            agenceINFO = agenceFichier.existe_element_fichier3(str(agence_id))
            if agenceINFO[0]:
                L = agenceFichier.str_to_liste(agenceINFO[1].replace('\n',''))
                self.agence_ville = L[1]
                self.agence_name = L[2]
                return
            else:
                return
    def nbr_clients_agence(self):
        compteFichier = C_Fichier('db/compte.txt')
        L=compteFichier.Fichier_to_Liste()
        nbr_client = 0
        for i in range(len(L)) :
            C = L[i].split(self.separateur)
            if C[4] == self.agence_id:
                nbr_client += 1
        print('Nombre de client dans l\'agence {} : {} clients'.format(self.agence_name,nbr_client))
        return nbr_client
    def nbr_clients_agence2(self):
        compteFichier = C_Fichier('db/compte.txt')
        L=compteFichier.Fichier_to_Liste()
        nbr_client = 0
        for i in range(len(L)) :
            C = L[i].split(self.separateur)
            if C[4] == self.agence_id:
                nbr_client += 1
        return nbr_client
    
    def get_deposit_amount_periode_agence(self):
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
                self.get_deposit_amount_periode_agence2(start_date,end_date)
                    
                        
                return
    
    def get_deposit_amount_periode_agence2(self,start_date,end_date):
        amounts = []
        depot_text = 'Dépôt de'
        depot_historiques = []
           
        compteFichier = C_Fichier('db/compte.txt')
        L=compteFichier.Fichier_to_Liste()
        for i in range(len(L)) :
            C = L[i].split(self.separateur)
            if C[4] == self.agence_id:
                historiques = C[-1].split(self.separateur2)
                for historique in historiques:
                    if depot_text in historique:
                        depot_historiques.append(historique)
        
        for i in range(len(depot_historiques)):
            historique = depot_historiques[i].split(self.separateur3)
            
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
            print("\n ==> Agence: {} -----> Le montant deposee entre {} et {} est : {:.2f} DH".format(self.agence_name,start_date.DateToStr(), end_date.DateToStr(),sum_montants_par_period))
        else:
            print("\nIl n'y a aucune operation de deposition entre {} et {} .".format(start_date.DateToStr(), end_date.DateToStr()))
            
                
        return
    
    
    def nbr_operation_mois_agence(self, annee):
        
        self.get_agence_info()
        departAnees = Date()
        departAnees.saisir_annee2(annee)
        dict_mois = {'1':0,
                     '2':0,
                     '3':0,
                     '4':0,
                     '5':0,
                     '6':0,
                     '7':0,
                     '8':0,
                     '9':0,
                     '10':0,
                     '11':0,
                     '12':0 }
        dict_mois_nom = {'1':'janvier',
                     '2':'février',
                     '3':'mars',
                     '4':'avril',
                     '5':'mai',
                     '6':'juin',
                     '7':'juillet',
                     '8':'août',
                     '9':'septembre',
                     '10':'octobre',
                     '11':'novembre',
                     '12':'décembre' }
        finAnnees = Date()
        finAnnees.an = departAnees.an + 1
        finAnnees.mois = departAnees.mois
        finAnnees.jour = departAnees.jour
        
        historiques_liste = []
        compteFichier = C_Fichier('db/compte.txt')
        L=compteFichier.Fichier_to_Liste()
        for i in range(len(L)) :
            C = L[i].replace('\n','').split(self.separateur)
            if C[4] == self.agence_id:
                historiques = C[-1].split(self.separateur2)
                
                for j in range(len(historiques)):
                    historiqueCompte = historiques[j].split(self.separateur2)
                    
                    date_historique_object = Date()
                   
                    for i in range(len(historiqueCompte)):
                        historique = historiqueCompte[i].split(self.separateur3)
                        #print(historiqueCompte[i])
                        date_historique_object = Date()
                        date_historique = historique[0]
                        date_historique_object.StrToDate(date_historique)
                        
                        if comparer_Date(finAnnees, date_historique_object) and comparer_Date(date_historique_object, departAnees) :
                            historiques_liste.append(historique)
        
        print('\n===> Le nombre des operation par mois en {} dans L\'agence {}\n'.format(departAnees.an, self.agence_name))
        for historiqueElement in historiques_liste:
            historiqueElementDate = Date()
            historiqueElementDate.StrToDate(historiqueElement[0])
            dict_mois[str(historiqueElementDate.mois)]+=1
        for c,v in dict_mois.items():
            if v!=0:
                print("==> "+ dict_mois_nom[c] +" : "+ str(v) +" operations")
            else:
                print("==> "+ dict_mois_nom[c] +" : aucune operation")
        return
    
    def nbr_operation_mois_agence2(self):
        
        self.get_agence_info()
        departAnees = Date()
        departAnees.saisir_annee()
        self.nbr_operation_mois_agence(self, departAnees.an)
        return
    
    def frequence_ouverture_agence(self):
        ouverture_historique = []
           
        compteFichier = C_Fichier('db/compte.txt')
        L=compteFichier.Fichier_to_Liste()
        for i in range(len(L)) :
            C = L[i].split(self.separateur)
            if C[4] == self.agence_id:
                historiques = C[-1].split(self.separateur2)
                ouverture_historique.append(historiques[0])
        
        
        if ouverture_historique != []:
            print('\nFrequence d\'ouverture de compte dans l\'agence {} :'.format(self.agence_name))
            
            for i in range(len(ouverture_historique)):
                print('---> {}'.format(ouverture_historique[i]))
        else:
            print("\nIl n'y a aucune operation d'ouverture de compte dans l\'agence {} :".format(self.agence_name))
            
                
        return
        
    def choix_agence(self):
        agenceFcihier = C_Fichier('db/agence.txt')
        menuAgence = []
        L = agenceFcihier.Fichier_to_Liste()
        print('\n Choisir L\'agence: \n')
        for i in range(len(L)):
            agence = agenceFcihier.str_to_liste(L[i])
            menuAgence.append('ID : '+ agence[0] + '\nVille : '+ agence[1]+'\nNom: '+agence[2] )
            
        menu = Menu(menuAgence)
        choix = menu.afficher_menu()
        self.agence_id = L[choix].split(';')[0]
        self.agence_ville = L[choix].split(';')[1]
        self.agence_name = L[choix].split(';')[2]
        return
    
