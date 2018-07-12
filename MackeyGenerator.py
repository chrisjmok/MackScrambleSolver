import sys
import string
import re
import os
import PyPDF2

#Command Line argument sample
def printArgs():
	print 'printArgs---'
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
	print 'First Arg', str(sys.argv[1])
	print '==============='

#read File sample
def readFile():
	print 'readFile---'
	f = open (str(sys.argv[1]), 'r')
	print ''
	for line in f:
		print line
	print '==============='
	f.close()

def insertLineDict(line):
	print "not yet implemented"

def stripPunc(line):
	#print 'stripPunc---'
	noNewLIne = line.strip('\n')
	out = re.split('\W+', noNewLIne)
	#for word in out:
		#print word
	#print '==============='
	return out
 

def makeFileDict(filename):
	#print '\n\nmakeFileDict-------\n'
	library = {}
	for line in filename:
		arrayLine = stripPunc(line)
		for word in arrayLine:
			if word not in library and word != '':
				#print word
				library[word] = 1
	#print '\n================\n'
	return library


def makeBank(directory):
	bank = {}
	for filename in os.listdir(os.getcwd()+'/'+directory):
		print filename
		if filename.endswith('.mack'):
			bank[filename] = makeFileDict(filename)
	return bank


#main function
def main():
	# file = open (str(sys.argv[1]), 'r')
	# file.close()
	bank = makeBank('bank')
	print bank



#if main defines runs main  
if __name__== "__main__":
  main()