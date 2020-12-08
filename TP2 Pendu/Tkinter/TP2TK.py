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
    liste=sorted(liste)
    return liste

#Fonction permettant de donner une chaine de caractères avec la première lettre du mot et des _
#pM est le mot à trouver
#Cette fonction renvoie le mot à trouver avec la première lettre affichée puis des _
def fTiret(pM):
    tiret=pM[0]
    for i in range (len(pM)-1):
        tiret=tiret+'_'
    return tiret

#Fontion permettant de proposer une lettre
def fLettre():
    lettre=input('Choissisez une lettre: ')
    return lettre

#Fonction permettant de jouer de jouer en affichant le mot avec les lettres trouvées
#pM est le mot à trouver, pT est le mot à trouver mais "caché" (cad avec des _), pE est le nombre d'erreurs et pLE et une chaine caractère cotenant les lettres déjà utilisées
#Canevas,photoliste et bon servent pour Tkinter, ils permettent de renvoyer "en temps réel" le nombre d'erreurs (et donc l'image) et le mot caché et champ sert à effacer la lettre une fois validée
def fJeu(pM,pT,pE,pLE,plettre,Canevas,photoliste,bon,champ):
    effacer=len(plettre)
    toto=pT.get()
    erreur=pE.get()
    if plettre in pLE:
        pT.set(toto)
        pE.set(erreur)
        champ.delete(0,effacer)
        Canevas.itemconfig(bon,image=photoliste[erreur])
        return pT,erreur,pLE
    pLE=pLE+plettre
    if plettre in pM:
        for i in range (len(pM)):
            if plettre==pM[i]:
                toto=toto[0:i]+plettre+toto[i+1:len(toto)]   
    else:
        erreur=erreur+1
    pT.set(toto)
    pE.set(erreur)
    champ.delete(0,effacer)
    Canevas.itemconfig(bon,image=photoliste[erreur])  
    return pT,erreur,pLE



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
