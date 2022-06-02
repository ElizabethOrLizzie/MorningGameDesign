#Elizabeth Nassi
#Write a program to create a new string made of an input string’s first, middle, and last character.
import os
os.system("cls")
word=input('your word is ')
first=word[0]
y=len(word)
x=int(y/2)
middle=word[x]
last=word[len(word)-1]
print(first+middle+last)

#Write a program to create a new string made of the middle three characters of an input string
word2=input('your word is ')
y2=len(word2)
x2=y2//2 #//gets integer
middle1=word[x2-1:x2+2]
print(middle1)

#Given two strings,s1ands2. Write a program to create a new strings3by appendings2in the middle ofs1.
word3=input('your first word is ')
word4=input('your second word is ')
half1=len(word3)//2
print(word3[0:half1]+word4+word3[half1:len(word3)])

#Given two strings,s1ands2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
word5=input('your first word is ')
word6=input('your second word is ')
first5=word5[0]
first6=word6[0]
middle5=word5[len(word5)//2]
middle6=word6[len(word6)//2]
last5=word5[len(word5)-1]
last6=word6[len(word6)-1]
print(first5+first6+middle5+middle6+last5+last6)