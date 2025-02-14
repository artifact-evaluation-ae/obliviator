import sys

c = open("/dev/shm/tpch/dbgen/customer.tbl", "r")
o = open("/dev/shm/q5_1_o_output.txt", "r") # order_custkey "|" order_key

data = c.readlines()
c.close()
data2 = o.readlines()
o.close()
output = open("/dev/shm/q5_2_1.txt", "w")
output.write(str(len(data))+ " "+str(len(data2))+"\n\n")
max1 = 0
for i in range(len(data)):
    d = data[i].split("|")
    output.write(d[0] + " " + d[0] + "|" + d[3] + "\n") # custKey " " custKey | nation_key
    if max1 < len(data[i]):
        max1 = len(data[i])

print("c completed, max length: "+str(max1))
max1 = 0

output.write("\n")
for i in range(len(data2)):
    d = data2[i].split("|")
    if data2[i][-1] == '\n':
        output.write(d[0] + " " + data2[i]) # order_custkey " " order_custkey "|" order_key
    else:
        output.write(d[0] + " " + data2[i] + "\n")
    if max1 < len(data2[i]):
        max1 = len(data2[i])

print("o completed, max length: "+str(max1))
output.close()