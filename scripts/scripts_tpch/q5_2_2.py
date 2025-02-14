import sys

c = open("/dev/shm/q5_2_1_output.txt", "r") # customer || order, new: custKey | nation_key @ order_custkey "|" order_key
o = open("/dev/shm/tpch/dbgen/lineitem.tbl", "r")

data = c.readlines()
c.close()
data2 = o.readlines()
o.close()
output = open("/dev/shm/q5_2_2.txt", "w")
output.write(str(len(data))+ " "+str(len(data2))+"\n\n")
max1 = 0
for i in range(len(data)):
    d_ = data[i].split("@$")
    d1 = d_[1].split("|")
    d0 = d_[0].split("|")
    #output.write(d[0] + " " + d0[3] + "@$" + d[0] + "\n") # order_key " " only c's nation key || o_order_key
    if (d1[1][-1] == '\n'):
        d1[1] = d1[1][:-1]
    output.write(d1[1] + " " + d0[1] + "|" + d1[1] + "\n")

max1 = 0

output.write("\n")
for i in range(len(data2)):
    d = data2[i].split("|") # orderkey " " price "|" discount "|" suppkey
    #if data2[i][-1] == '\n':
    #    output.write(d[0] + " " + data2[i])
    #else:
    output.write(d[0] + " " + d[5] + "|" + d[6] + "|" + d[2] + "\n")
    if max1 < len(data2[i]):
        max1 = len(data2[i])

print("o completed, max length: "+str(max1))
output.close()