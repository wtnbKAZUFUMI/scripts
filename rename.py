import sys
import os

args = sys.argv
files_path =  args[1] + "/"
files = os.listdir(files_path)
for file in files:
 	try:
		filename, extention = file.split(".")
		renamedfilename = "{0:06d}".format(int(filename))
		os.rename(files_path + str(file), files_path + str(renamedfilename) + "." + str(extention))
	except ValueError:
		print str(file) + ": ValueError(not Changed)" 


