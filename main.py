from tkinter import *
import random


def is0(a):
    if not a == 0:
        return str(a)
    else:
        return ' '


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


class Tile:

    def __init__(self, row, column):
        self.r = int(row)
        self.c = int(column)


class Screen(object):

    def __init__(self, size):
        self.size = size
        self.screen = Tk()
        self.screen.title("2048")
        self.screen.resizable(False, False)
        self.tiles = [[Label(self.screen, text='', font=('Arial', 30), height=2, width=4, relief=RAISED, bd=2)
                    for j in range(size)] for k in range(size)]
        for i in range(size):
            for j in range(size):
                self.tiles[i][j].grid(row=i, column=j)
        self.label_score = Label(self.screen, text='Score: 0', font=("Arial", 40))
        self.label_score.grid(row=size, column=0, columnspan=size)
        Button(self.screen, text='Restart', font=("Arial", 45), bd=2).grid(row=size+1, column=0, columnspan=size)
        self.l_lose = Label(self.screen, text="", font=("Arial", 45))
        self.l_lose.grid(row=size, column=0)

    def project(self, brd, score):
        for i in range(self.size):
            for j in range(self.size):
                self.tiles[i][j].config(text=is0(brd[i][j]), bg=colorchooser(brd[i][j]))
        self.label_score.config(text=("Score: " + str(score)))
        self.screen.update()


class Board(object):

    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for i in range(size)]
        self.score = 0

    def new_step(self):
        free = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.board[i][j] == 0:
                    free.append(Tile(i, j))
        if len(free) == 0:
            print("Game over")
            return None
        rtile = random.choice(free)
        self.board[rtile.r][rtile.c] = (random.randint(0, 9) == 9) * 2 + 2

    def rotate(self, direc):
        board2 = [[] * self.size for i in range(self.size)]
        for i in range(0, self.size):
            board2.append([])
            for j in range(0, self.size):
                board2[i].append(self.board[i][j])
        for i in range(0, self.size):
            for j in range(0, self.size):
                if direc == -90:
                    self.board[i][j] = board2[self.size - 1 - j][i]
                elif direc == 90:
                    self.board[self.size - 1 - j][i] = board2[i][j]

    def compress(self):
        for k in range(self.size-1):
            for i in range(self.size-1, k, -1):
                for j in range(self.size):
                    if self.board[i-1][j] != 0 and self.board[i][j] == 0:
                        self.board[i][j] = self.board[i-1][j]
                        self.board[i-1][j] = 0

    def merge(self):
        for k in range(self.size-1):
            for i in range(self.size-1, k, -1):
                for j in range(self.size):
                    if self.board[i-1][j] == self.board[i][j]:
                        self.board[i][j] *= 2
                        self.score += self.board[i][j]
                        self.board[i-1][j] = 0

    def move_up(self, event):
        self.rotate(90)
        self.rotate(90)
        self.compress()
        self.merge()
        self.compress()
        self.rotate(90)
        self.rotate(90)
        self.new_step()
        screen.project(self.board, self.score)

    def move_down(self, event):
        self.compress()
        self.merge()
        self.compress()
        self.new_step()
        screen.project(self.board, self.score)

    def move_left(self, event):
        self.rotate(90)
        self.compress()
        self.merge()
        self.compress()
        self.rotate(-90)
        self.new_step()
        screen.project(self.board, self.score)

    def move_right(self, event):
        self.rotate(-90)
        self.compress()
        self.merge()
        self.compress()
        self.rotate(90)
        self.new_step()
        screen.project(self.board, self.score)

    def print(self):
        for i in range(0, self.size):
            print('|'.join(map(str, self.board[i])))


size = int(input("Enter board size: "))
screen = Screen(size)
board = Board(size)
screen.screen.bind('<w>', board.move_up)
screen.screen.bind('<a>', board.move_left)
screen.screen.bind('<s>', board.move_down)
screen.screen.bind('<d>', board.move_right)
board.new_step()
board.new_step()
screen.project(board.board, board.score)
screen.screen.mainloop()
