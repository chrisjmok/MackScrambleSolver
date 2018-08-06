import re

class Scramble():

	def __init__(self, fname):
		file = open(fname, 'r')
		text = file.read()
		self.words = re.split('\W+', text)
		self.set = set(self.words)
		self.counts = {}
		for word in self.words:
			self.counts[word] = 0

