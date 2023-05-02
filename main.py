from tkinter import *
import random


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
        self.tiles = [[Label(self.screen, text='', font=('Arial', 30),
                             height=2, width=4, relief=RAISED, bd=2)
                             for j in range(size)] for k in range(size)]
        for i in range(size):
            for j in range(size):
                self.tiles[i][j].grid(row=i, column=j)
        self.label_score = Label(self.screen, text='Score: 0', font=("Arial", 40))
        self.label_score.grid(row=size, column=0, columnspan=size)
        Button(self.screen, command=self.restart, text='Restart',
               font=("Arial", 45), bd=2).grid(row=size+1, column=0, columnspan=size)
        self.l_lose = Label(self.screen, text="", font=("Clear Sans", 45))
        self.l_lose.grid(row=size, column=0)

    def project(self):
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
        for i in range(self.size):
            for j in range(self.size):
                self.tiles[i][j].config(text=(board.board[i][j] if board.board[i][j] != 0 else ""),
                                        bg=colors.get(2048) if board.board[i][j] > 2048
                                        else colors.get(board.board[i][j]))
        self.label_score.config(text=("Score: " + str(board.score)))
        self.screen.update()

    def restart(self):
        board.board = [[0] * size for i in range(size)]
        board.score = 0
        board.new_step()
        board.new_step()
        self.l_lose = Label(self.screen, text="", font=("Arial", 45))
        self.l_lose.grid(row=size, column=0)
        self.project()

    def game_over(self):
        self.l_lose.grid(row=self.size+2, column=0, columnspan=4)
        self.l_lose.config(text="You lose!")
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
        for i in self.board:
            if 0 not in i:
                if self.game_over():
                    screen.game_over()
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

    def move(self):
        for j in range(4):
            for n in range(4):
                for i in range(3, 0, -1):
                    if self.board[i][j] == 0:
                        self.board[i - 1][j], self.board[i][j] = 0, self.board[i - 1][j]
                    elif self.board[i][j] == self.board[i - 1][j]:
                        self.score += self.board[i][j] * 2
                        self.board[i - 1][j], self.board[i][j] = 0, self.board[i][j] * 2

    def game_over(self):
        b = True
        for i in range(4):
            for j in range(3):
                if board.board[i][j] == board.board[i][j + 1]:
                    b = False
        for j in range(4):
            for i in range(3):
                if board.board[i][j] == board.board[i + 1][j]:
                    b = False
        return b

    def move_up(self, event):
        board2 = [[i for i in o] for o in board.board]
        self.rotate(90)
        self.rotate(90)
        self.move()
        self.rotate(90)
        self.rotate(90)
        if board2 != board.board:
            self.new_step()
        screen.project()

    def move_down(self, event):
        board2 = [[i for i in o] for o in board.board]
        self.move()
        if board2 != board.board:
            self.new_step()
        screen.project()

    def move_left(self, event):
        board2 = [[i for i in o] for o in board.board]
        self.rotate(90)
        self.move()
        self.rotate(-90)
        if board2 != board.board:
            self.new_step()
        screen.project()

    def move_right(self, event):
        board2 = [[i for i in o] for o in board.board]
        self.rotate(-90)
        self.move()
        self.rotate(90)
        if board2 != board.board:
            self.new_step()
        screen.project()


size = int(input("Enter board size: "))
screen = Screen(size)
board = Board(size)
screen.screen.bind('<w>', board.move_up)
screen.screen.bind('<a>', board.move_left)
screen.screen.bind('<s>', board.move_down)
screen.screen.bind('<d>', board.move_right)
board.new_step()
board.new_step()
screen.project()
screen.screen.mainloop()
