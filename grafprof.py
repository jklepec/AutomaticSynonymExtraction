import numpy as np

# učitavam riječi i spremam u vektor lines
lines = []
#kako da se ovo ne pokrece svaki put? I kako se komentira više redova u pythonu?
with open('index.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    lines[count] = line.strip()
    count += 1

# ucitavam podatke o bridovima
edge = np.loadtxt("dico.txt", dtype='i')

#mislim da je tu nes krivo mozda, zasto puno rijeci pokazuje na 4??
#radim graf od podataka, spremljen kao rjecnik
rjecnik = {}
n = len(lines)
broj_bridova = len(edge)
frek = [0] * n

for i in range (broj_bridova):
    frek[edge[i][1]-1] += 1

j=0
for i in range (0,n) :
    if 
    niz = []
    while (edge[j][0] == i+1) :
        if frek[edge[j][1]-1]<=1000 :
            niz.append(lines[edge[j][1]-1])
        j+=1
        if(j>=broj_bridova) :
            break
    if (frek[i] > 1000)  :
        continue   
    rjecnik[lines[i]] = niz
    
import json
with open("sample.json", "w+") as outfile:
    json.dump(rjecnik, outfile)

print("gotovo")


