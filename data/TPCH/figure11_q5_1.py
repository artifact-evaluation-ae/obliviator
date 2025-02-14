import sys

# c = open("/dev/shm/tpch/dbgen/customer.tbl", "r")
o = open("/dev/shm/tpch/dbgen/orders.tbl", "r")
# l = open("/dev/shm/tpch/dbgen/lineitem.tbl", "r")
# s = open("/dev/shm/tpch/dbgen/supplier.tbl", "r")
# n = open("/dev/shm/tpch/dbgen/nation.tbl", "r")
# r = open("/dev/shm/tpch/dbgen/region.tbl", "r")

d_o = o.readlines()
o.close()
output_o = open("/dev/shm/q5_1_o.txt", "w")
output_o.write(str(len(d_o)) + "\n\n")
max1 = 0

for i in range(len(d_o)):
    d = d_o[i].split("|")
    date = d[4].split("-")
    output_o.write(date[0] + date[1] + date[2] + " " + d[1] + "|" + d[0] + "\n") # order_date " " order_custkey "|" order_key
    
    if max1 < len(d_o[i]):
        max1 = len(d_o[i])

print("o completed, max length: "+str(max1))
output_o.close


