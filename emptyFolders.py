# Created by Jake Stephens

# This program generates an output csv file that 
# Contains a list of all empty directories in a directory tree
# For a given directory

# To run the program navigate to the project folder
# That contains emptyFolders.py

# For windows run the command
# py emptyFolders.py <TargetDirectoryPath>

# For mac/linux run the command
# python emptyFolders.py <TargetDirectoryPath>



import os
import sys

# Main driver starts here

currentPath  = str(sys.argv[1])
output = open('list of empty folders.csv', 'w')
count = 0

# iterates through entire directory tree
for dirPath, dirs, files in os.walk('.\\'+currentPath):

	items = os.listdir(dirPath)
	# if the folder is empty
	if len(items) == 0:
		# add it to the outputfile
		output.write(dirPath+'\n')
		print(dirPath)
		count+=1

# prints the count of empty folders to the console
print (count)
# closes the output file
output.close()