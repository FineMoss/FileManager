# Created by Jake Stephens

# This program removes all files that exist in the active directory
# Only if they exist in the archive directory
# with exception of .sfprime hidden files
# The program, archive directory, and active directory must all be in the same directory

# to run on windows machine
# navigate to the directory with the program
# run the command: py removeDuplicates.py <archive> <active>

# to run on mac or linux machine 
# navigate to the directory with the program
# run the command: python removeDuplicates.py <archive> <active>


import sys
import os


# Main driver starts here

archive = sys.argv[1]
active = sys.argv[2]
count = 0

# iterate through all directories in archive
for dirpath, dirs, files in os.walk('.\\'+archive):
	print (dirpath)
	# iterate through all files in all directories in archive
	for item in os.listdir(dirpath):
		
		# update file path
		archivepath = dirpath+'\\'+item

		# if it is a file in archive
		if os.path.isfile(archivepath):
			
			split = archivepath.split('\\')
			split[1] = active
			activepath = '\\'.join(split)

			# and it if exists in active
			if os.path.isfile(activepath):

				# if the file is not .sfprime
				if activepath.split('\\').pop() != '.sfprime':
					
					# remove file from active
					os.remove(activepath)
					print ('removed: '+activepath)
					count+=1


#  prints total number of files removed
print ('Total files deleted: '+str(count))









