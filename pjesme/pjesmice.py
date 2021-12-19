import csv

def nadi_rijeci(text):
    po_cemu_splitaj = ""
    for c in text:
        if not (c in "šđžčć" or (c >= 'a' and c <= 'z')):
            if c not in po_cemu_splitaj:
                po_cemu_splitaj += c

    nadene_rijeci = [text]
    for znak in po_cemu_splitaj:
        nove_rijeci = []
        for rijec in nadene_rijeci:
            tmp = rijec.split(znak)
            nove_rijeci = nove_rijeci + tmp
        nadene_rijeci = nove_rijeci
    return [x for x in nadene_rijeci if len(x)>=2]

rjecnik = {}
with open('lyrics.csv','r', encoding='utf-8')as file:
   print("tu sam")
   filecontent=csv.reader(file)
   print("csv")
   for row in filecontent:
        ntorka = (row[2], row[3])
        rjecnik [ntorka] = nadi_rijeci(row[4])


print("ucitao")

pjesma = (input("ime izvodaca: "), input("ime pjesme: "))
Gn = {}

for y in rjecnik.keys():
    words = y[1].split()
    n=len(words)
    brojac=0

    for i in (n) :
        for x in rjecnik[pjesma]:
            if (words[i]==x) :
                brojac+=1
                break
            
    if (brojac >= n/2) :
        Gn[y] = 1

print("gotovo")
        
Gn[pjesma] = 1

np = pjesma[1].split()
dulj=len(np)
lista = [0] *dulj


for x in rjecnik:
    for rijec in data[x]:
        for i in (dulj) :
            if (np[i]==rijec) :
                lista [i]=1

    if (sum(lista) >= dulj):        
          Gn[x] = 1











