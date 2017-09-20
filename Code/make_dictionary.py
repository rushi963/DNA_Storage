"""
Author : Omkar Damle and Rushikesh Nalla
ID : 201401114 and 201401106
Date : 18th April 2017

This function in this file is used to make the codebook.
"""

#Let us make a dictionary - later we replace this by code book generation

import edit_distance
import random

def codeBookGen():

	#dic = {"1":"ATTC","2":"ACTA","3":"ATTA","4":"TATA","5":"AATC","6":"ACAA","7":"TTTC","0":"TCTA",}

	#generate all possible sequences of length 4
	pool = []

	print("Making dictionary")

	for i in range(256):
		temp = format(i,'08b')	
		str2 = ""
		x = ""
		
		for j in range(4):
			x = temp[2*j:2*j+2]
			#print(x)
			if x == '00':
				str2 += 'A'
			elif x == '01':
				str2 += 'C'
			elif x == '10':
				str2 += 'G'
			else :
				str2 += 'T'


			#print(temp)	
		#print(temp)
		#print(str2)
		pool.append(str2);
		
	len(pool)
	#pool has been created
	#now test for repetitivenesss

	pool1 = []
	for str2 in pool:
		myset = set()
		
		#print(str2)
		
		for i in range(16):
			ss = ""		#subsequence
			b = format(i,'04b')
			for j in range(4):
				if b[j] == '1':
					ss += str2[j]
				
			#print(ss)
			myset.add(ss)

		#print(len(myset))
		
		ratio = len(myset)/16	

		if ratio > 0.75:
			pool1.append(str2)
			#print(myset)
			#print(str2)
		#time.sleep(10)		
		
	#print(len(pool1))
		
	#The sequences with high repititiveness have been removed.
	#Now we will remove ones with undesirable GC content(<40 or >60)
	"""
	pool2 = []

	for str2 in pool1:
		countGC = str2.count('G') + str2.count('C')
		if countGC == 2:
			pool2.append(str2)
			print(str2)
		
	print(len(pool2))	
	"""
	pool2 = pool1				#REMOVE THIS IF GC CONTENT CONSTRAINT NEEDS TO BE INCLUDED

	no = 0

	while no != 8:
		
	#now we use edit distance constraint
		x = random.randint(0,len(pool2)-1)
		codewords = []
		codewords.append(pool2[x])

		str1 = codewords[0]


		pool3 = []
		temppool = pool2

		for i in range(len(pool2)):
			str1 = codewords[i]
			for str2 in temppool:
				dist = edit_distance.SequenceMatcher(a=str2,b=str1).distance()
				if  dist >= 3:
					pool3.append(str2)	
				"""
				else:
					print(dist)
					print(str2,str1)
				"""	
			#print('This is the length of pool 3:',len(pool3))
			if len(pool3) == 0:
				break
					
			x = random.randint(0,len(pool3)-1)
			codewords.append(pool3[x])
			temppool = pool3
			pool3 = []
				
		no = len(codewords)
	#	print(codewords)	
	return codewords
	
	