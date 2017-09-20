"""
Author : Omkar Damle and Rushikesh Nalla
ID : 201401114 and 201401106
Date : 18th April 2017

This is an implementation of ideas discussed in paper : A highly parallel strategy for storage of digital information in living cells
The following files will be produced for some input file named: name1.txt(same applies for png and jpg files):
1. name1.xz - lzma compressed original file
2. name1_comp.xz - lzma compressed recovered file
3. name1_decoded.txt - FINAL recovered file
4. name1.txt - sequence of DNA nucleotides 
"""

import lzma
import math
import time
import edit_distance
import random
import base64

import make_dictionary
import correctError

full_name = input("Enter name of input file: ")
#print(input_file_name)
#input("waiting");

is_png = False
is_jpg = False
is_txt = False

if "png" in full_name:
	is_png = True
elif "jpg" in full_name:
	is_jpg = True
elif "txt" in full_name:
	is_txt = True

	
input_file_name = full_name.split(".")[0]

	
#handle the image files here
	
if is_png or is_jpg:
	print("We have an image file as imput")
	with open(full_name, "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
		#print(encoded_string)
	bytes1 = encoded_string
	with lzma.open(input_file_name + ".xz","w") as file:
		file.write(bytes1)

elif is_txt:
#compression
	print("We have a text file as imput")
	with open(full_name,"r+") as f1:
		String1 = f1.read()

	bytes_str = String1.encode('utf-8')
	#data = b"abc"
	with lzma.open(input_file_name + ".xz","w") as file:
		file.write(bytes_str)

			
#with lzma.open("file.xz") as f:
#    file_content = f.read();


"""
Read compressed data
"""
#print(file_content)
with open(input_file_name + ".xz","rb") as f:
    file_content = f.read()

#print(file_content)

# converting from byte stream to octal
x = file_content.hex();
#print("This is hexadecimal :::::::: ",x)
dec = int(x,16);
y = oct(dec);
#print("This is octal :::::::::" , y)


#print(type(y))

codewords = make_dictionary.codeBookGen()

	
#dic = {"1":"ATTC","2":"ACTA","3":"ATTA","4":"TATA","5":"AATC","6":"ACAA","7":"TTTC","0":"TCTA",}
dic = {
	"0":codewords[0],	
	"1":codewords[1],
	"2":codewords[2],
	"3":codewords[3],
	"4":codewords[4],
	"5":codewords[5],
	"6":codewords[6],
	"7":codewords[7],
	}

print('Printing Dictionary...................')
print(dic)
	
#Dictionary has been created successfully!!!!!!!!!!!!!!!!!!

#niter = math.floor(len(y)/3)
niter = len(y)
newStr = ""

for i in range(2,niter):
	newStr += dic[y[i]];

#print('\n')
#print(newStr)

print("Storing DNA sequence as txt file")
with open(input_file_name + "_DNA.txt","w+") as fstore:
	fstore.write(newStr)

print("Reading DNA sequence from txt file")

with open(input_file_name + "_DNA.txt","r+") as fstore1:
	newStr = fstore1.read()

	

print("introducing some errors")	
# introducing errors
#string = "A"
#newStr = newStr[:2] + string + newStr[3:]
#newStr = newStr.replace('A','T')
dna = 'ACGT'
r = random.randint(0,3)
s = dna[r]
newStr = ''.join("s" if i % 4 == 0 else char for i, char in enumerate(newStr,r+1))

#print('\n')
#print(newStr)

# error correction
#compare = '01234567'

print("Doing error correction")

newStr = correctError.correctErrors(newStr,dic)

#print('\n')
#print(newStr)

print("Error correction done")

# converting DNA sequence to octal
octalString = ""
for i in range(0,len(newStr),4):
	temp = newStr[i:i+4]
	for key,value in dic.items():
		if value == temp:
			octalString = octalString + key

#print(octalString)			

# converting from octal to byte stream
dec1 = str(int(octalString,8));
dec2 = int(dec1);
m = hex(dec2);
#print(m)
m = m[2:]
z = bytes.fromhex(m);
#print(z);

#decompression
with open(input_file_name + "_comp.xz","wb") as f1:
    f1.write(z);
	
with lzma.open(input_file_name + "_comp.xz","rb") as f2:
    file_content = f2.read()

if is_png or is_jpg:	
	result = base64.b64decode(file_content)
	
	if is_png:
		with open(input_file_name + "_decoded.png","wb") as f2:
			f2.write(bytes(result))
	elif is_jpg:
		with open(input_file_name + "_decoded.jpg","wb") as f2:
			f2.write(bytes(result))
			
elif is_txt:
	result = file_content.decode('utf-8')
	with open(input_file_name + "_decoded.txt","w+") as f2:
		f2.write(result)

print("Decoded file created")		
		
#print(result)
#data_in = b"abc"
#data_out = lzma.compress(data_in)
#print(data_out)