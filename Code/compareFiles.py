"""
Author : Omkar Damle and Rushikesh Nalla
ID : 201401114 and 201401106
Date : 18th April 2017

This function is used to compare two files.
"""

file1 = open(input("Give name of file 1"))
file2 = open(input("Give name of file 2"))

count = 10000
same = True
for i in range(count):
	if file1.read(1) != file2.read(1):
		same = False
		break
if same:			
	print("The files are same character by character")
else:
	print("The files are NOT same character by character")
					