# projet_calcul
# crée une calculatrice en phyton   
WIDTH, HEIGHT = 300, 50
pad_x = 50
pad_y = 0
taille = 20

import tkinter as tk
root = tk.Tk()
root.title(" Calculatrice ") # ajoute un titre


# Variables globales 
nb1 = ""
nb2 = ""
op = 0
#les fonction

def ajoute(nb):
    global nb1
    nb1 += nb


def num1():
    ajoute("1")
    label.config(text = nb1)


def num2():
    ajoute("2")
    label.config(text = nb1)


def num3():
    ajoute("3")
    label.config(text = nb1)


def num4():
    ajoute("4")
    label.config(text = nb1)


def num5():
    ajoute("5")
    label.config(text = nb1)


def num6():
    ajoute("6")
    label.config(text = nb1)


def num7():
    ajoute("7")
    label.config(text = nb1)


def num8():
    ajoute("8")
    label.config(text = nb1)


def num9():
    ajoute("9")
    label.config(text = nb1)


def num0():
    ajoute("0")
    label.config(text = nb1)


def virgule():
    ajoute(".")
    label.config(text = nb1)


def clear():
    global nb1
    nb1 = ""
    label.config(text = nb1)


def egale():
    global nb1, nb2, op
    nb1 = float(nb1)
    if op == 1 :
        resultat = round(nb2 + nb1 , 9)
    if op == 2 :
        resultat = round(nb2 - nb1 , 9)
    if op == 3 :
        resultat = round(nb2 * nb1 , 9)
    if op == 4 :
        resultat = round(nb2 / nb1 , 9)
    label.config(text = resultat)
    nb1 = ""
    nb2 = ""
    op = 0


def plus():
    global nb1, nb2, op
    nb2 = float(nb1)
    nb1 = ""
    op = 1
    label.config(text= " + ")


def moins():
    global nb1, nb2, op
    nb2 = float(nb1)
    nb1 = ""
    op = 2
    label.config(text= " - ")


def multi():
    global nb1, nb2, op
    nb2 = float(nb1)
    nb1 = ""
    op = 3
    label.config(text= " * ")


def div():
    global nb1, nb2, op
    nb2 = float(nb1)
    nb1 = ""
    op = 4
    label.config(text= " / ")


# Début du code


# le label (ligne de calcul)


label = tk.Label(root, text=" 0 ",font = ("helvetica", "30"))
label.grid(row= 0 , column= 0, columnspan = 3)

#les boutton


b_1 = tk.Button(root, text="  1  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num1)
b_1.grid(row=3, column=0)

b_2 = tk.Button(root, text="  2  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num2)
b_2.grid(row=3, column=1)

b_3 = tk.Button(root, text="  3  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num3)
b_3.grid(row=3, column=2)

b_4 = tk.Button(root, text="  4  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num4)
b_4.grid(row=2, column=0)

b_5 = tk.Button(root, text="  5  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num5)
b_5.grid(row=2, column=1)

b_6 = tk.Button(root, text="  6  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num6)
b_6.grid(row=2, column=2)

b_7 = tk.Button(root, text="  7  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num7)
b_7.grid(row=1, column=0)

b_8 = tk.Button(root, text="  8  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num8)
b_8.grid(row=1, column=1)

b_9 = tk.Button(root, text="  9  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num9)
b_9.grid(row=1, column=2)

b_0 = tk.Button(root, text="  0  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = num0)
b_0.grid(row=4, column=0 )

b_virgule = tk.Button(root, text="   .  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = virgule)
b_virgule.grid(row=4, column=1)

b_clear = tk.Button(root, text="  C  ", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = clear)
b_clear.grid(row=0, column=4)

b_egale = tk.Button(root, text= "  =  ", bg="black", fg="red", padx = pad_x, pady= pad_y, font = ("helvitica", "20"), command = egale )
b_egale.grid(row=4, column=2 )

b_plus = tk.Button(root, text="  +   ", bg="red", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = plus)
b_plus.grid(row=4, column=4)

b_moins = tk.Button(root, text="   -   ", bg="red", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = moins)
b_moins.grid(row=3, column=4)

b_multi = tk.Button(root, text="   *   ", bg="red", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = multi)
b_multi.grid(row=2, column=4)

b_div = tk.Button(root, text="   /   ", bg="red", padx = pad_x, pady = pad_y,font = ("helvetica", "20"), command = div)
b_div.grid(row=1, column=4)


root.mainloop()

def clav_1(event):
    num1()

def clav_2(event):
    num2()

def clav_3(event):
    num3()

def clav_4(event):
    num4()

def clav_5(event):
    num5()

def clav_6(event):
    num6

def clav_7(event):
    num7()

def clav_8(event):
    num8()

def clav_9(event):
    num9()

def clav_0(event):
    num0()

def clav_egale(event):
    egale()

def clav_point(event):
    virgule()

def clav_plus(event):
    plus()

def clav_moins(event):
    moins()

def clav_multi(event):
    multi()

def clav_div(event):
    div()

# root bind

root.bind("<KeyPress-1>", clav_1)
root.bind("<KeyPress-2>", clav_2)
root.bind("<KeyPress-3>", clav_3)
root.bind("<KeyPress-4>", clav_4)
root.bind("<KeyPress-5>", clav_5)
root.bind("<KeyPress-6>", clav_6)
root.bind("<KeyPress-7>", clav_7)
root.bind("<KeyPress-8>", clav_8)
root.bind("<KeyPress-9>", clav_9)
root.bind("<KeyPress-0>", clav_0)
root.bind("<return>", clav_egale)
root.bind("<KeyPress-.>", clav_point)
root.bind("<KeyPress-+>", clav_plus)
root.bind("<KeyPress-->", clav_moins)
root.bind("<KeyPress-*>", clav_multi)
root.bind("<KeyPress-/>", clav_div)

# fin
