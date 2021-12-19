import json
import codecs

rjecnik = {}
with codecs.open('orginalni.json', 'rb') as f:
  rjecnik = json.load(f)


words = list(rjecnik.keys())
words.sort()

r = open('rijeci.txt', 'w', encoding = 'utf-8')  
f = open('input.txt', 'w', encoding = 'utf-8')

def trans(x):
  word = x
  '''
  for c in x:
    if c == 'ć':
      word += '1'
    elif c == 'č':
      word += '2'
    elif c == 'š':
      word += '3'
    elif c == 'đ':
      word += '4'
    elif c == 'ž':
      word += '5'
    elif c == 'ȍ':
      word += 'o'
    elif c not in '-→0:‘0' or c < 'a' or c > 'z':
      word += c
'''
  if len(word) == 0: word += 'a'
  return word.replace(" ", "")

f.write(f'{len(words)}\n')
for x in words:
  f.write(f'{len(rjecnik[x])} {trans(x)}\n')
  for y in rjecnik[x]:
    f.write(trans(y.lower()) + ' ')
  f.write('\n')
  r.write(x + '\n')
  if x == "badava": print(rjecnik[x])

f.close()
r.close()
