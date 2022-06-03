#ELizabeth Nassi
#learn abt functions, lists, loops
import random
import os
os.system('cls')
thislist = ["apple","banana", "cherry", "kiwi"]
print(thislist[-1]) #- makes go from end
print(thislist[2:3]) #: for range
print(thislist[:3]) #prints up to the number, but not the number
print(thislist[2:]) #Prints 2 and above, includes 2
print(thislist[-3:-1]) #range of negative, does not include kiwi
print(thislist[-3:]) #to include kiwi

if "apple" is in thislist:
    print("yes apple is in the list")

for num in range(10):
    print(num, end='')
    print()

for element in thislist: #element =thislist (times run through loop)
    print(element)
    print()

thislist = thislist.append("pineapple") #will change list permenantly
print(thislist[0:])

thislist.insert(0, "papaya") #adding an element to a specific index insert (index, element you want to add)
print(thislist [0:])

for i in range(len (thislist)):
    print(thislist[i], end = "/")
    print()

list_num = [1,2,3,4]
list_num.extend(thislist)
#append add list, extend add elements

word = random.choice(thislist)
print(word)

guess=input
if guess in word:
    print("congrats you guessed the word")