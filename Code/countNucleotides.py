"""
Author : Omkar Damle and Rushikesh Nalla
ID : 201401114 and 201401106
Date : 18th April 2017

The function in this file is used to count nucleotides.
"""

with open(input("give name of input file"),"r") as file:
	countA = 0
	countC = 0
	countG = 0
	countT = 0
	
	while(True):
		char = file.read(1)
		if char == 'A':
			countA+=1
		elif char == 'C': 
			countC+=1
		elif char == 'G':
			countG+=1
		elif char == 'T':
			countT+=1	
		else:
			break
		
total = countA+countC+countG+countT

perA = countA*100/total
print("Percentage of A "+ str(perA))			

perC = countC*100/total
print("Percentage of C "+ str(perC))			

perG = countG*100/total
print("Percentage of G "+ str(perG))			

perT = countT*100/total
print("Percentage of T "+ str(perT))			