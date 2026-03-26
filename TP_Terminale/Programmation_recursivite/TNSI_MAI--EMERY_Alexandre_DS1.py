#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 22:41:35 2025

@author: DE CECCO
"""

def long(s):
    if len(s)==1:
        return 1
    return 1+long(s[1:])

def inverse(s):
    if len(s)==1:
        return s
    return s[-1]+inverse(s[:-1])

def estPalind(mot):
    if len(mot)<=1:
        return True
    return mot[0]==mot[-1] and estPalind(mot[1:-1])
    
def Tri_rapide(L) :
    N = len(L)
    if N<=1:
        return L
    piv = L.pop(N//2)
    Lg, Ld = [ ], [ ]
    for x in L:
        if x <= piv:
            Lg.append(x)
        else:
            Ld.append(x)
    return Tri_rapide(Lg) + [piv] + Tri_rapide(Ld)

# -----------------------------------------
# partie test qui ne doit pas être modifiée
# -----------------------------------------
s = "RAPACE"
print(f"longueur de {s} : ",long(s))

print(f"inverse de {s} : ",inverse(s))

p = "RESSASSER"
print(f"{p} est-il un palindrome ? ",estPalind(p))
p = "RETENTER"
print(f"{p} est-il un palindrome ? ",estPalind(p))

L = [5,1,9,8,6,4,3,65,13,65]
print("Liste triée : ",Tri_rapide(L))