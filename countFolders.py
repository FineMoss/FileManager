# Created by Jake Stephens

# This program generates an output csv file with one or two entry on each row
# Each entry is a folder name in the given directory.
# If the folder is empty, then 'empty' will be the second entry in the row.

# To run the program navigate to the project folder
# That contains countFolders.py

# For windows run the command
# py countFolders.py <TargetDirectoryPath>

# For mac/linux run the command
# python countFolders.py <TargetDirectoryPath>


import os
import sys
import csv

# Main driver starts here

path = sys.argv[1]
outputFile = open('output.csv', 'w')

# iterates through all the directories in the TargetDirectoryPath
for item in os.listdir('.\\'+path):
	print (item)

	# adds the folder to the output file
	outputFile.write(item+',')

	# if the folder is empty
	if len(os.listdir('.\\'+path+'\\'+item)) == 0:
		# adds the string 'empty' to the output file
		outputFile.write('empty,')
	# goes to a new line in the output file
	outputFile.write('\n')
	
# closes the file
outputFile.close()