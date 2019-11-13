# maze generator implementation using recursive backtracking

from random import randint

class Cell:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.walls = [True,True,True,True] # top, right, bottom, left
        self.visited = False
        self.neighbors = []

    @property
    def symbol(self):
        # ▖
        # ║═
        # ╚╔╗╝
        # ╩╠╦╣
        # ╬
        w = self.walls
        if w == [True,True,True,True]: return ' '
        elif w == [False,True,True,True]: return '║'
        elif w == [True,True,False,True]: return '║'
        elif w == [True,False,True,True]: return '═'
        elif w == [True,True,True,False]: return '═'

        elif w == [False,True,False,True]: return '║'
        elif w == [True,False,True,False]: return '═'

        elif w == [False,False,True,True]: return '╚'
        elif w == [True,False,False,True]: return '╔'
        elif w == [True,True,False,False]: return '╗'
        elif w == [False,True,True,False]: return '╝'

        elif w == [False,False,True,False]: return '╩'
        elif w == [False,False,False,True]: return '╠'
        elif w == [True,False,False,False]: return '╦'
        elif w == [False,True,False,False]: return '╣'

        elif w == [False,False,False,False]: return '╬'
    
    def picK_neighbor(self):
        # TODO: select neighbor to continue walking, remove wall between them
        r =
        n = self.neighbors[r]
        


class Board:
    def __init__(self,size):
        self.board = None
        self.generate_board(size)
        self.generate_neighbors()

    def generate_board(self,size):
        i,j = size
        b = self.board
        b = [[None]*j]*i
        for i in range(len(b)):
            for j in range(len(b[i])):
                b[i][j] = Cell(i,j)
    
    def generate_neighbors(self):
        for i in range(len(b)):
            for j in range(len(b[i])):
                neighbors = [
                    get_cell(i-1,j),
                    get_cell(i,j+1),
                    get_cell(i+1,j),
                    get_cell(i,j-1)
                ]
                b[i][j].neighbors = list(filter(lambda c: c != None,neighbors))

    def get_cell(self,i,j):
        if i < len(self.board):
            if j < len(self.board[i]):
                return self.board[i][j]
        return
    
    def display(self):
        b = self.board
        for i in range(len(b)):
            for j in range(len(b[i])):
                print(b[i][j].symbol,end='')
            print('\n')

    def walk(self,i,j):
        # TODO: implement recursive walking
        c = get_cell(i,j)
        c.visited = True

        # if not n.visited:
        #     walk(n.i,n.j)
        

if __name__ == '__main__':
    b = Board((10,2))
    b.display()
    b.display()