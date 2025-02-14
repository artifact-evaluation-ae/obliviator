import sys

f_c = open("/dev/shm/tpch/dbgen/customer.tbl", "r")
f_o = open("/dev/shm/tpch/dbgen/orders.tbl", "r")
f_l = open("/dev/shm/tpch/dbgen/lineitem.tbl", "r")

d_c = f_c.readlines()
d_o = f_o.readlines()
d_l = f_l.readlines()

f_c.close()
f_o.close()
f_l.close()

max1 = 0
max2 = 0
max3 = 0
mx1 = 0

output_c = open("/dev/shm/q3_c.txt", "w")
output_c.write(str(len(d_c))+"\n")
output_c.write('\n')

output_o = open("/dev/shm/q3_o.txt", "w")
output_o.write(str(len(d_o))+"\n")
output_o.write('\n')

output_l = open("/dev/shm/q3_l.txt", "w")
output_l.write(str(len(d_l))+"\n")
output_l.write('\n')

for i in range(len(d_c)):
    d = d_c[i].split('|')
    output_c.write(d[6]+" "+d[0]+"\n")
    
    if max1 < (len(d[0])):
        max1 = (len(d[0]))
    if mx1 < len(d[6]):
        mx1 = len(d[6])

print("Processing for customer.tbl completed, pay attention the max length is: " + str(mx1) + " and " + str(max1))
output_c.close()

for i in range(len(d_o)):
    d = d_o[i].split('|')
    dd = d[4].split('-')
    output_o.write(dd[0]+dd[1]+dd[2]+" "+dd[0]+dd[1]+dd[2]+"|"+d[7]+"|"+d[1]+"|"+d[0]+"\n") # order_date " " o_order_date || o_shippriority || o_custkey || o_orderkey
    
    if max2 < (len(dd[0]+dd[1]+dd[2]+" "+dd[0]+dd[1]+dd[2]+"|"+d[7]+"|"+d[1]+"|"+d[0]+"\n")):
        max2 = (len(dd[0]+dd[1]+dd[2]+" "+dd[0]+dd[1]+dd[2]+"|"+d[7]+"|"+d[1]+"|"+d[0]+"\n"))

print("Processing for order.tbl completed, pay attention the max length is: " + str(max2))
output_o.close()

for i in range(len(d_l)):
    d = d_l[i].split('|')
    dd = d[10].split('-')
    output_l.write(dd[0]+dd[1]+dd[2]+" "+d[0]+"|"+d[5]+"|"+d[6]+"\n") # ship_date " " l_orderkey || l_extendedprice || l_discount
    
    if max3 < (len(dd[0]+dd[1]+dd[2]+" "+d[0]+"|"+d[5]+"|"+d[6]+"\n")):
        max3 = (len(dd[0]+dd[1]+dd[2]+" "+d[0]+"|"+d[5]+"|"+d[6]+"\n"))

print("Processing for lineitem.tbl completed, pay attention the max length is: " + str(max3))

output_l.close()