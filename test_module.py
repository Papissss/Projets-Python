# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 23:29:10 2024

@author: DIEDHIOU
"""

def mes_statistiques_descriptives (new_liste):
    minimum = min(new_liste)
    maximum = max(new_liste)
    somme = sum(new_liste)
    moyenne = somme/len(new_liste)
    resultat = {"Min" : minimum,
                "Max" : maximum,
                "Somme" : somme,
                "Moyenne" : moyenne}
    return resultat