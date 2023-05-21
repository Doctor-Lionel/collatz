Cat = []
print('How many cats do you have?')
myCats = input()
while True:
    print('What is the name of cat ' + str(len(Cat) + 1))
    catName = input()
    if catName == '':
        break
    Cat = Cat + [catName]

print('The names of your cats are:')     
for c in Cat:
    print(' ', c) 
