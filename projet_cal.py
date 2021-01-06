from tkinter import * # Tkinter

class Calculatrice():
    def __init__(self): # Construction
        self.nbr1 = 0 # Premier nombre
        self.nbr2 = 0 # Deuxième nombre
        self.result = 0 # Valeur finale
        self.entrer = StringVar() # Capte les valeurs écrit
        self.texte = "" # Nombre écrir par l'utilisateur
        self.signe = "" # Type d'opération
        
    def init(self): # Initialisation 
        self.nbr1 = 0
        self.nbr2 = 0
        self.result = 0
        self.texte = ""
        self.signe = ""
        
    def afficher_Nb(self): # Afficher nombre sur écran 
        self.entrer.set(self.texte)

    def operation(self): # Vérification du type d'opération
        if : 
            if "+" in self.texte:
                self.Plus()
            elif "-" in self.texte:
                self.Moin()
            elif "/" in self.texte:
                self.Div()
            elif "*" in self.texte:
                self.Mult()
        else :
            self.entrer.set("ERROR")
            self.init()

    def Plus(self): # Addition
        nbr = self.texte.split("+")
        self.nbr1 = float(nbr[0])
        self.nbr2 = float(nbr[1])
        self.result = self.nbr2 + self.nbr2
        self.entrer.set(str(self.result))
        self.init()

    def Moin(self): # Soustarction
        nbr = self.texte.split("-")
        self.nbr1 = float(nbr[0])
        self.nbr2 = float(nbr[1])
        self.result = self.nbr1 - self.nbr2
        self.entrer.set(str(self.result))
        self.init()

    def Div(self): # Division
        nbr = self.texte.split("/")
        self.nbr1 = float(nbr[0])
        self.nbr2 = float(nbr[1])
        self.result = self.nbr1 / self.nbr2
        self.entrer.set(str(self.result))
        self.init()

    def Mult(self): # Multiplication
        nbr = self.text.split("*")
        self.nbr1 = float(nbr[0])
        self.nbr2 = float(nbr[1])
        self.result = self.nbr1 * self.nbr2
        self.entrer.set(str(self.result))
        self.init()
    
# Fonction des boutons

def B1 ():
    calculatrice.texte += "1"
    calculatrice.entrer.set(calculatrice.texte)

def B2 ():
    calculatrice.texte += "2"
    calculatrice.entrer.set(calculatrice.texte)

def B3 ():
    calculatrice.texte += "3"
    calculatrice.entrer.set(calculatrice.texte)

def B4 ():
    calculatrice.texte += "4"
    calculatrice.entrer.set(calculatrice.texte)
    
def B5 ():
    calculatrice.texte += "5"
    calculatrice.entrer.set(calculatrice.texte)

def B6 ():
    calculatrice.texte += "6"
    calculatrice.entrer.set(calculatrice.texte)

def B7 (): 
    calculatrice.texte += "7"
    calculatrice.entrer.set(calculatrice.texte)

def B8 (): 
    calculatrice.texte += "8"
    calculatrice.entrer.set(calculatrice.texte)
    
def B9 (): 
    calculatrice.texte += "9"
    calculatrice.entrer.set(calculatrice.texte)

def B0():
    calculatrice.texte += "0"
    calculatrice.entrer.set(calculatrice.texte)

def BV():
    calculatrice.texte += "."
    calculatrice.entrer.set(calculatrice.texte)
    
def BP (): 
    calculatrice.texte += "+"
    calculatrice.entrer.set(calculatrice.texte)

def BS (): 
    calculatrice.texte += "-"
    calculatrice.entrer.set(calculatrice.texte)

def BD ():
    calculatrice.texte += "/"
    calculatrice.entrer.set(calculatrice.texte)

def BM (): 
    calculatrice.texte += "*"
    calculatrice.entrer.set(calculatrice.texte)

def BE ():
    calculatrice.operation()

def BC (): 
    calculatrice.entrer.set("")
    calculatrice.init()
    
# FENETRE :

fenetre = Tk() # Création de a fenêtr 1e
fenetre.affichage("200x240") # Définition de la fenêtre
fenetre.titre("Calculatrice") # Titre de la calculatrice
fenetre["bg"]= "black" # Couleur de la fenêtre
fen["relief"] = "raised"

# PROGRAMME :

# Création instance
calculatrice = Calculatrice()

# // Ecran calculatrice //
ECRAN = Entrer(fen, width=28, textvariable=calculatrice.entry, bg ="black", fg="white", relief=SUNKEN, bd=5).place(x=9, y=8)

# // Bouttons //
B1 = Button(fenetre, text="1", command=B1, width=3, height=2, bg="grey", fg="white").place(x=10, y=40) # Boutton 1
B2 = Button(fenetre, text="2", command=B2, width=3, height=2, bg="grey", fg="white").place(x=50, y=40) # Boutton 2
B3 = Button(fenetre, text="3", command=B3, width=3, height=2, bg="grey", fg="white").place(x=90, y=40) # Boutton 3
B4 = Button(fenetre, text="4", command=B4, width=3, height=2, bg="grey", fg="white").place(x=10, y=90) # Boutton 4
B5 = Button(fenetre, text="5", command=B5, width=3, height=2, bg="grey", fg="white").place(x=50, y=90) # Boutton 5
B6 = Button(fenetre, text="6", command=B6, width=3, height=2, bg="grey", fg="white").place(x=90, y=90) # Boutton 6
B7 = Button(fenetre, text="7", command=B7, width=3, height=2, bg="grey", fg="white").place(x=10, y=140) # Boutton 7
B8 = Button(fenetre, text="8", command=B8, width=3, height=2, bg="grey", fg="white").place(x=50, y=140) # Boutton 8
B9 = Button(fenetre, text="9", command=B9, width=3, height=2, bg="grey", fg="white").place(x=90, y=140) # Boutton 9
BC = Button(fenetre, text="C", command=BC, width=3, height=2, bg="gold", fg="grey", relief=RIDGE).place(x=10, y=190) # Boutton C (Clear)
B0 = Button(fenetre, text="0", command=B0, width=3, height=2, bg="grey", fg="white").place(x=50, y=190) # Boutton 0
BF = Button(fenetre, text=".", command=BF, width=3, height=2, bg="grey", fg="white").place(x=90, y=190) # Boutton = (égale)

BP = Button(fenetre, text="+", command=BP, width=4, height=2, bg="gold", fg="grey", relief=GROOVE).place(x=150, y=40) # Boutton + (addition)
BS = Button(fenetre, text="*", command=BS, width=4, height=2, bg="gold", fg="grey", relief=GROOVE).place(x=150, y=80) # Boutton - (soustacrtion)
BD = Button(fenetre, text="/", command=BD, width=4, height=2, bg="gold", fg="grey", relief=GROOVE).place(x=150, y=120) # Boutton / (division)
BM = Button(fenetre, text="*", command=BM, width=4, height=2, bg="gold", fg="grey", relief=GROOVE).place(x=150, y=160) # Boutton X (multiplication)
BE = Button(fenetre, text="=", command=BE, width=4, height=1, bg="grey", fg="white", relief=RIDGE).place(x=150, y=205) # Button = (égale)

fenetre.mainloop() # Gestion de la fenêtre