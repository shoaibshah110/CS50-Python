import random

#coin = random.choice(["heads", "tails"])
#print(coin)

# Just import certain module you want rather than all modules, you can just specify choice
#from random import choice

#coin = choice(["heads", "tails"])
#print(coin)


#number = random.randint(1,10)
#print(number)

names = ["shoaib", "mohib", "aki"]

random.shuffle(names)

for name in names:
    print(name)

