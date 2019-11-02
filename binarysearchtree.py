from random import randint

class Node :
	def __init__(self,value):
		self.value = value
		# TODO: add depth variable 
		self.left = None
		self.right = None

	def add_child(self,node):
		if node.value < self.value:
			if self.left == None:
				self.left = node
			else:
				self.left.add_child(node)
		elif node.value > self.value:
			if self.right == None:
				self.right = node
			else:
				self.right.add_child(node)

	def visit(self):
		# TODO: make print function
		if self.left != None:
			self.left.visit()
		print(self.value)
		if self.right != None:
			self.right.visit()

	def search(self,value):
		if self.value == value:
			print(f'found {value}')
		elif value < self.value and self.left != None:
			self.left.search(value)
		elif value > self.value and self.right != None:
			self.right.search(value)
		else:
			print(f'{value} not found')
			return


class Tree :
	def __init__(self):
		self.root = None

	def add_value(self,value):
		node = Node(value)
		if self.root == None:
			self.root = node
			return
		else:
			self.root.add_child(node)

	def traverse(self):
		self.root.visit()
	
	def search(self,value):
		self.root.search(value)	

	
if __name__ == "__main__":
	tree = Tree()
	for i in range(0,15):
		tree.add_value(randint(0,100))
	tree.traverse()
	tree.search(13)
