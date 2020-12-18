# projet calculatrice 

WIDTH, HEIGHT = 300, 50
pad_x = 50
pad_y = 0
taille = 20

import tkinter as tk
root = tk.Tk()


# Variables globales 

A = 0
B = 0

op = ""         # opérations + - * /
R = 0           # résultat



# Fonctions 
def clic_1():
    global A
    global B
    global op
    N = 1
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + op + str(B))
        print("B = ", B)


def clic_2():
    global A
    global B
    global op
    N = 2
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + " " + op + " " + str(B))
        print("B = ", B)


def clic_3():
    global A
    global B
    global op
    N = 3
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + " " + op + " " + str(B))
        print("B = ", B)


def clic_4():
    global A
    global B
    global op
    N = 4
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + " " + op + " " + str(B))
        print("B = ", B)


def clic_5():
    global A
    global B
    global op
    N = 5
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + " " + op + " " + str(B))
        print("B = ", B)


def clic_6():
    global A
    global B
    global op
    N = 6
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + " " + op + " " + str(B))
        print("B = ", B)


def clic_7():
    global A
    global B
    global op
    N = 7
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + " " + op + " " + str(B))
        print("B = ", B)


def clic_8():
    global A
    global B
    global op
    N = 8
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + " " + op + " " + str(B))
        print("B = ", B)


def clic_9():
    global A
    global B
    global op
    N = 9
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + " " + op + " " + str(B))
        print("B = ", B)


def clic_0():
    global A
    global B
    global op
    N = 0
    if op == "":
        A = A*10 + N
        L_resultat.config(text=str(A))
        print("A = ", A)
    else:
        B = B*10 + N
        L_resultat.config(text=str(A) + " " + op + " " + str(B))
        print("B = ", B)




def plus():
    global op
    op = "+"
    L_resultat.config(text=str(A) + " " + op )

def moins():
    global op
    op = "-"
    L_resultat.config(text=str(A) + " " + op )

def mult():
    global op
    op = "x"
    L_resultat.config(text=str(A) + " " + op )

def div():
    global op
    op = "/"
    L_resultat.config(text=str(A) + " " + op )


def egal():
    global A
    global B
    global R
    global op
    if op == "+":
        R = A + B
    elif op == "-":
        R = A - B
    elif op == "x":
        R = A * B
    elif op == "/":
        R = A / B
    L_resultat.config(text=str(A) + " " + op + " " + str(B) + " = " + str(format(R, ".2f")))
    A = R
    B = 0
    R = 0
    op = ""


def clear():
    global A, B, R, op
    A, B, R = 0, 0, 0
    op = ""
    L_resultat.config(text="")


# Début du code


# Labels (ligne de calcul) ************************************************

L_resultat = tk.Label(root, text="", font=("calibri", taille), padx=50)
L_resultat.grid(column=0, row=0, columnspan = 3)


# Boutons *****************************************************************

# Ligne 4
B_0 = tk.Button(root, text="0", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_0)
B_0.grid(column=0, row=4)

B_point = tk.Button(root, text=".", padx=pad_x, pady = pad_y, font=("calibri", taille))
B_point.grid(column=1, row=4)

B_egal = tk.Button(root, text="=", padx=pad_x, pady = pad_y, font=("calibri", taille), bg = "orange", command=egal)
B_egal.grid(column=2, row=4)


# Ligne 3
B_1 = tk.Button(root, text="1", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_1)
B_1.grid(column=0, row=3)

B_2 = tk.Button(root, text="2", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_2)
B_2.grid(column=1, row=3)

B_3 = tk.Button(root, text="3", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_3)
B_3.grid(column=2, row=3)


# Ligne 2
B_4 = tk.Button(root, text="4", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_4)
B_4.grid(column=0, row=2)

B_5 = tk.Button(root, text="5", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_5)
B_5.grid(column=1, row=2)

B_6 = tk.Button(root, text="6", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_6)
B_6.grid(column=2, row=2)


# Ligne 1
B_7 = tk.Button(root, text="7", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_7)
B_7.grid(column=0, row=1)

B_8 = tk.Button(root, text="8", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_8)
B_8.grid(column=1, row=1)

B_9 = tk.Button(root, text="9", padx=pad_x, pady = pad_y, font=("calibri", taille), command=clic_9)
B_9.grid(column=2, row=1)


# Colonne 3
B_clear = tk.Button(root, text="CLEAR", padx=20, pady = pad_y, font=("calibri", taille), bg = "dark grey", command=clear)
B_clear.grid(column=3, row=0)

B_div = tk.Button(root, text="/", padx=pad_x, pady = pad_y, font=("calibri", taille), bg = "dark grey", command=div)
B_div.grid(column=3, row=1)

B_mult = tk.Button(root, text="x", padx=pad_x, pady = pad_y, font=("calibri", taille), bg = "dark grey", command=mult)
B_mult.grid(column=3, row=2)

B_moins = tk.Button(root, text="-", padx=pad_x, pady = pad_y, font=("calibri", taille), bg = "dark grey", command=moins)
B_moins.grid(column=3, row=3)

B_plus = tk.Button(root, text="+", padx=pad_x, pady = pad_y, font=("calibri", taille), bg = "dark grey", command=plus)
B_plus.grid(column=3, row=4)



# Fin du code 
root.mainloop()