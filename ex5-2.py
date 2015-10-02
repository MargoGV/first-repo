from random import *
output1 = open('output1.txt', 'w')
for i in range(1000000):
    print(randint(0, 10000)/100, file = output1)
output.close()
