import sys

f = open("/dev/shm/q5_3_output.txt", "r")
# nation name @ l_extended_price @ l_discount
d = f.readlines()
f.close()
o = open("/dev/shm/q5_4.txt", "w")
o.write(str(len(d)) + "\n\n")
max1 = 0

for i in range(len(d)):
    d0 = d[i].split("@$")
    if (d0[2][-1] == "\n"):
        o.write(str(hash(d0[0]))[1:5] + " " + d0[1] + " " + d0[2])
    else:
        o.write(str(hash(d0[0]))[1:5] + " " + d0[1] + " " + d0[2] + "\n")
    if max1 < 4 + len(" " + d0[1] + " " + d0[2]):
        max1 = 4 + len(" " + d0[1] + " " + d0[2])

print("completed q5_4, max length is "+str(max1))
o.close()
