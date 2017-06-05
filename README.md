# FileManager
Provides python scripts for manipulating files and directories 

Directions for use is in the comments of the python files


Basic Overview:

moveToArchives.py   - Moves all files that are older than M months to an Archive directory and removes the files from the current directory.

removeDuplicates.py - Removes all files that exist in the active directory only if they exist in the archive directory. With exception of .sfprime hidden files.

countFolders.py     - Generates an output.csv file. The first entry in each row is a directory in the TargetFilePath. The second entry, if there is one, says if that folder is empty with the string 'empty'
