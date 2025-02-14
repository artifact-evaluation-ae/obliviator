import sys

f1 = open("supplier.tbl", "r")
f2 = open("customer.tbl", "r")

f3 = open("test"+sys.argv[1]+"_1.txt", "w")
data1 =  f1.readlines()
data2 = f2.readlines()
f3.write(str(len(data1))+" "+str(len(data2))+"\n")
f3.write('\n')

max1 = 0
max2 = 0
max3 = 0
min3 = 0
my_list = set()

for i in range(len(data1)):
    lst = data1[i].split("|")
    
    f3.write(lst[3]+" "+"DATA"+"\n")
    if i == 0:
        min3 = float(lst[5])
    
    if max1 < len(lst[2]):
        max1 = len(lst[2])
    if max2 < len(lst[-2]):
        max2 = len(lst[-2])
    if max3 < float(lst[5]):
        max3 = float(lst[5])
    if float(lst[5]) < min3:
        min3 = float(lst[5])
f3.write('\r\n')

for i in range(len(data2)):
    lst = data2[i].split("|")
    f3.write(lst[3]+" "+"DATA"+"\n")
    if max1 < len(lst[2]):
        max1 = len(lst[2])
    if max2 < len(lst[-2]):
        max2 = len(lst[-2])
    if max3 < float(lst[5]):
        max3 = float(lst[5])
    if float(lst[5]) < min3:
        min3 = float(lst[5])
    if not (lst[6] in my_list):
        my_list = my_list | {lst[6]}
f1.close()
f2.close()
f3.close()

print("max1: "+str(max1))
print("max2: "+str(max2))
print("max3: "+str(max3))
print("min3: "+str(min3))
print("type: "+str(my_list))