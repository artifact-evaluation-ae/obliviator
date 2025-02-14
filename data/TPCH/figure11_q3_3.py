import sys

# c_custkey @ o_order_date || o_shippriority || o_custkey || o_orderkey @ l_orderkey || l_extendedprice || l_discount
f = open("/dev/shm/q3_2_2_output.txt", "r")
output = open("/dev/shm/q3_3.txt", "w")
data = f.readlines()
f.close()
mx1 = 0
mx2 = 0
mx3 = 0
mx4 = 0
mx5 = 0
output.write(str(len(data))+"\n\n")

for i in range(len(data)):
    dd = data[i].split("@$")
    d0 = dd[0].split("|")
    #d0_date = d0[4].split('-')
    d1 = dd[1].split("|") # order key " " price " " discount " " order_date " " ship priority " " orderkey||orderdate||shippriority
    d2 = dd[2].split("|")
    #output.write(d1[3]+" "+d1[5]+" "+d1[6]+" "+str(d0_date[0])+str(d0_date[1])+str(d0_date[2])+" "+str(d0[7])+" "+d1[0]+str(d0_date[0])+str(d0_date[1])+str(d0_date[2])+str(d0[7])+"\n")
    if (d2[2][-1] == "\n"):
        d2[2] = d2[2][:-1]
    output.write(d1[3]+" "+d2[1]+" "+d2[2]+" "+d1[0]+" "+d1[1]+" "+d1[3]+d1[0]+d1[1]+"\n")   

output.close()