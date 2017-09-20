"""
Author : Omkar Damle and Rushikesh Nalla
ID : 201401114 and 201401106
Date : 18th April 2017

The function in this file is used to do error correction.
"""

import edit_distance

def correctErrors(newStr,dic):
	for i in range(0, len(newStr), 4):
		str1 = newStr[i:i+4]
		error = 1;
		for j in range(8):
			if str1 == dic[str(j)]:
				error = 0;
				break
		if error == 1:
			edit_dist = []
			for k in range(8):
				edit_dist.append(edit_distance.SequenceMatcher(a=str1,b=dic[str(k)]).distance())
			min_index = edit_dist.index(min(edit_dist))
			newStr = newStr[:i] + dic[str(min_index)] + newStr[i+4:]
	return newStr