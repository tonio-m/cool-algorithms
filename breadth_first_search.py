import json

class Node:
	def __init__(self,value):
		self.value = value
		self.edges = []
		self.parent = None
		self.checked = False
	
	def add_edge(self,node):
		self.edges.append(node)
	
	def check(self,value):
		self.checked = True
		if self.value == value:
			return True
		else:
			return False


class Graph:
	def __init__(self):
		self.nodes = []
		self.graph = {}
		self.queue = []

	def add_node(self,node):
		self.nodes.append(node)
		self.graph[node.value] = node
	
	def get_node(self,key):
		if key in self.graph:
			return self.graph[key]
		return None
	
	def find(self,start,end):
		start_node = self.get_node(start)
		self.queue.append(start_node)
		self.search(end)
	
	def search(self,value):
		while self.queue:
			current = self.queue[0]
			if current.check(value):
				path = self.trace_path(current)
				print(f'found! with path {path}')
				return
			self.queue.pop(0)
			for n in current.edges:
				if not n.checked:
					n.parent = current
					self.queue.append(n)
		print('not found')
	
	@staticmethod
	def trace_path(end):
		path = []
		current = end
		while current != None:
			path.insert(0,current.value)
			current = current.parent
		return '.'.join(path)

def load(movies):
	for movie in movies:
	title = movie['title']
	cast = movie['cast']
	movie_node = Node(title)
	graph.add_node(movie_node)

	for actor in cast:
		actor_node = graph.get_node(actor)
		if actor_node is None:
			actor_node = Node(actor)
			graph.add_node(actor_node)
		movie_node.add_edge(actor_node)
		actor_node.add_edge(movie_node)

if __name__ == '__main__':
	graph = Graph()
	
	f = json.loads(open('data/kevin_bacon.json','r').read())
	movies = f['movies']
	
	for movie in movies:
		title = movie['title']
		cast = movie['cast']
		movie_node = Node(title)
		graph.add_node(movie_node)

		for actor in cast:
			actor_node = graph.get_node(actor)
			if actor_node is None:
				actor_node = Node(actor)
				graph.add_node(actor_node)
			movie_node.add_edge(actor_node)
			actor_node.add_edge(movie_node)

	
	graph.find("Kevin Bacon","Eat Pray Love")
