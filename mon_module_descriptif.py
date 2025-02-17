# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:51:22 2024

@author: DIEDHIOU
"""
"""
Cette fonction permet de faire des statistiques descriptives sur une liste
""" 
def ma_statistique_descriptive (ma_liste):
    minimum = min(ma_liste)
    maximum = max(ma_liste)
    somme = sum(ma_liste)
    moyenne = somme/len(ma_liste)
    resultat = {"min": minimum, "max" : maximum, "somme" : somme, "moyenne": moyenne }
    return resultat 

"""
Cette fonction permet de calculer la somme des éléments d'une liste
"""
def somme_element(ma_liste):
    somme = sum(ma_liste)
    resultat = {"somme": somme}
    return resultat 
