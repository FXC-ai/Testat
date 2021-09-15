#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 12:36:01 2021

@author: oem
"""

import numpy as np

sensibilite = p_M_T = 0.8
specificite = p_S_Tn = 0.9

population = 1000
p_M = 0.005
p_S = 1- p_M

pop_M = p_M * population
pop_S = p_S * population

pop_MT = p_M_T * pop_M
pop_MTn = pop_M - pop_MT

pop_STn = p_S_Tn * pop_S
pop_ST = pop_S - pop_STn

p_T_M = pop_MT / (pop_MT + pop_ST)
p_Tn_S = pop_STn / (pop_STn + pop_MTn)


arr_population = np.array([[pop_MT, pop_MTn],[pop_ST, pop_STn], [p_T_M, p_Tn_S]])
