import json
import numpy as np


f = open('sample.json')
data = json.load(f)
print(data['water'])

rijec = input()
Gn = {}

for x in data[rijec]:
  Gn[x] = 1
Gn[rijec] = 1

for x in data:
  if rijec in data[x]:
    Gn[x] = 1

Gn['pond'] = 1
rijeci = list(Gn.keys())

for i, x in enumerate(rijeci):
  Gn[x]=i


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
X = np.matrix(np.zeros((n, 3)))
X = X + 1

for i in range(4000):
  X = B * X * A.transpose() + B.transpose() * X * A
  X = X / np.linalg.norm (X)


stupac2 = list((X[i, 1], rijeci[i]) for i in range(n))

stupac2.sort()
stupac2.reverse()
for x in stupac2: print(x)
