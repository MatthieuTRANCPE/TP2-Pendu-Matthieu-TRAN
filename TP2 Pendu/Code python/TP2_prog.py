#Ce fichier est un programme qui utilise les fonctions de TP2 pour faire marcher le jeu du pendu.


from TP2 import fJeu,fAfficher,fTiret,fMots,fFichier,fScore,fLettre


#S est fixé pour que le score ait une valeur initiale
S=10
#r est fixé à un pour pouvoir rejouer ou non, lorsque r=1 on continue de jouer
r=1

#Cette boucle appelle les différentes fontions pour mettre en marche le python, tant que rien ne met fin à la boucle on continue de jouer
while r==1:
    mot=fMots(fFichier())
    pT=fTiret(mot)
    LE=''
    E=0
    fAfficher(E,fTiret(mot),mot,LE)
    while E<8 and mot!=pT:
        pT,E,LE=fJeu(mot,pT,E,LE,fLettre())
        fAfficher(E,pT,mot,LE)
    S=fScore(E,S)
    print('Votre nombre de derreurs est : '+ str(E))
    print('Votre meilleur score est : '+ str(S))
    r=int(input('Voulez-vous rejouer? (1 ou 0) : '))
