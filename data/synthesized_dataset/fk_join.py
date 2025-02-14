import random
import os

power_list = [10]
data_max = 100

for i in power_list:
    name = "./test.txt"
    file = open(name, 'w')
    file.write("10 "+str(pow(2,i))+"\n")
    file.write("\n")
    for o in range(10):
        file.write(str(o+1)+" "+str(random.randint(1, data_max))+"\n")
    file.write("\n")
    for o in range(pow(2,i)):
        file.write(str(((o+1)% 10)+1)+" "+str(random.randint(1, data_max))+"\n")
    file.close
    print(name + " ", end = "")
