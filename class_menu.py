# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:20:34 2023

@author: sagou
"""


from class_fichier import C_Fichier

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

