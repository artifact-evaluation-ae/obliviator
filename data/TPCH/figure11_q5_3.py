import sys

f = open("/dev/shm/q5_2_5_output.txt", "r")
# region key | region name @ nation key | nation name | nation table's region key @ customer's nation key @ l_extended_price | l_discount @ s_nation key
d = f.readlines()
f.close()
o = open("/dev/shm/q5_3.txt", "w")
o.write(str(len(d)) + "\n\n")
max1 = 0

for i in range(len(d)):
    d0 = d[i].split("@$")
    d00 = d0[0].split("|") # regain name " " c_nationkey " " s_nationkey " " n_name "@$" l_extendedprice "@$" l_discount
    d01 = d0[1].split("|")
    d02 = d0[2].split("|")
    d03 = d0[3].split("|")
    d04 = d0[4].split("|")
    if (d04[0][-1] == "\n"):
        o.write(d00[1] + " " + d02[0] + " " + d04[0][:-1] + " " + d01[1] + "@$" + d03[0] + "@$" +d03[1] + "\n")
    else:
        o.write(d00[1] + " " + d02[0] + " " + d04[0] + " " + d01[1] + "@$" + d03[0] + "@$" +d03[1] + "\n")
    if max1 < len(d00[1] + " " + d02[0] + " " + d04[0] + " " + d01[1] + "@$" + d03[0] + "@$" +d03[1] + "\n"):
        max1 = len(d00[1] + " " + d02[0] + " " + d04[0] + " " + d01[1] + "@$" + d03[0] + "@$" +d03[1] + "\n")

print("completed q5_3, max length is "+str(max1))
o.close()
