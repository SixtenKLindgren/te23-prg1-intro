import random

numbers = []
while len(numbers) < 10 :
    numbers.append(random.randint(0,10000))
for i in numbers :
    splitlist = list(str(i))
    joinedstr = splitlist.sort()
    numbers.append(joinedstr)
print(numbers)
    