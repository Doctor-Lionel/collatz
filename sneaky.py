import re

SneakyMe =('''
''')





# Regular expression pattern to match phone numbers
phone_regex = r'\w+'

# Find all occurrences of phone numbers in the string
phone_numbers = re.findall(phone_regex, SneakyMe)

# Count the number of times each phone number occurred
phone_count = {}
for number in phone_numbers:
    if number in phone_count:
        phone_count[number] += 1
    else:
        phone_count[number] = 1

# Print the phone numbers and their counts
        print(number, count)




escape = 'Nothing'
while escape != '':
    print('press ENTER to exit')
    escape = input()
    escape = ''
