#Ce fichier est un programme qui utilise les fonctions de TP2 pour faire marcher le jeu du pendu.


from TP2TK import fJeu,fAfficher,fTiret,fMots,fFichier,fScore,fLettre
from tkinter import Tk, Frame, Label, Button, Canvas, Entry, StringVar, PhotoImage,IntVar


#Création de la fenetre principale
Mafenetre = Tk()
Mafenetre.title('Pendu')

#Images importées
bon1=PhotoImage(file="bonhomme1.gif")
bon2=PhotoImage(file="bonhomme2.gif")
bon3=PhotoImage(file="bonhomme3.gif")
bon4=PhotoImage(file="bonhomme4.gif")
bon5=PhotoImage(file="bonhomme5.gif")
bon6=PhotoImage(file="bonhomme6.gif")
bon7=PhotoImage(file="bonhomme7.gif")
bon8=PhotoImage(file="bonhomme8.gif")
photoliste=[bon8,bon7,bon6,bon5,bon4,bon3,bon2,bon1]

#Initialisation des variables
mot=fMots(fFichier())
LE=''
E=IntVar()
pT=StringVar()
pT.set(fTiret(mot))


#Creation d'un widget frame dans la fenetre principale
frame1 = Frame(Mafenetre, relief ='groove')
frame1.pack(side='left',padx=10,pady=10)

#Creation d'un bouton pour quitter
BoutonQuitter = Button(Mafenetre, text="Quitter", command = Mafenetre.destroy)
BoutonQuitter.pack(padx=5,pady=5)

#Creation d'un widget entry
champ=Entry(Mafenetre)
champ.focus_set()
champ.pack(padx=5,pady=5)

#Creation d'un widget Label et d'un widget Button dans un widget Frame
Label(frame1,text="Pendu").pack(padx=10,pady=10)
valider=Button(frame1,text="Valider",command=lambda: fJeu(mot,pT,E,LE,champ.get(),Canevas,photoliste,bon,champ))
valider.pack(padx=10,pady=10)

#Creation d'un Label pour afficher le mot caché
mott=Label(Mafenetre,textvariable=pT)
mott.pack(padx=50,pady=50)

#Creation canvas pour afficher l'image du pendu
Canevas=Canvas(Mafenetre,width=500,height=500)
bon=Canevas.create_image(200,200,image=photoliste[0])
Canevas.pack(padx=0,pady=0)


Mafenetre.mainloop()


