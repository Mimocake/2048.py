import random
from tkinter import *


def proection():
    for i in range(4):
        for j in range(4):
            tiles[i][j].config(text=is0(field[i][j]), bg=colorchooser(field[i][j]))
    label_score.config(text=("Score: "+str(score)))


def colorchooser(a):
    colors = {
        0: "#CCC0B3",
        2: "#EEE4DA",
        4: "#EDE0C8",
        8: "#F2B179",
        16: "#F59563",
        32: "#F67C5F",
        64: "#F65E3B",
        128: "#EDCC72",
        256: "#EDCF61",
        512: "#EDC850",
        1024: "#EDC53F",
        2048: "#EDC22E",
    }

    for i in colors.keys():
        if a > 2048:
            return colors.get(2048)
        elif a == i:
            return colors.get(i)


def is0(a):
    if not a == 0:
        return str(a)
    else:
        return ' '


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
    global score
    field2 = [[i for i in o] for o in field]
    for j in range(4):
        for n in range(4):
            for i in range(3):
                if field[i][j] == 0:
                    field[i][j], field[i+1][j] = field[i+1][j], 0
                elif field[i][j] == field[i+1][j]:
                    score += field[i][j]
                    field[i][j], field[i+1][j] = field[i][j]*2, 0
    if field2 != field:
        new_step()
    else:
        pass


def move_down(a):
    global field
    global score
    field2 = [[i for i in o] for o in field]
    for j in range(4):
        for n in range(4):
            for i in range(3, 0, -1):
                if field[i][j] == 0:
                    field[i-1][j], field[i][j] = 0, field[i-1][j]
                elif field[i][j] == field[i-1][j]:
                    score += field[i][j]
                    field[i-1][j], field[i][j] = 0, field[i][j]*2
    if field2 != field:
        new_step()
    else:
        pass


def move_right(a):
    global field
    global score
    field2 = [[i for i in o] for o in field]
    for i in range(4):
        for n in range(3):
            for j2 in range(3, 0, -1):
                if field[i][j2] == 0:
                    field[i][j2 - 1], field[i][j2] = 0, field[i][j2-1]
                elif field[i][j2] == field[i][j2-1]:
                    score += field[i][j2]
                    field[i][j2-1], field[i][j2] = 0, field[i][j2]*2
    if field2 != field:
        new_step()
    else:
        pass


def move_left(a):
    global field
    global score
    field2 = [[i for i in o] for o in field]
    for i in range(4):
        for n in range(4):
            for j in range(3):
                if field[i][j] == 0:
                    field[i][j], field[i][j+1] = field[i][j+1], 0
                elif field[i][j] == field[i][j+1]:
                    score += field[i][j]
                    field[i][j], field[i][j+1] = field[i][j]*2, 0
    if field2 != field:
        new_step()
    else:
        pass


field = [[0]*4 for i in range(4)]
score = 0

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
tiles = [[Label(window, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=2)
          for j in range(4)] for k in range(4)]
label_score = Label(window, text='Score: 0', font=("Arial", 45))

for i in range(4):
    for j in range(4):
        tiles[i][j].grid(row=i, column=j)

label_score.grid(row=4, column=0, columnspan=4)

new_step()
new_step()

window.mainloop()
