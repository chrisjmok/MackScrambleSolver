from testParse import Test
from scramble import Scramble
import sys
import os

# class Bank():
# 	def __init__(self):
def display(tests):
	for key in tests:
		print("Display")
		tests[key].display()

def makeBank(directory):
	bank = {}
	for filename in os.listdir(os.getcwd()+'/'+directory):
		print filename
		if filename.endswith('.mack'):
			bank[filename] = Test(filename)
	return bank

def main():
	scramble = Scramble(sys.argv[2])
	print(scramble.counts)
	tests = makeBank(str(sys.argv[1]))
	#print(tests)
	for key in tests:
	 	tests[key].readTest(sys.argv[1])
		tests[key].check(scramble)
	display(tests)

#if main defines runs main  
if __name__== "__main__":
  main()