
"""
Il est recommandé d'utiliser le dossier du programme "Bank system/main.py" plutôt que le fichier All.py pour une utilisation optimale du système.

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




# =============================================================================
# Modele List
# =============================================================================

class C_Liste(list):
    
    def __init__(self,sep=';'):
        self.separateur = sep
    
    def afficher_Liste(self):
        for i in range(len(self)):
            print(self[i],'\n')
    
    def Str_to_List(self,Ligne_Chaine):
        return Ligne_Chaine.split(self.separateur) 
    
    def Liste_to_Str(self,Liste_Elements):
        return self.separateur.join(Liste_Elements) 

    def changer_element(self,E):
        Liste_Tempo=[]
        for i in range(len(self)):
            Element_courant=self[i]
            if E != Element_courant:
               Liste_Tempo=Liste_Tempo + [Element_courant]
            else:               
                print("Veuillez saisir un élément à la place de : ",E,"\n")
                E_modifie= input("Veuillez saisir un élément : ")
                Liste_Tempo=Liste_Tempo + [E_modifie]
        return Liste_Tempo 
# =============================================================================
# Class Fichier
# =============================================================================

import os
import os.path
from os import chdir, mkdir

class C_Dossier():

   
    def __init__(self,sep=""):
       self.separateur=sep
    
    def dossier_courant():
        return os.getcwd()

    def existe_dossier(Chemin):
        if os.path.exists(Chemin) :
            return True
        else:
            return False 
        
    def changer_dossier(Chemin):
        if C_Dossier.existe_dossier(Chemin):
            return(chdir(Chemin))
 
        
    def creer_dossier(Chemin):
        if not C_Dossier.existe_dossier(Chemin):
             return(mkdir(Chemin))
         
            
import os.path
from Module_Classe_Liste import C_Liste
            

class C_Fichier():
    #____________________________________________________________________________________________________________________________________________________________
    # Le constructeur d'une instance d'un fichier
    # Ce constructeur permet d'attribuer à une instance de fichier son nom (vide par défaut) 
    # Ce constructeur permet de spécifier le séparateur des éléments s'il existe (également vide par défauté)su
    # Un séparateur peut être un ";", une "," un "#', etc.  
    def __init__(self,NF="",sep=";", sep2="+"):
        self.nomFichier=NF
        self.separateur=sep
        self.separateur2=sep2
    
    #____________________________________________________________________________________________________________________________________________________________
    # Vérifie si un fichier exite ou non.
    def existe_fichier(self):
         if os.path.isfile(self.nomFichier):
             return True
         else:
             return False
    #____________________________________________________________________________________________________________________________________________________________
    # Vérifie si un fichier exite ou non.
    def specifier_Nom_fichier(self):
        while True:
            print("\n")
            print("Instanciation et saisie d'un nouveau fichier de travail :\n")
            self.nomFichier=input("Entrez le chemin de votre fichier : "+"\n")
            if self.existe_fichier():
                print("le fichier spécifié existe déjà dans le répertoire courant, veuillez recommencer")
            else:
                break  
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide sans supprimer le fichier de même nom s'il existe
    def creer_fichier_1(self):
        f = open(self.nomFichier,"x") #Création d'un fichier vide. Ici, le fichier n'est pas écrasé contrairement au mode 'w'  
        f.close()
    
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide avec suppression du fichier de même nom s'il existe
    def creer_fichier_2(self):
        f = open(self.nomFichier,"w") #Création d'un fichier vide. Ici, le fichier existant qui porte le même nom est écrasé contrairement mode 'x'  
        f.close()
    
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide avec possibilité de dialogue avant de supprimer un fichier de même nom s'il existe dans le même répertoire (dossier)
    def creer_fichier_3(self):
        if os.path.exists(self.nomFichier):         # Condition pour vérifier si jamais le fichier à créer existe déjà dans le répertoire courant
            print("Il existe un fichier qui porte le même nom"+"\n")
            print("Voulez-vous l'écraser ?")
            while True:                             # Itération (boucle infinie) pour prévenir les événetuelles erreurs de frappe (autre chose que '1' et '2') (Attention, il faut absolument provoquer quelque part dans la boucle une rupture avec "break" )
                # Menu local pour exposer les dexu cas de figures (on peut également créer une instance de la classe Menu ici)
                print("Veuillez choisir ce qu'il faut faire, selon les options suivantes : "+"\n")
                print("1. Ecraser le fichier existant")
                print("2. Garder le fichier")
                rep=input("Veuillez taper 1 ou 2 ")
                if rep=='1':                        # Cas où l'utilisateur choisit d'écraser le fichier existant 
                    self.creer_fichier_2()          # Appel à laméthode creer_fichier_2()
                    break                           # rupture de la boucle d'itération => on sort de la boucle infinie while
                elif rep=='2':                      # Cas où l'utilisateur choisit de ne pas écraser le fichier existant (pas besoin dans ce cas de faire appel à la méthode creer_fichier_1()) 
                    break                           # rupture de la boucle d'itération => on sort de la boucle infinie while
                else:                               # cas où l'utilisateur n'a tapé ni "1", ni"2"
                    print("Erreur de frappe"+"\n")
        else:                                       # cas où le fichier à créer n'existe pas dans le répertoire courant
            self.creer_fichier_1()                  # Appel à laméthode creer_fichier_1()
    
    #____________________________________________________________________________________________________________________________________________________________
    def ActiverFichier(self,Message):
        print(Message)
        self.specifier_Nom_fichier()
        self.creer_fichier_3()                      
 
    #____________________________________________________________________________________________________________________________________________________________
    # Supprimer un fichier
    def supprimer_fichier(self):
        if os.path.exists(self.nomFichier):         # Condition pour vérifier si jamais le fichier à créer existe déjà dans le répertoire courant
            os.remove(self.nomFichier)
            print("Le fichier a été supprimé")
        else:
            print("Le fichier spécifié n'existe pas dans le répertoire courant")

    #____________________________________________________________________________________________________________________________________________________________
    # Ajouter un élément
    def enregistrer_Element(self,Element):
        with open(self.nomFichier,'a') as F:   # Ouverture du fichier en mode lecture.
             F.write(Element)

    #____________________________________________________________________________________________________________________________________________________________
    # Ajouter un ensemble d'éléments sous forme de liste
    def Liste_to_Fichier(self,Liste): # 'creer_Fichier_Avec_Liste_Elements(self,ListeElements)' Créer d'un fichier à partir d'une liste : chaque élément de la liste représente une ligne du fichier
        with open(self.nomFichier,'w') as F:   # Ouverture du fichier en mode écriture : à ce niveau si le fichier existe il va être écrasé
            F.writelines(Liste)    

    def str_to_fichier(self,string):
        with open(self.nomFichier,'w') as F:   # Ouverture du fichier en mode écriture : à ce niveau si le fichier existe il va être écrasé
             F.write(string)
        return
             
             
    def Liste_to_str_to_Fichier(self,Liste_1): 
       Liste = self.Liste_to_Str1(Liste_1)
       with open(self.nomFichier,'a') as F:   # Ouverture du fichier en mode écriture : à ce niveau si le fichier existe il va être écrasé
            
            F.writelines(Liste)   
            F.writelines('\n')
    #____________________________________________________________________________________________________________________________________________________________
    # Lire le contenu d'un fichier et le retourne en le plaçant dans une liste
    def Fichier_to_Liste(self):  # extration d'une liste depuis un fichier  : chaque ligne du fichier représente un élément de cette liste
            with open(self.nomFichier, 'r') as f:    # Ouverture du fichier en mode lecture.
                return f.readlines()
    def Fichier_to_str(self):
        with open (self.nomFichier,'r') as f:
            return f.read()

    def supprimer_element(self,element):
        ch = self.Fichier_to_str()
        print(ch)
        chh = ch.replace(element,'')
        print(chh)
        self.str_to_fichier(ch)
        
    #____________________________________________________________________________________________________________________________________________________________
    # Afficher un fichier ligne par ligne
    def afficher_lignes_fichier(self):
        print("\n Affichage des lignes du fichier \n")
        with open(self.nomFichier, 'r') as F:
            for ligne in F:
                print (ligne)               
        print("\n Fin affichage des lignes du fichier")

    #____________________________________________________________________________________________________________________________________________________________
    # Afficher un fichier ligne par ligne et pour chaque ligne mot par mot
    def afficher_mots_fichier(self):
        i=0 # uttiliser comme un simple compteur pour afficher dans un message afin de le rendre plus explicite
        with open(self.nomFichier, 'r') as F:
            for ligne in F:
               i+=1
               print("Affichage des éléments du contenu la ligne : ",i,"\n") # message explicite
               L=C_Liste(ligne.split(self.separateur)) # Création d'une instance de la classe 'C_Liste'
               L.afficher_Liste()  # ici on fait appel à la méthode 'afficher_Liste()' de la classe 'C_Liste'


    def existe_element_fichier(self,Element):
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element in Liste_Lignes_du_Fichier[i]:
                    return(True)
        return(False)
                 
    
    def existe_element_fichier2(self,element):
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                L=Liste_Lignes_du_Fichier[i].split(self.separateur)
                if element in L:
                    return(True)
        return(False)
    
    
    def existe_element_fichier3(self,element):
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                L=Liste_Lignes_du_Fichier[i].split(self.separateur)
                if element in L:
                    return(True, Liste_Lignes_du_Fichier[i])
        return(False,False)

    
    
    def modifier_element_fichier(self,Element):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                Ligne_Courante=Liste_Lignes_du_Fichier[i] # La variable 'Ligne_Courante' est utilisée pour donner plus de clarté sur le plan pédagogique, on peut à la place utiliser directement directement 'Liste_Lignes_du_Fichier[i]'
                Liste_Elements_Ligne_Courante=self.Str_to_List(Ligne_Courante) # Ici on transforme la chaîne de caractère 'Ligne_Courante'  en une liste 'Liste_Elements_Ligne_Courante' 
                if Element not in Liste_Elements_Ligne_Courante:
                    Nouvelle_Liste=Nouvelle_Liste+[Ligne_Courante+'\n']
                else:
                    Nouvelle_Liste=C_Liste(Liste_Elements_Ligne_Courante) # Nouvelle_Liste est une instance de la classe C_Liste
                    Nouvelle_Liste_Elements=Nouvelle_Liste.changer_element(Element)
                    Nouvelle_Ligne_Modifiee=self.Liste_to_Str(Nouvelle_Liste_Elements)
                    Nouvelle_Liste=Nouvelle_Liste+[Nouvelle_Ligne_Modifiee+'\n']    
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            
    def ajouter_a_la_fin_de_la_ligne(self,ID,Element,sep):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                Ligne_Courante=Liste_Lignes_du_Fichier[i] # La variable 'Ligne_Courante' est utilisée pour donner plus de clarté sur le plan pédagogique, on peut à la place utiliser directement directement 'Liste_Lignes_du_Fichier[i]'
                Liste_Elements_Ligne_Courante=self.str_to_liste(Ligne_Courante) # Ici on transforme la chaîne de caractère 'Ligne_Courante'  en une liste 'Liste_Elements_Ligne_Courante' 
                if ID not in Liste_Elements_Ligne_Courante:
                    Nouvelle_Liste=Nouvelle_Liste+[Ligne_Courante+'\n']
                else:
                    Liste_Elements_Ligne_Courante[-1] = Liste_Elements_Ligne_Courante[-1].replace('\n','') +sep+ str(Element)
                    
                    Nouvelle_Liste_Elements=Liste_Elements_Ligne_Courante
                    Nouvelle_Ligne_Modifiee=self.Liste_to_Str1(Nouvelle_Liste_Elements)
                    Nouvelle_Liste=Nouvelle_Liste+[Nouvelle_Ligne_Modifiee+'\n']    
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
       
    
    def Liste_to_Str1(self,Liste_Elements):
        return self.separateur.join(map(str, Liste_Elements))
    
    def Liste_to_Str2(self,Liste_Elements):
        return self.separateur2.join(Liste_Elements)
    
    def supprimer_element_fichier(self,Element):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
# erreur d'écriture        Liste_Lignes_du_Fichier=Fichier_to_Liste(self) # extraire_liste(nomFichier)
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element not in Liste_Lignes_du_Fichier[i]:
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]+'\n']
# écriture erronée  Liste_to_Fichier(self.nomFichier,Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            
    def supprimer_ligne_fichier(self,Element_ligne):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
# erreur d'écriture        Liste_Lignes_du_Fichier=Fichier_to_Liste(self) # extraire_liste(nomFichier)
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element_ligne not in Liste_Lignes_du_Fichier[i]:
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]]
                else:
                    continue
# écriture erronée  Liste_to_Fichier(self.nomFichier,Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            
    def supprimer_ligne_fichier2(self,Element_ligne):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
# erreur d'écriture        Liste_Lignes_du_Fichier=Fichier_to_Liste(self) # extraire_liste(nomFichier)
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element_ligne+"\n" not in Liste_Lignes_du_Fichier[i].split(self.separateur)[-1].split(self.separateur2) and Element_ligne not in Liste_Lignes_du_Fichier[i].split(self.separateur)[-1].split(self.separateur2):
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]]
                else:
                    continue
# écriture erronée  Liste_to_Fichier(self.nomFichier,Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            self.Liste_to_Fichier(Nouvelle_Liste) #
            
    def modiffier_ligne(self,Element_ligne,nv_ligne):
        Nouvelle_Liste=[] 
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() 
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element_ligne not in Liste_Lignes_du_Fichier[i]:
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]]
                else:
                    Nouvelle_Liste = Nouvelle_Liste+[nv_ligne + '\n']
            self.Liste_to_Fichier(Nouvelle_Liste) #
        return
        
            

    def str_to_liste(self, string):
        return string.split(self.separateur)
    
    
    def nbre_ligne(self):
        return len(self.Fichier_to_Liste())
       

    def str_to_liste2(self, string):
        return string.split(self.separateur2)

    

# =============================================================================
# class Menu
# =============================================================================
    
class Menu():
    " classe générique de gestion de menu"
    def __init__(self,L=[]):
        self.list=L
        
    def afficher_menu(self):
        print('')
        if self.list != []:
            for i in range(len(self.list)):
                print(i," : ",self.list[i],"\n")
            return self.choix()

    def choix(self):
      while True:             
        try:
          i=int(input("Selon votre choix taper un nombre entre 0 et "+str(len(self.list)-1)+" -->  "))
          assert i >= 0 and i <= len(self.list)-1
        except ValueError:
          print("! Veuillez saisir un nombre entier.\n")
        except AssertionError:
          print("! Le nombre saisi doit être supérieur ou égal à 0 et inférieur ou égal à "+ str(len(self.list)-1) +".\n")        
        else:
          return i 
          break       
      
    def get_menu_db(self,menu_id):
        menuFichier = C_Fichier('db/menu.txt')
        menu = menuFichier.existe_element_fichier3(str(menu_id))
        if menu[0]:
            L = menuFichier.str_to_liste(menu[1].replace('\n',''))
            
            self.list = L[1:] + ['Retour', 'Quitter']
            return

# =============================================================================
# class Date
# =============================================================================


from datetime import datetime



def saisirDate():
    jour=int(input("saisir le jour de la date (entre 1 et 31) : "))
    mois=int(input("saisir le mois de la date (entre 1 et 12) : "))
    an=int(input("saisir l'année de la date (un nombre en 4 chiffre ) : "))
    return jour,mois,an      

def afficherDate(jour,mois,an):
    print(DateToStr(jour,mois,an))         

def DateToStr(jour,mois,an):     
    return str(jour)+"-"+str(mois)+"-"+str(an)

def StrToDate(ch):
    L=ch.split("-")
    jour=int(L[0])
    mois=int(L[1])
    an=int(L[2])
    return jour,mois,an


def comparer_Date(date1,date2):
    d1 = datetime(date1.an, date1.mois, date1.jour)
    d2 = datetime(date2.an, date2.mois, date2.jour)
      
    if d1 > d2:
        return True
    elif d1 <= d2:
        return False

class Date(object):
    def __init__(self,jj=0,mm=0,aa=0,H=0,M=0,S=0):
        self.jour=jj
        self.mois=mm
        self.an=aa 
        self.H=H
        self.M=M
        self.S=S
  
    
    def date_now(self):
        
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def saisirDate(self):
        
        while(True):
            self.jour=int(input("saisir le jour de la date (entre 1 et 31) : "))
            self.mois=int(input("saisir le mois de la date (entre 1 et 12) : "))
            self.an=int(input("saisir l'année de la date (un nombre en 4 chiffre ) : "))
            try:
                 self.verifierdate()
            except ValueError:
                print("\n-------La date n'est pas valid-------\n")
            else:
                break
            
        
    def saisir_annee(self):
        while(True):
            self.an=int(input("saisir l'année de la date (un nombre en 4 chiffre ) : "))
            self.jour = 1
            self.mois = 1
            try:
                 self.verifierdate()
            except ValueError:
                print("\n-------La date n'est pas valid-------\n")
            else:
                break
    def saisir_annee2(self,annee):
        self.an=int(annee)
        self.jour = 1
        self.mois = 1
    
    def verifierdate(self):
        return  datetime(self.an, self.mois, self.jour)
    
    def afficherDate(self):
        print(self.DateToStr())            
    
    def DateToStr(self):    
        return str(self.an)+"-"+str(self.mois)+"-"+str(self.jour)

    def StrToDate(self,ch):
        L=ch.split("-")
        self.an=int(L[0])
        self.mois=int(L[1])
        self.jour=int(L[2])

    def SUP_Dates(self,D2):
        if self.an<D2.an:
            return False
        elif self.an==D2.an:
            if self.mois<D2.mois:
                return False
            elif self.mois==D2.mois:
                if self.jour<D2.jour:
                    return False
        return True

    def AGE(self,D2):
        if self.mois<D2.mois:
            return D2.an-self.an
        else:
            return D2.an-self.an-1



# =============================================================================
# class Compte
# =============================================================================
import numpy as np

from random import randint

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







# =============================================================================
# class Client
# =============================================================================

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
    
# =============================================================================
#  class agence
# =============================================================================


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

# =============================================================================
# class banque
# =============================================================================

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
    
# =============================================================================
# Main Function
# =============================================================================

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
    
