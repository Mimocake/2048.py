import random
from tkinter import *


def proection():
    label00.config(text=is0(field[0][0]), bg=colorchooser(field[0][0]))
    label01.config(text=is0(field[0][1]), bg=colorchooser(field[0][1]))
    label02.config(text=is0(field[0][2]), bg=colorchooser(field[0][2]))
    label03.config(text=is0(field[0][3]), bg=colorchooser(field[0][3]))
    label10.config(text=is0(field[1][0]), bg=colorchooser(field[1][0]))
    label11.config(text=is0(field[1][1]), bg=colorchooser(field[1][1]))
    label12.config(text=is0(field[1][2]), bg=colorchooser(field[1][2]))
    label13.config(text=is0(field[1][3]), bg=colorchooser(field[1][3]))
    label20.config(text=is0(field[2][0]), bg=colorchooser(field[2][0]))
    label21.config(text=is0(field[2][1]), bg=colorchooser(field[2][1]))
    label22.config(text=is0(field[2][2]), bg=colorchooser(field[2][2]))
    label23.config(text=is0(field[2][3]), bg=colorchooser(field[2][3]))
    label30.config(text=is0(field[3][0]), bg=colorchooser(field[3][0]))
    label31.config(text=is0(field[3][1]), bg=colorchooser(field[3][1]))
    label32.config(text=is0(field[3][2]), bg=colorchooser(field[3][2]))
    label33.config(text=is0(field[3][3]), bg=colorchooser(field[3][3]))


def colorchooser(a):
    if a == 0:
        return "#CCC0B3"
    elif a == 2:
        return "#EEE4DA"
    elif a == 4:
        return "#EDE0C8"
    elif a == 8:
        return "#F2B179"
    elif a == 16:
        return "#F59563"
    elif a == 32:
        return "#F67C5F"
    elif a == 64:
        return "#F65E3B"
    elif a == 128:
        return "#EDCC72"
    elif a == 256:
        return "#EDCF61"
    elif a == 512:
        return "#EDC850"
    elif a == 1024:
        return "#EDC53F"
    elif a >= 2048:
        return "#EDC22E"


def is0(a):
    if not a == 0:
        return str(a)
    else:
        return ' '


def counter_0():
    global field
    count = 0
    for i in field:
        for j in i:
            if j == 0:
                count += 1
    return count


def new_step():
    global field
    randvar = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    a = random.randint(0, 3)
    b = random.randint(0, 3)
    while field[a][b] != 0:
        a = random.randint(0, 3)
        b = random.randint(0, 3)
    field[a][b] = random.choice(randvar)
    proection()


def move_up(a):
    global field
    for j in range(4):
        for n in range(4):
            for i in range(3):
                if field[i][j] == 0:
                    field[i][j], field[i+1][j] = field[i+1][j], 0
                elif field[i][j] == field[i+1][j]:
                    field[i][j], field[i+1][j] = field[i][j]*2, 0
    new_step()


def move_down(a):
    global field
    for j in range(4):
        for n in range(4):
            for i in range(3, 0, -1):
                if field[i][j] == 0:
                    field[i-1][j], field[i][j] = 0, field[i-1][j]
                elif field[i][j] == field[i-1][j]:
                    field[i-1][j], field[i][j] = 0, field[i][j]*2
    new_step()


def move_right(a):
    global field
    for i in range(4):
        for n in range(3):
            for j2 in range(3, 0, -1):
                if field[i][j2] == 0:
                    field[i][j2 - 1], field[i][j2] = 0, field[i][j2-1]
                elif field[i][j2] == field[i][j2-1]:
                    field[i][j2-1], field[i][j2] = 0, field[i][j2]*2
    new_step()


def move_left(a):
    global field
    for i in range(4):
        for n in range(4):
            for j in range(3):
                if field[i][j] == 0:
                    field[i][j], field[i][j+1] = field[i][j+1], 0
                elif field[i][j] == field[i][j+1]:
                    field[i][j], field[i][j+1] = field[i][j]*2, 0
    new_step()


field = [[0]*4 for i in range(4)]

window = Tk()

window.bind('<w>', move_up)
window.bind('<a>', move_left)
window.bind('<s>', move_down)
window.bind('<d>', move_right)
window.bind('<W>', move_up)
window.bind('<A>', move_left)
window.bind('<S>', move_down)
window.bind('<D>', move_right)
window.bind('<Up>', move_up)
window.bind('<Left>', move_left)
window.bind('<Down>', move_down)
window.bind('<Right>', move_right)

label00 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label01 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label02 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label03 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label10 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label11 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label12 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label13 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label20 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label21 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label22 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label23 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label30 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label31 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label32 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)
label33 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RIDGE,bd=5)

label00.grid(row=0, column=0)
label01.grid(row=0, column=1)
label02.grid(row=0, column=2)
label03.grid(row=0, column=3)
label10.grid(row=1, column=0)
label11.grid(row=1, column=1)
label12.grid(row=1, column=2)
label13.grid(row=1, column=3)
label20.grid(row=2, column=0)
label21.grid(row=2, column=1)
label22.grid(row=2, column=2)
label23.grid(row=2, column=3)
label30.grid(row=3, column=0)
label31.grid(row=3, column=1)
label32.grid(row=3, column=2)
label33.grid(row=3, column=3)

new_step()
new_step()

window.mainloop()
