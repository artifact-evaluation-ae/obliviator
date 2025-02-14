import sys

f1 = open("/home/twitter_1n2_1.txt", "r")
f2 = open("/home/twitter_1_2.txt", "r")

data1 =  f1.readlines()
data2 = f2.readlines()
f1.close()
f2.close()

f3 = open("twitter_1.txt", "w")
f3.write(str(len(data1))+" "+str(len(data2))+"\n")
f3.write('\n')

for i in range(len(data1)):
    f3.write(data1[i])
    f3.write('\r\n')

for i in range(len(data2)):
    f3.write(data2[i])

f3.close()




f1 = open("/home/file1n2_1.txt", "r")
f2 = open("/home/file2_2.txt", "r")

data1 =  f1.readlines()
data2 = f2.readlines()
f1.close()
f2.close()

f3 = open("twitter_2.txt", "w")
f3.write(str(len(data1))+" "+str(len(data2))+"\n")
f3.write('\n')

for i in range(len(data1)):
    f3.write(data1[i])
    f3.write('\r\n')

for i in range(len(data2)):
    f3.write(data2[i])

f3.close()



f1 = open("/home/file3_1.txt", "r")
f2 = open("/home/file3_2.txt", "r")

data1 =  f1.readlines()
data2 = f2.readlines()
f1.close()
f2.close()

f3 = open("twitter_3.txt", "w")
f3.write(str(len(data1))+" "+str(len(data2))+"\n")
f3.write('\n')

for i in range(len(data1)):
    f3.write(data1[i])
    f3.write('\r\n')

for i in range(len(data2)):
    f3.write(data2[i])

f3.close()
