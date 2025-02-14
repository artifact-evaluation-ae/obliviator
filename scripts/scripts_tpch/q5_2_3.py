import sys

c = open("/dev/shm/q5_2_2_output.txt", "r") # nation key || o_order_key @  price "|" discount "|" suppkey
o = open("/dev/shm/tpch/dbgen/supplier.tbl", "r")

data = c.readlines()
c.close()
data2 = o.readlines()
o.close()
output = open("/dev/shm/q5_2_3.txt", "w")
output.write(str(len(data2))+ " "+str(len(data))+"\n\n")
max1 = 0
for i in range(len(data2)):
    d = data2[i].split("|")
    output.write(d[0] + " " + d[3] + "\n") # s_suppkey " " s_nation key


max1 = 0

output.write("\n")
for i in range(len(data)):
    d_ = data[i].split("@$")
    d1 = d_[1].split("|")
    d0 = d_[0].split("|")
    if (d1[2][-1] == '\n'):
        d1[2] = d1[2][:-1]
    output.write(d1[2] + " " + d0[0] + "@$" + d1[0] + "|" + d1[1] + "\n") # l_suppkey " " only c's nation key || l_extended_price || l_discount


output.close()