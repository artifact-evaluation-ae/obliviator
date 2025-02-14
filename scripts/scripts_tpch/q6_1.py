import sys

f = open("/dev/shm/tpch/dbgen/lineitem.tbl", "r")
d = f.readlines()
f.close()
output = open("/dev/shm/q6_1.txt", "w")
output.write(str(len(d))+"\n\n")

for i in range(len(d)):
    d0 = d[i].split("|") # price, discount, shipdate, quantity
    d1 = d0[10].split("-")
    output.write(d0[5]+" "+d0[6]+" "+d1[0]+d1[1]+d1[2]+" "+d0[4]+"\n")
output.close()
