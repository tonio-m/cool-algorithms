#TODO:board walking and cell visiting
# maze generator implementation using recursive backtracker

class Cell:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        # top, right, bottom, left
        self.walls = [True,True,True,True]
        self.visited = False

    @property
    def drawing(self):
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


class Board:
    def __init__(self,size):
        self.board = None
        self.generate_board(size)

    def generate_board(self,size):
        i,j = size
        b = [[None]*j]*i
        for i in range(len(b)):
            for j in range(len(b[i])):
                b[i][j] = Cell(i,j)
        self.board = b

    def display(self):
        b = self.board
        for i in range(len(b)):
            for j in range(len(b[i])):
                print(b[i][j].drawing,end='')
            print('\n')


    def walk(self,i,j): 
        b = self.board
        c =  b[i][j]
        c.visited = True

        neighbors = [b[i-1][j], b[i][j-1],
                        b[i+1][j], b[i][j+1]]
        for c in neighbors:
            if not c.visited:



if __name__ == '__main__':
    b = Board((10,2))
    b.display()
    b.walK(0,0)
    