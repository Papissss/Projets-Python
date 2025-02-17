# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:40:27 2024

@author: DIEDHIOU
"""

def mes_statistiques_descriptives(mes_stats):
    somme = sum(mes_stats)
    moyenne = sum(mes_stats)/len(mes_stats)
    minimum = min(mes_stats)
    maximum = max(mes_stats)
    resultat = {"Somme" : somme, "Moyenne" : moyenne, "Minimum" : minimum, "Maximum" : maximum}
    return (resultat)

def sommes_des_unites(mes_stats):
    somme = sum(mes_stats)
    return somme

def moyenne_des_elements(mes_stats):
    moyenne = sum(mes_stats)/len(mes_stats)
    return moyenne

def maximum_element(mes_stats):
    maximum = max(mes_stats)
    return maximum

def minimum_element(mes_stats):
    minimum = min(mes_stats)
    return minimum
    