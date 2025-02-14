
f3 = open("title.basics.tsv", "r")
f4 = open("imdb_title.txt", "w")
d = f3.readlines()
for i in range(1, len(d)):
    lst = d[i].split('\t')
    if (lst[5][0] != '1') and (lst[5][0] != '2'):
        continue
    year = int(lst[5])
    #movie_id[int(lst[0][2:])] = True
    f4.write(str(int(lst[0][2:]))+" "+str(year)+"\n")
f3.close()
f4.close()


f1 = open("name.basics.tsv", "r")
f2 = open("imdb_name.txt", "w")
d = f1.readlines()
for i in range(1, len(d)):
    #print(str(i))
    lst = d[i].split('\t')
    if (lst[-1][0] != 't'):
        continue
    lst2 = lst[-1].split(',')
    lst2[-1] = lst2[-1][:-1]
    for o in range(len(lst2)):
        #if (int(lst2[o][2:]) < len(movie_id)):
            #if (movie_id[int(lst2[o][2:])]):
                f2.write(str(int(lst2[o][2:]))+" "+str(int(lst[0][2:]))+"\n")
f1.close()
f2.close()

