import sys

c = open("/dev/shm/q5_2_4_output.txt", "r") # nation key || nation name || n's region key || customer's nation key || l_extended_price || l_discount || s_nation key
o = open("/dev/shm/tpch/dbgen/region.tbl", "r") # nation's whole thing

data = c.readlines()
c.close()
data2 = o.readlines()
o.close()
output = open("/dev/shm/q5_2_5.txt", "w")
output.write(str(len(data2))+ " "+str(len(data))+"\n\n")
max1 = 0
for i in range(len(data2)):
    d = data2[i].split("|")
    output.write(d[0] + " " + d[0] + "|" + d[1] + "\n") # region key " "  region key ||region name 
    if max1 < len(d[0] + "|" + d[1]):
        max1 = len(d[0] + "|" + d[1])
print("o completed, max length: "+str(max1))
max1 = 0

output.write("\n")
for i in range(len(data)):
    d_ = data[i].split("@$")
    d = d_[0].split("|")
    d0 = d_[0].split("|")
    if (data[i][-1] == '\n'):
        output.write(d[2] + " " + data[i]) # n_region key " " nation key || nation name || n's region key || customer's nation key || l_extended_price || l_discount || s_nation key
    else:
        output.write(d[2] + " " + data[i] + "\n") 
    if max1 < len(data[i]):
        max1 = len(data[i])

print("c completed, max length: "+str(max1))


output.close()