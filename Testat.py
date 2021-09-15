#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 12:36:01 2021

@author: oem
"""

import numpy as np
# import math

sensibilite = p_M_T = 0.8
specificite = p_S_Tn = 0.9

population = 1000
p_M = 0.005

class Testat :
    
    def __init__(self, sensibilite, specificite, population, p_M):
        self.sensibilite = self.p_M_T = sensibilite
        self.specificite = self.p_S_Tn = specificite
        self.population = population
        self.p_M = p_M
        
    def calculate(self):
        p_S = 1 - self.p_M
        
        pop_M = self.p_M * self.population
        pop_S = p_S * self.population
        
        pop_MT = self.p_M_T * pop_M
        pop_MTn = pop_M - pop_MT
        
        pop_STn = self.p_S_Tn * pop_S
        pop_ST = pop_S - pop_STn
        
        p_T_M = pop_MT / (pop_MT + pop_ST)
        p_Tn_S = pop_STn / (pop_STn + pop_MTn)


        arr_population = np.array([[pop_MT, pop_MTn, pop_M],
                                   [pop_ST, pop_STn, pop_S], 
                                   [p_T_M, p_Tn_S, population]])
        
        return arr_population
    
    def __str__(self):
        
        arr_population = self.calculate()
        str_initial_datas = "Les données initiales sont : \n - Population = {}\n - Proportion de malade = {} \n - Sensibilité du test = {}\n - Spécificité du test = {}".format(self.population, self.p_M, self.specificite, self.sensibilite)
        str_result_1 = "La probabilité d'être malade sachant que l'on a un test positif est : {}".format(round(arr_population[2,0],4))
        str_result_2 = "La probabilité d'être sain sachant que l'on a un test négatif est : {}".format(round(arr_population[2,1],4))
        str_affichage = str_initial_datas + '\n' + str_result_1 + '\n' + str_result_2
        
        return str_affichage

testat = Testat(sensibilite, specificite, population, p_M)
print(testat)