
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
root.mainloop()