#Definition of function for the number
def FUNCTION():
    print('Make a guess of a number between 1 and 100')
    numberNeeded = random.randint(1, 100)
    for i in range(10):
        print('You have ' + str(10 - i) +' guess(es)')
        myguess = int(input())
        if not myguess.isdecimal() or myguess < 0 or myguess > 100:
            print('Please type a digit from 1 to 100')
        elif myguess > numberNeeded:
            print('The number is less than ' + str(myguess) + '.')
        elif myguess < numberNeeded:
            print('The number is larger than ' + str(myguess) + '.')
        elif myguess == numberNeeded:
            print('Well done!!. You guessed the correct number after ' + str(i + 1) + ' guesses.')
            print('The number is actually ' + str(numberNeeded) + '.')
            break

        
#What is your name
print('Hello! What is your name?')
myName = input()
while not myName.isalpha():
    print('Are you sure that is reallyyour name?')
    print('What is your name?')


#Name of "AI"
print('Welcome ' + myName + '. My name is  Mufasa(version 2.0.06)')
print('I was created by the almighty LIONEL SEFA-BOAKYE YIADOM on 14th November, 2022')
print('Get ready for action')
print('')


#Asking about siblings
sibling_list = []
print('Do you have siblings?')
Sibability = input()


#siblingloop and yes or no
while not (Sibability.isalpha() and (Sibability.lower() == 'no' or Sibability.lower() == 'yes')):
    print('Do you have any siblings, YES or NO?')
    Sibability = input()    
if Sibability.upper() == 'YES':
    print('How many are they?')
    sib = input()
    while not sib.isdecimal():
        print('Please type a number.')
        sib = input()


#Number and names of siblings
    sib_number = int(sib)
    print('Input their names after the numbers.')
    for x in range(sib_number):
        sib_name = input(str(x+1) + '.    ')
        sibling_list += [sib_name]
    print('')
    print('')
    print('The names of your siblings are:')
    for x in range(sib_number):
        print(sibling_list[x])
else:
    print('Would you like to know the names of my siblings?.')
    my_way = input()
    if my_way == 'yes' or my_way == 'sure' or my_way == 'ok' or my_way == 'okay': 
        print('My siblings are Mufasa(version1.0.00) and Mufasa(version1.1.04)')
    elif my_way.isalnum() and not my_way.isalpha():
        print('You really love numbers don\'t you?.')
    else:
        print('My siblings are Mufasa(version1.0.00) and Mufasa(version1.1.04)')
print('')


#Compulsory guessing game
import random, sys
print('Would you like to play a guessing game?')
choice = input()
if choice.lower() == 'yes':
    FUNCTION()
else:
    print('You will certainly play this game')
    FUNCTION()


#Closing
print('')
while True:
    print('Type EXIT to exit')
    End_ing = input()
    if End_ing.lower() == 'exit':
        sys.exit
        break
    else:
        print(myName + ", you typed '" + End_ing + "'.")
        continue
        
