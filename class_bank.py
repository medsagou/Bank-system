
from class_fichier import C_Fichier
from Modele_date import *
from Modele_date import Date
import numpy as np
from class_agence import Agence
from class_compte import Compte


class Bank:
    
    def __init__(self):
        self.bankname = 'FSTT Bank'
        self.separateur = ';'
        self.separateur2 = '+'
        self.separateur3 = ' '
    
    
        
    
    def nbr_clients_total(self):
        fichierClient = C_Fichier('db/compte.txt')
        print("Le nombre de clients: {}".format(fichierClient.nbre_ligne()))
        return
    
    def nbr_clients_par_agence(self):
        agenceFichier = C_Fichier('db/agence.txt', ';')
        listes_Agences = agenceFichier.Fichier_to_Liste()
        for i in range(len(listes_Agences)):
            L = agenceFichier.str_to_liste(listes_Agences[i].replace('\n',''))
            agence = Agence(L[0])
            agence.get_agence_info()
            agence.nbr_clients_agence()
        return
    def pourcentage_client_par_agence(self):
        agenceFichier = C_Fichier('db/agence.txt', ';')
        listes_Agences = agenceFichier.Fichier_to_Liste()
        dict_agence_nbr_client = {}
        nbr_total = 0
        for i in range(len(listes_Agences)):
            L = agenceFichier.str_to_liste(listes_Agences[i].replace('\n',''))
            agence = Agence(L[0])
            agence.get_agence_info()
            nbr = agence.nbr_clients_agence2()
            nbr_total += nbr
            dict_agence_nbr_client['ID : '+ str(agence.agence_id) + '\nVille : '+ agence.agence_ville +'\nNom: '+ agence.agence_name] = nbr
        for c,v in dict_agence_nbr_client.items():
            print(c,'Moyenne des Clients: '+ str((v/nbr_total)*100) + "%")
        return
    
    def frequence_ouverture_compte(self):
        
        agenceFichier = C_Fichier('db/agence.txt', ';')
        listes_Agences = agenceFichier.Fichier_to_Liste()
        for i in range(len(listes_Agences)):
            L = agenceFichier.str_to_liste(listes_Agences[i].replace('\n',''))
            agence = Agence(L[0])
            agence.get_agence_info()
            agence.frequence_ouverture_agence()
            
        return
    
    def moyenne_global_des_soldes(self):
        compteFichier = C_Fichier('db/compte.txt')
        L = compteFichier.Fichier_to_Liste()
        n = self.nbr_clients_total()
        amount = 0
        for i in range (len(L)):
            C = compteFichier.str_to_liste(L[i])
            amount += float(C[3])
        print("La moyenne global des soldes dans notre Banque est : {}".format(float(amount)/int(n)))
            
            
            
            
            
    def get_deposit_amount_periode(self):
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
                compteFichier = C_Fichier('db/compte.txt')
                L=compteFichier.Fichier_to_Liste()
                for i in range(len(L)) :
                    C = L[i].split(self.separateur)
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
                    print("Le montant global deposee entre {} et {} est : {:.2f} DH".format(start_date.DateToStr(), end_date.DateToStr(),sum_montants_par_period))
                else:
                    print("\nIl n'y a aucune operation de deposition entre {} et {} .".format(start_date.DateToStr(), end_date.DateToStr()))
                    
                        
                return
   

    def nomber_operation_par_mois_par_agence(self):
        agenceFichier = C_Fichier('db/agence.txt', ';')
        listes_Agences = agenceFichier.Fichier_to_Liste()
        departAnees = Date()
        departAnees.saisir_annee()
        for i in range(len(listes_Agences)):
            L = agenceFichier.str_to_liste(listes_Agences[i].replace('\n',''))
            agence = Agence(L[0])
            agence.get_agence_info()
            agence.nbr_operation_mois_agence(departAnees.an)
        return
    
    def get_deposit_amount_periode_par_agence(self):
        agenceFichier = C_Fichier('db/agence.txt', ';')
        listes_Agences = agenceFichier.Fichier_to_Liste()
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
            for i in range(len(listes_Agences)):
                L = agenceFichier.str_to_liste(listes_Agences[i].replace('\n',''))
                agence = Agence(L[0])
                agence.get_agence_info()
                agence.get_deposit_amount_periode_agence2(start_date,end_date)
        return
    
    
    
    def nomber_operation_par_mois(self):
        departAnees = Date()
        departAnees.saisir_annee()
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
        
        print('\nLe nombre des operation par mois en {}\n'.format(departAnees.an))
        for historiqueElement in historiques_liste:
            historiqueElementDate = Date()
            historiqueElementDate.StrToDate(historiqueElement[0])
            dict_mois[str(historiqueElementDate.mois)]+=1
        for c,v in dict_mois.items():
            if v!=0:
                print("==> "+ dict_mois_nom[c] +" : "+ str(v) +" operations")
            else:
                print("==> "+ dict_mois_nom[c] +" : aucune operation")
           
            
            
                    
                
                
         
         
         
    
    def meilleur_chiffre_par_mois():
        return
    
