#find if number is even or odd
#multiple of three or five
import os
os.system("cls")
Number=int(input('Enter a number: '))
if (Number%2==0):
    print ('This is an even number.')
else:
    print ('This is an odd number.')
if (Number%3==0):
    print ('This is a multiple of three.')
if (Number%5==0):
    print ('This is a multiple of five.')