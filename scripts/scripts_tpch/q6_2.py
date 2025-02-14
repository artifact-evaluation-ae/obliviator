import sys

f = open("/dev/shm/q6_1_output.txt", "r")
d = f.readlines()
f.close()
output = open("/dev/shm/q6_2.txt", "w")
output.write(str(len(d))+"\n\n")

for i in range(len(d)):
    d0 = d[i].split(" ") # price, discount, shipdate, quantity
    #d1 = d0[10].split("-")
    if (d0[1][-1] == '\n'):
        output.write(d0[0]+" "+d0[1])
    else:
        output.write(d0[0]+" "+d0[1]+"\n")
output.close()
