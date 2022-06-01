#Elizabeth Nassi
#Calculate BMI
#get user weight and height
import os
os.system('cls')
weight=40 #assign this value as a number
#weight = input('Your weight in kg is...? ') give us a string
weight = int( input('Your weight in kg is...? ')) #typecast
height=165 #assign this value as a number
#height = input('Your height in cm is...? ') give us a string
height = int( input('Your height in cm is...? ')) #typecast
ht = height/100
Squareht =ht*ht
BMI =weight/Squareht
print('Your BMI is ' ,BMI)