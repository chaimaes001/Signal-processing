# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:07:40 2021
@author: Chaimae
"""
import numpy as np
import matplotlib.pyplot as plt

def dtw(m1=[], m2=[]):
    
    #ici la taille du vecteur du signal du 1er mot
    m = len(m1)
    #ici la taille du vecteur du signal du 2ème mot
    n = len(m2)
    #on va creer une matrice de n lignes et m colonnes
    DTW = np.zeros((n, m), dtype=float)
    #ici remplir la première ligne de la matrice
    for i in range(1, m):
        DTW[0, i] = distance(m1[i], m2[0]) + DTW[0, i - 1]

    for i in range(1, n):
        DTW[i, 0] = distance(m1[0], m2[i]) + DTW[i - 1, 0]
        
    #ivi remplir les autres élément de la matrice en se basant sur les lignes et les colonnes précédentes
    for i in range(1, n):
        for j in range(1, m):
            cost = distance(m1[j], m2[i])
            DTW[i, j] = cost + np.min([DTW[i - 1, j],DTW[i, j - 1],DTW[i - 1, j - 1]])

    #ici trouver le meilleur chemin
    path = dict()
    #ici associer la valeur de dtw(n-1,m-1) à la variable path pour le départ
    path[0] = (n - 1, m - 1, DTW[n - 1, m - 1])
    c = 0
    finished = False
    i = n - 1
    j = m - 1
    while (not finished):
        
        #ici récupérer les 3 valeurs de (i-1,j) ,(i-1,j-1) et (i,j-1) de la matrice et les affecter au vecteur v
        v = np.array([DTW[i - 1, j], DTW[i - 1, j - 1], DTW[i, j - 1]])
        #ici récupérer le minimum de ces valeurs et l'affecter à la variable cost
        cost = np.min(v)
        #ici chercher la valeur minimale
        k = np.where(v == cost)[0][0]

        # k = 0 c'est à dire le minimum existe à l'index (i-1,j)
        if k == 0:  
            #ici affecter la valeur minimale à l'indice c
            path[c] = (i - 1, j, cost)
            i = i - 1
            
        #ici le minimum existe dans la case (i-1,j-1)
        elif k == 1: 
            #ici affecter la valeur minimale à l'indice c
            path[c] = (i - 1, j - 1, cost)
            j = j - 1
            i = i - 1
            
        #ici le minimum existe dans la case (i-1,j-1)            
        else: 
            path[c] = (i, j - 1, cost)
            j = j - 1
        #la condition d'arret c'est qu'on est arrivé a la position (0,0) dans la matrice DTW
        if path[c][0] == 0 and path[c][1] == 0:
            finished = True
        c += 1
        
    # plt.plot(list(path.keys()),list(path.values()))
    # plt.show() 
        
    #ici création d'un vecteur pour stocker les valeurs du cout du chemin
    cost = np.array([])
    for k in path.keys():
        cost = np.append(cost, path[k][2])
    #ici calcule de la somme du cout
    S = np.sum(cost)
    #ici normalisation de la valeur 
    D = np.sqrt(S)
    return D

def distance(v1, v2):
    return (v1 - v2) ** 2
