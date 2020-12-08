#Ce ficher est composé de toutes les fonctions permettant de réaliser un pendu.

import random
from random import randint
from tkinter import Tk


#Fonction permettant générer un nombre aléatoire pour choisir le mot dans la liste
#pL est une liste contenant tous les mots
#Cette fonction renvoie le mot àt rouver
def fMots(pL):
    rnd=random.randint(0,3)
    mot=pL[rnd]
    return mot
    
#Fonction permettant d'ouvrir le fichier contenant les mots, le lire et retourner une liste
#Cette fonction une liste contenant tous les mots à trouver sous forme de liste
def fFichier():
    fichier=open('pendu.txt','r')
    lst=fichier.read()
    fichier.close()
    liste=lst.split()
    return liste

#Fonction permettant de donner une chaine de caractères avec la première lettre du mot et des _
#pM est le mot à trouver
#Cette fonction renvoie le mot à trouver avec la première lettre affichée puis des _
def fTiret(pM):
    tiret=pM[0]
    for i in range (len(pM)-1):
        tiret=tiret+'_'
    return tiret

def fLettre():
    lettre=input('Choissisez une lettre: ')
    return lettre
#Fonction permettant de jouer de jouer en affichant le mot avec les lettres trouvées
#pM est le mot à trouver, pT est le mot à trouver mais "caché" (cad avec des _), pE est le nombre d'erreurs et pLE et une chaine caractère cotenant les lettres déjà utilisées
def fJeu(pM,pT,pE,pLE,plettre):
    if plettre in pLE:
        return pT,pE,pLE
    pLE=pLE+plettre
    if plettre in pM: #Le mot est parcouru pour savoir si chaque lettre du mot caché correspond à la lettre proposée
        for i in range (len(pM)):
            if plettre==pM[i]:
                pT=pT[0:i]+plettre+pT[i+1:len(pT)]   
    else:
        pE=pE+1
    return pT,pE,pLE


#Fonction permettant d'afficher le pendu au cours de la partie ainsi que le mot avec les tirets
#pM est le mot à trouver, pT est le mot à trouver mais "caché" (cad avec des _), pE est le nombre d'erreurs et pLE et une chaine caractère cotenant les lettres déjà utilisées
def fAfficher(pE,pT,pM,pLE):
    L=["---------","| \n| \n---------","| \n| \n| \n| \n---------","|/ \n| \n| \n| \n| \n---------",
       "______ \n|/ \n| \n| \n| \n| \n---------","______ \n|/   | \n| \n| \n| \n| \n---------",
       "______ \n|/   | \n|    o \n|  \n| \n| \n---------",
       "______ \n|/   | \n|    o \n|   /|\ \n| \n| \n---------",
       "______ \n|/   | \n|    o \n|   /|\ \n|   / \ \n| \n---------"]
    print (L[pE])
    print (pT)
    if pE==8:
        print('Perdu')
    elif pM==pT:
        print('Gagné') 

#Fonction permettant de retenir le meilleur score du joueur
#pE est le nombre d'erreurs
#Cette fonction retourne le meilleur score du joueur
def fScore(pE,pS):
    if pE<pS:
        pS=pE
    return pS
