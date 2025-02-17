# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 00:44:00 2024

@author: DIEDHIOU
"""

def stat_descriptives(nom_liste):
    somme = sum(nom_liste)
    moyenne = somme/len(nom_liste)
    minimum = min(nom_liste)
    maximum = max(nom_liste)
    resultat = {"Somme" : somme, "Min" : minimum, "Max" : maximum, "Moyenne" : moyenne}
    return resultat;

def somme_element(nom_liste):
    return sum(nom_liste)
