def collatz(x):                                        #definition of collatz is given here
    print('')
    print(x)
    while True:
        if x % 2 == 0 and x != 0:
            print(int(x / 2))
            x /= 2                                     #x /= 2  is the same as x = x / 2
            continue
        elif x % 2 == 1 and x != 1:
            print(int(3 * x + 1))
            x = 3 * x + 1 
            continue
        elif x == 1:
            break
        elif x == 0:
            print(1)
            break


print('Collatz sequence is a sequence of numbers that eventually leads to 1')
print('Input a number to see how this works.')
my_x = input()                                                                   #At this point, the user inputs a number into the computer
while not my_x.isdecimal():                                                                                         
    print('Please type an integer')                                         #Prompts the user to input an integer
    my_x = input()

my_number = int(my_x)
collatz(my_number)                                                                         
print('The sequence is worked by the following method:')
print('>>>>For even numbers you continue dividing by 2')
print('>>>>if you get an odd number or 0, they are multiplied by 3 and added to 1')
print('>>>>The process is continued till you eventually get to 1')

import sys
print('Hit the enter key to exit')
myself = input()
sys.exit
#mufasa 

