# Created by Jake Stephens

# This program will move all files that are older than M months
# To an Archive directory and remove them from the current directory

# To run the program navigate to the project folder
# That contains moveToArchives.py, the directory that needs files moved to archives
# And the archives directory

# For windows run the command
# py moveToArchives.py <currentPath> <targetPath> <M>

# For mac/linux run the command
# python moveToArchives.py <currentPath> <targetPath> <M>


import sys
import os
import datetime
import shutil


# Main driver starts here

currentPath  = sys.argv[1]
targetPath   = sys.argv[2]
inputMonths  = sys.argv[3]

# Provides the current date, and parses out the month and year
currentDate  = str(datetime.datetime.now())
currentYear  = int(currentDate[0:4])
currentMonth = int(currentDate[5:7])

# computes target year and month 
targetMonth  = currentMonth-int(inputMonths)
targetYear   = currentYear
while targetMonth <= 0:
	targetYear-=1
	targetMonth+=12


# running count of total files moved
count = 0

# iterate through all directories in currentPath
for dirPath, dirs, files in os.walk('.\\'+currentPath):
	
	# updates path
	split = dirPath.split('\\')
	split[1] = targetPath
	newPath = '\\'.join(split)
	
	# if the directory does not exist in archives then add it
	if not os.path.isdir(newPath):
		os.makedirs(newPath)

	# iterate through all files in all directories in currentPath
	for item in os.listdir(dirPath):

		# update file path
		filePath = dirPath+'\\'+item

		# if it is a file
		if os.path.isfile(filePath):
			
			# make sure its not .sfprime
			if filePath.split('\\').pop() != '.sfprime':
				
				# get date last modified
				t = os.path.getmtime(filePath)
				modDate  = str(datetime.datetime.fromtimestamp(t))
				modYear  = int(modDate[0:4])
				modMonth = int(modDate[5:7])
				
				# if date last modified was longer than specified date
				if modYear <= targetYear and modMonth <= targetMonth:
					print (filePath)
					print (modDate)
					# increment counter
					count+=1

					# update path
					split2 = filePath.split('\\')
					split2[1] = targetPath
					newPath2 = '\\'.join(split2)

					# move file to archive directory
					shutil.move(filePath, newPath2)


# Print total files moved
print ('Total files moved to archives: '+str(count))









