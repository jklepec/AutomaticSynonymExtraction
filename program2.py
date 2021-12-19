import json
import numpy as np


f = open('sample.json')
data = json.load(f)

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

Gn['pond'] = 1

n = len(Gn.keys())

B = [None] * n

for x in Gn.keys():
  lista = [0] * n
  for y in data.get(x, []):
    index = Gn.get(y, -1)
    if index != -1:
      lista [index] = 1 #/ len(data[x])
    else:
      lista[index] = 0
  B[Gn[x]] = lista

A=[[0,1,0],[0,0,1],[0,0,0]]

B = np.matrix(B)
A = np.matrix(A)
X = np.matrix(np.zeros((n, 1)))
X = X + 1

kaca = B.transpose() * B + B * B.transpose()

for i in range(4000):
  X = kaca * X
  X /= X.sum()


stupac2 = list((X[i, 0], rijeci[i]) for i in range(n))

stupac2.sort()
stupac2.reverse()
print(list(stupac2[i][1] for i in range(n)))
