import sys

c = open("/dev/shm/q5_2_3_output.txt", "r") # s_nation key || Customer's nation key || l_extended_price || l_discount 
o = open("/dev/shm/tpch/dbgen/nation.tbl", "r") # nation's whole thing

data = c.readlines()
c.close()
data2 = o.readlines()
o.close()
output = open("/dev/shm/q5_2_4.txt", "w")
output.write(str(len(data2))+ " "+str(len(data))+"\n\n")
max1 = 0
for i in range(len(data2)):
    d = data2[i].split("|")
    output.write(d[0] + " " + d[0] + "|" + d[1] + "|" + d[2] + "\n") # nation key " " nation key || name ||region key 
    if max1 < len(d[0] + "|" + d[1] + "|" + d[2]):
        max1 = len(d[0] + "|" + d[1] + "|" + d[2])

print("o completed, max length: "+str(max1))
max1 = 0

output.write("\n")
for i in range(len(data)):
    d_ = data[i].split("@$")
    d = d_[0].split("|")
    # d0 = d_[2].split("|")
    if (d_[2][-1] == '\n'):
        output.write(d[0] + " " + d_[1] + "@$" + d_[2][:-1] + "@$" + d[0]+'\n') # s_nation key " " only c's nation key || l_extended_price || l_discount || s_nation key
    else:
        output.write(d[0] + " " + d_[1] + "@$" + d_[2] + "@$" + d[0]+'\n') # s_nation key " " only c's nation key || l_extended_price || l_discount || s_nation key
    if max1 < len(d[0] + " " + d_[1] + "@$" + d_[2]):
        max1 = len(d[0] + " " + d_[1] + "@$" + d_[2])

print("c completed, max length: "+str(max1))
output.close()