class Symbol:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def parse_string(self,string):
        errormsg = "it's not a well-formed formula"
        if len(string) is 0:
            raise Exception(errormsg)
        if string[0] is '¬':
            self.value = '¬'
            self.right = Symbol()
            self.right.parse_string(string[1:])
            return
        
        if len(string) is 1:
            if 65 <= ord(string) <= 90:
                self.value = string
                return
        
        string = string[1:-1]
            
        depth = 0
        for i in range(len(string)):
            c = string[i]
            if c is '(':
                depth += 1
            elif c is ')':
                depth -= 1
            
            if self.isbinaryoperator(c) and depth == 0:
                self.value = c
                self.left = Symbol()
                self.left.parse_string(string[:i])
                self.right = Symbol()
                self.right.parse_string(string[i+1:])
                return
        raise Exception(errormsg)

    def visit(self, lvl = ''):
        if self.isbinaryoperator(self.value):
            print(lvl + '(')
        if self.left is not None:
            self.left.visit(lvl + '\t')
        print(lvl + self.value)
        if self.right is not None:
            self.right.visit(lvl + '\t')
        if self.isbinaryoperator(self.value):
            print(lvl + ')')

    @staticmethod
    def isbinaryoperator(char):
        if char in ['⊃','⇔','∧','∨']:
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

