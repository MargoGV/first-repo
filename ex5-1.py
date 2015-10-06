from random import *
output = open('output.txt', 'w')
for i in range(1000000):
    print(randint(0, 100), file = output)
output.close()
