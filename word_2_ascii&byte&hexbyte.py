#Please run this script with python3
#This script convert word/character  to ascii byte (0-127)
print("\nThis script convert text to ASCII")
wor = print('\nenter the word to convert to ascii: ')
word = str(input()) 
print('The ascii_byte  representation of: ' + str(word)  + '   is' )
print("\n")
for i in word:
	ascii_rep = ord(i)
	print(str(ascii_rep)," " , end="")
print("\n")
print("The  byte representation is: ")
print("\n")
for i in word:
	hex_byte = bytes(word,"utf-16")
	print(str(hex_byte), " ", end="")
print("\n")
print("The hex_byte representation is: ", "\n")
word = str(word)
for i in word:
	s = i.encode('utf-8')
	c = s.hex()
	print("0x",end="")
	print( c ,"  ", end="" )
print("\n") 


