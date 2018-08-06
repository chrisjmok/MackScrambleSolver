from testParse import Test
import sys
import os

# class Bank():
# 	def __init__(self):
def makeBank(directory):
	bank = {}
	for filename in os.listdir(os.getcwd()+'/'+directory):
		print filename
		if filename.endswith('.mack'):
			bank[filename] = Test(filename)
	return bank

def main():
	tests = makeBank(str(sys.argv[1]))
	print(tests)
	for key in tests:
	 	tests[key].readTest(sys.argv[1])


#if main defines runs main  
if __name__== "__main__":
  main()