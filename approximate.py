def approximate(x):
    x = int(x * 10)
    if x% 10 == 5 or x % 10 == 6 or x % 10 == 7 or x % 10 == 8 or x % 10 == 9:
        return((x//10)+1)
    else:
        return(x // 10)


print('input a number\nlet me approximate it to the nearest ones digit')
my_number = float(input())
print('The answer is ' + str(approximate(my_number)))
        
xxe = input()
