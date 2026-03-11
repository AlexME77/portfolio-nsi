#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:56:06 2024

@author: eric
"""
import timeit
import random

def test():
    k = 0
    for i in range(10):
        k += 1
        
tic = timeit.default_timer()
test()
#print(timeit.default_timer()-tic)

def triSimple(L):
    LL = []
    while len(L) > 0:
        m = L[0]
        for e in L:
            if e < m:
                m = e
        LL.append(m)
        L.remove(m)
    return LL
            
        
def triFusion(L):
    if len(L) <= 1:
        return L
    else:
        return fusion_r(triFusion(L[:len(L)//2]), triFusion(L[len(L)//2:]))

def fusion(L1, L2):
    i = 0
    j = 0
    liste_fusion = []

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            liste_fusion.append(L1[i])
            i += 1
        else:
            liste_fusion.append(L2[j])
            j += 1
    while i < len(L1):
        liste_fusion.append(L1[i])
        i += 1
    while j < len(L2):
        liste_fusion.append(L2[j])
        j += 1
    return liste_fusion

def fusion_r(L1, L2):
    if len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1
    elif L1[0] <= L2[0]:
        return [L1[0]] + fusion_r(L1[1:], L2)
    else:
        return [L2[0]] + fusion_r(L1, L2[1:])
    
def aleatoire(N):
    L = []
    for i in range(N):
        L.append(random.randint(0,100))
    return L

if __name__=='__main__':
    L = aleatoire(10)

    print("Liste aléatoire :", L)

    tic = timeit.default_timer()
    print("Tri fusion :", triFusion(L))
    print(timeit.default_timer()-tic)

    tic = timeit.default_timer()
    print("Tri simple :", triSimple(L))
    print(timeit.default_timer()-tic)

    tic = timeit.default_timer()
    print("Test de la fonction fusion :", fusion([1,3,5,7], [2,4,6,8]))
    print(timeit.default_timer()-tic)

    tic = timeit.default_timer()
    print("Test de la fonction fusion_r :", fusion_r([1,3,5,7], [2,4,6,8]))
    print(timeit.default_timer()-tic)


