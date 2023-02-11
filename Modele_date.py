# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 16:13:03 2023

@author: HP
"""


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
 