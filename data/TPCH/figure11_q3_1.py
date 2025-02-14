import sys

# c_custkey
f_c = open("/dev/shm/q3_c_output.txt", "r")
# o_order_date || o_shippriority || o_custkey || o_orderkey
f_o = open("/dev/shm/q3_o_output.txt", "r")
# f_l = open("/dev/shm/q3_l_output.txt", "r")
max1 = 0
max2 = 0
# max3 = 0
mx1 = 0
mx2 = 0
# mx3 = 0

output_c = open("/dev/shm/q3_2_1.txt", "w")
data = f_c.readlines()
data2 = f_o.readlines()
f_o.close()
f_c.close()
output_c.write(str(len(data)) + " " + str(len(data2)) + "\n")
output_c.write("\n")
for i in range(len(data)):
    d = data[i].split('|')
    if (d[0][-1] != '\n'):
        output_c.write(d[0] + " " + d[0] + "\n")
    else:
        output_c.write(d[0][:-1] + " " + d[0])
    if (max1 < len(d[0])):
        max1 = len(d[0])
    else:
        max1 = len(d[0])
    if (mx1 < len(d[0])):
        mx1 = len(d[0])
    else:
        mx1 = len(d[0])

output_c.write("\n")
print("c completed, key " + str(mx1) + " data "+str(max1))

for i in range(len(data2)):
    d = data2[i].split('|')
    if (data2[i][-1] != '\n'):
        output_c.write(d[2] + " " + data2[i] + "\n")
    else:
        output_c.write(d[2] + " " + data2[i])
    if (max2 < len(data2[i])):
        max2 = len(data2[i])
    else:
        max2 = len(data2[i])
    if (mx2 < len(d[2])):
        mx2 = len(d[2])
    else:
        mx2 = len(d[2])

print("o completed, key " + str(mx2) + " data "+str(max2))
output_c.close()

"""
output_l = open("/dev/shm/q3_2_l.txt", "w")
data = f_l.readlines()
f_l.close()
output_l.write(str(len(data)) + "\n")
output_l.write("\n")
for i in range(len(data)):
    d = data[i].split('|')
    if (data[i][-1] != '\n'):
        output_l.write(d[0] + " " + data[i] + "\n")
    else:
        output_l.write(d[0] + " " + data[i])
    if (max3 < len(data[i])):
        max3 = len(data[i])
    else:
        max3 = len(data[i])
    if (mx3 < len(d[0])):
        mx3 = len(d[0])
    else:
        mx3 = len(d[0])
print("l completed, key " + str(mx3) + " data "+str(max3))
output_l.close()
"""