
import requests
from Rjecnik import Rjecnik

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

slova = ['a', 'b', 'c', 'č', 'ć', 'd', 'đ', 'dž', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l', 'lj', 'm', 'n', 'nj',
         'o', 'p', 'r', 's', 'š', 't', 'u', 'v', 'z', 'ž']

rjecnik = Rjecnik()

for slovo in slova:
  ok = 1
  for i in range(120):
    url = f'http://rjecnik.hr/?letter={slovo}&page={i}'
    html_content = requests.get(url, headers=headers).text
    ok *= rjecnik.dodaj(html_content)
    print('.', end = '')
  assert ok == 0
  print(slovo)

rjecnik.spremi()

    
