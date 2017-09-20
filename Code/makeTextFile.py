"""
Author : Omkar Damle and Rushikesh Nalla
ID : 201401114 and 201401106
Date : 18th April 2017

The function in this file is used to create random text files.
"""

import random

with open("longRandomText.txt","w+") as file:
	for i in range(10000):
		file.write(str(random.randint(0,9)))
		