import random


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
    if counter_0() >= 2:
        for i in range(2):
            while field[a][b] != 0:
                a = random.randint(0, 3)
                b = random.randint(0, 3)
            field[a][b] = random.choice(randvar)
    elif counter_0() == 1:
        while field[a][b] != 0:
            a = random.randint(0, 3)
            b = random.randint(0, 3)
        field[a][b] = random.choice(randvar)
    else:
        print('You lose!')
    for i in range(4):
        print('|'.join(map(str, field[i])))


def move_up():
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


def move_left():
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


def move_down():
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


def move_right():
    global field
    for i in range(4):
        for j in range(3, 0, -1):
            if field[i][j] == 0:
                j2 = j
                while j2 < 0 and field[i][j2] == 0:
                    j2 -= 1
                field[i][j], field[i][j2] = field[i][j2], 0
            elif j == 3 and (field[i][j] == field[i][j - 3] or
                             field[i][j] == field[i][j - 2] or
                             field[i][j] == field[i][j - 1]):
                field[i][j], field[i][j - 3] = field[i][j] * 2, 0
            elif j == 2 and (field[i][j] == field[i][j - 2] or
                             field[i][j] == field[i][j - 1]):
                field[i][j], field[i][j - 2] = field[i][j] * 2, 0
            elif j == 1 and field[i][j] == field[i][j - 1]:
                field[i][j], field[i][j - 1] = field[i][j] * 2, 0
            else:
                continue


field = [[0]*4 for i in range(4)]
new_step()
while True:
    a = input('Print W to move up, A to move left, S to move down or D to move right: ')
    a.lower()
    if a == 'w':
        move_up()
        new_step()
    elif a == 'a':
        move_left()
        new_step()
    elif a == 's':
        move_down()
        new_step()
    elif a == 'd':
        move_right()
        new_step()
    else:
        continue
