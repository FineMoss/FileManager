# Created by Jake Stephens


import os
import sys
import csv


path = sys.argv[1]
outputFile = open('output.csv', 'w')

for item in os.listdir('.\\'+path):
	print (item)

	outputFile.write(item+',')

	if len(os.listdir('.\\'+path+'\\'+item)) == 0:
		outputFile.write('empty,')

	outputFile.write('\n')

outputFile.close()