#great things start from scratch
import random
Num = random.randint(1, 20)
print('Guess a number. You have ten guesses')

for gUesse in range(1, 11):
    print('The number is from 0 to 100')
    Choice = int(input())
    if Choice > Num:
        print('Your guess is big. Make another guess')
    elif Choice < Num:
        print('Your guess is small. Make another guess')
    else:
        break

if Choice == Num:
    print('Well done, you guessed the number in ' + str(gUesse) + ' guesses.')
else:
    print('You have run out guesses. The number is ' + str(Num))
    
import sys
while True:
    print('type EXIT to exit')
    myChoice = input()
    if myChoice == 'exit':
        break
    else:
        print('You typed ' + myChoice + '.')
        #Let's hope this works.
    sys.exit
