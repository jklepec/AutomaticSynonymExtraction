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

j=0
for i in range (0,n) :
    niz = []
    while (edge[j][0] == i+1) :
        niz.append(lines[edge[j][1]-1])
        j+=1
        if(j>=broj_bridova) :
            break
    rjecnik[lines[i]] = niz

data = rjecnik

rijec = input()
Gn = {}

for x in data[rijec]:
  Gn[x] = 1
Gn[rijec] = 1

for x in data:
  if rijec in data[x]:
    Gn[x] = 1

rijeci = list(Gn.keys())

for i, x in enumerate(rijeci):
  Gn[x]=i

print(Gn.keys())

n = len(Gn.keys())

B = [None] * n

for x in Gn.keys():
  lista = [0] * n
  for y in data.get(x, []):
    index = Gn.get(y, -1)
    if index != -1:
      lista [index] = 1
    else:
      lista[index] = 0
  B[Gn[x]] = lista

A=[[0,1,0],[0,0,1],[0,0,0]]

B = np.matrix(B)
A = np.matrix(A)
X = np.matrix(np.zeros((n, 3)))
X = X + 1
print(X)

for i in range(1002):
  X = B * X * A.transpose() + B.transpose() * X * A
  X = X / np.linalg.norm (X)

print (X)

stupac2 = list((X[i, 1], rijeci[i]) for i in range(n))

stupac2.sort()
stupac2.reverse()
print(stupac2)

