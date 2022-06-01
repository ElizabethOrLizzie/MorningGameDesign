#Elizabeth Nassi
#Calculate Age
#get user year and current year
import os
os.system('cls')
by=2001 #assign this value as a number
#by=input('Your birth year is ') give us a string
by = int( input('Your birth year is ') ) #typecast
Currentyear=2022 #alsa number
age =Currentyear-by
print('Your age is' ,age,)
#Selection
if age >50:
    print('You are old.')