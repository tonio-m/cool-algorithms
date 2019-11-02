class Symbol:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def parse_string(self,string):
        if len(string) is 1:
            self.value = string
            return
        if string[0] is '(' and string[-1] is ')':
            string = string[1:-1]
        depth = 0
        for i in range(len(string)):
            c = string[i]
            if c is "(":
                depth += 1
            elif c is ")":
                depth -=1
            
            if self.isoperator(c) and depth == 0:
                self.value = c
                if len(string[:i]) is not 0:
                    self.left = Symbol()
                    self.left.parse_string(string[:i])
                if len(string[i+1:]) is not 0:
                    self.right = Symbol()
                    self.right.parse_string(string[i+1:])

    def visit(self):
        if self.left is not None:
            self.left.visit()
        print(self.value)
        if self.right is not None:
            self.right.visit()

    @staticmethod
    def isoperator(char):
        if char in ['⊃','⇔','∧','∨','¬']:
            return True
        return False


class Expression:
    def __init__(self):
        self.root = Symbol()
    
    def from_string(self,string):
        self.root.parse_string(string)
    
    def traverse(self):
        self.root.visit()


if __name__ == '__main__':
    e = Expression()
    e.from_string('((Q∧S)⊃((S∨R)∨R))')
    e.traverse()