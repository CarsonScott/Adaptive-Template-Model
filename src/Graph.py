class Graph:

	def __init__(self, np=0, lp=0):
		self.np = []
		self.lp = []
		self.nodes = []		
		self.links = []
		self.npCount = np
		self.lpCount = lp

	def add_node(self):
		self.nodes.append(None)
		node = len(self.nodes)-1

		self.np.append([])		
		for n in range(self.npCount):
			self.np[node].append(None)
		
	def add_link(self,i,j):
		self.links.append((i,j))
		link = len(self.links)-1

		self.lp.append([])
		for l in range(self.lpCount):
			self.lp[link].append(None)

	def get_nbhd(self,i):
		y = []
		for l in self.links:
			if l[0] == i: y.append(l[1])
			if l[1] == i: y.append(l[0])
		return y

