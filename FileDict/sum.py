import re

file = open('regex_sum_2159774.txt')

sum = 0

for line in file:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)
print (sum)