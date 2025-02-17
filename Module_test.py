# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:12:44 2024

@author: DIEDHIOU
"""

""" 
Ceci est une description de statitique descriptive

"""

def donnees_descriptives (nouvelle_liste):
    minimum = min(nouvelle_liste)
    maximum = max(nouvelle_liste)
    somme = sum(nouvelle_liste)
    moyenne = somme/len(nouvelle_liste)
    resultat = {"Min" : minimum, 
                "Max" : maximum, 
                "Somme" : somme, 
                "Moyenne" : moyenne}
    
    
    return resultat 

def sommedelaserie (nouvelle_liste):
    somme = sum(nouvelle_liste)
    resultat = {"somme" : somme}
    return somme