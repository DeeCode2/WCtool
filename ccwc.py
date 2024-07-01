import argparse
import os
import re
import sys

parser = argparse.ArgumentParser(description = "Command line WC tool")
parser.add_argument("-c", nargs = '*', help = "print num of bytes in file", default=sys.stdin)
parser.add_argument("-l", nargs = '*', help="print num of lines in file")
parser.add_argument("-w", nargs = '*', help="print num of words in file")
parser.add_argument("-m", nargs = '*', help="print num of characters in file")
parser.add_argument("-a", nargs = '*', help="print num of bytes, lies, words, and characters in file")

#parse args from standard input
args = parser.parse_args()

def getbytes(myfile):
	filedata = os.stat(myfile)
	return filedata.st_size
	
def getlines(myfile):
	with open(myfile, "r") as file:
		for count, line in enumerate(file):
			pass
	return count + 1

def getwords(myfile):
	with open(myfile, "r") as file:
		lines =  file.read()
		return len(lines.rstrip().split())
	
def getchars(myfile):
	with open(myfile, "r") as file:
		data = file.read()
		return len(re.findall(r'\S', data))
		
def getall(myfile):
	with open(myfile, "r") as file:
		print(getbytes(myfile), getlines(myfile), getwords(myfile), myfile)
		
#check is arg has any input data
if args.c:
	print(getbytes(args.c[0]), args.c[0])
elif args.l:
	print(getlines(args.l[0]), args.l[0])
elif args.m:
	print(getchars(args.m[0]), args.m[0])
elif args.a:
	getall(args.a[0])
