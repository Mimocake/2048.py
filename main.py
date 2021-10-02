import random
from tkinter import *


def proection():
    label00.config(text=is0(field[0][0]))
    label01.config(text=is0(field[0][1]))
    label02.config(text=is0(field[0][2]))
    label03.config(text=is0(field[0][3]))
    label10.config(text=is0(field[1][0]))
    label11.config(text=is0(field[1][1]))
    label12.config(text=is0(field[1][2]))
    label13.config(text=is0(field[1][3]))
    label20.config(text=is0(field[2][0]))
    label21.config(text=is0(field[2][1]))
    label22.config(text=is0(field[2][2]))
    label23.config(text=is0(field[2][3]))
    label30.config(text=is0(field[3][0]))
    label31.config(text=is0(field[3][1]))
    label32.config(text=is0(field[3][2]))
    label33.config(text=is0(field[3][3]))


def is0(a):
    if not a == 0:
        return str(a)


def counter_0():
    global field
    count = 0
    for i in field:
        for j in i:
            if j == 0:
                count += 1
    return count


def new_step():
    randvar = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    a = random.randint(0, 3)
    b = random.randint(0, 3)
    for i in range(2):
        while field[a][b] != 0:
            a = random.randint(0, 3)
            b = random.randint(0, 3)
        field[a][b] = random.choice(randvar)
    proection()


def move_up(a):
    global field
    for j in range(4):
        for i in range(3):
            if field[i][j] == 0:
                i2 = i
                while i2 < 3 and field[i2][j] == 0:
                    i2 += 1
                field[i][j], field[i2][j] = field[i2][j], 0
            elif i == 0 and (field[i][j] == field[i+3][j] or
                             field[i][j] == field[i + 2][j] or
                             field[i][j] == field[i + 1][j]):
                field[i][j], field[i+3][j] = field[i][j]*2, 0
            elif i == 1 and (field[i][j] == field[i+2][j] or
                             field[i][j] == field[i+1][j]):
                field[i][j], field[i+2][j] = field[i][j] * 2, 0
            elif i == 2 and field[i][j] == field[i+1][j]:
                field[i][j], field[i+1][j] = field[i][j]*2, 0
            else:
                continue
    new_step()


def move_left(a):
    global field
    for i in range(4):
        for j in range(3):
            if field[i][j] == 0:
                j2 = j
                while j2 < 3 and field[i][j2] == 0:
                    j2 += 1
                field[i][j], field[i][j2] = field[i][j2], 0
            elif j == 0 and (field[i][j] == field[i][j+3] or
                             field[i][j] == field[i][j+2] or
                             field[i][j] == field[i][j+1]):
                field[i][j], field[i][j+3] = field[i][j] * 2, 0
            elif j == 1 and (field[i][j] == field[i][j + 2] or
                             field[i][j] == field[i][j + 1]):
                field[i][j], field[i][j + 2] = field[i][j] * 2, 0
            elif j == 2 and field[i][j] == field[i][j+1]:
                field[i][j], field[i][j+1] = field[i][j] * 2, 0
            else:
                continue
    new_step()


def move_down(a):
    global field
    for j in range(4):
        for i in range(3, 0, -1):
            if field[i][j] == 0:
                i2 = i
                while i2 > 0 and field[i2][j] == 0:
                    i2 -= 1
                field[i][j], field[i2][j] = field[i2][j], 0
            elif i == 3 and (field[i][j] == field[i - 3][j] or
                             field[i][j] == field[i - 2][j] or
                             field[i][j] == field[i - 1][j]):
                field[i][j], field[i - 3][j] = field[i][j] * 2, 0
            elif i == 2 and (field[i][j] == field[i - 2][j] or
                             field[i][j] == field[i - 1][j]):
                field[i][j], field[i - 2][j] = field[i][j] * 2, 0
            elif i == 1 and field[i][j] == field[i - 1][j]:
                field[i][j], field[i - 1][j] = field[i][j] * 2, 0
            else:
                continue
    new_step()


def move_right(a):
    global field
    for i in range(4):
        for n in range(3):
            j2 = 3
            while j2 > 0:
                if field[i][j2] == 0:
                    field[i][j2 - 1], field[i][j2] = 0, field[i][j2-1]
                elif field[i][j2] == field[i][j2-1]:
                    field[i][j2-1], field[i][j2] = 0, field[i][j2]*2
                j2 = j2 - 1
    new_step()


field = [[0]*4 for i in range(4)]

window = Tk()

window.bind("<w>", move_up)
window.bind('<a>', move_left)
window.bind('<s>', move_down)
window.bind('<d>', move_right)

label00 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label01 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label02 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label03 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label10 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label11 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label12 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label13 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label20 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label21 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label22 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label23 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label30 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label31 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label32 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)
label33 = Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=5)

label00.grid(row=0, column=0)
label01.grid(row=0, column=1)
label02.grid(row=0, column=2)
label03.grid(row=0, column=3)
label10.grid(row=1, column=0)
label11.grid(row=1, column=1)
label12.grid(row=1, column=2)
label13.grid(row=1, column=3)
label20.grid(row=2, column=0)
label20.grid(row=2, column=0)
label21.grid(row=2, column=1)
label22.grid(row=2, column=2)
label23.grid(row=2, column=3)
label30.grid(row=3, column=0)
label31.grid(row=3, column=1)
label32.grid(row=3, column=2)
label33.grid(row=3, column=3)

new_step()

window.mainloop()
