from bs4 import BeautifulSoup
from unidecode import unidecode
import json


class Rjecnik:
  rjecnik = dict(encoding = 'utf-8')
  
  def nadi_rijeci(self, text):
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
    return nadene_rijeci

  def uljepsaj(self):
    return
  
  # dodaje html stranicu u rjecnik
  def dodaj(self, html):
    soup = BeautifulSoup(html, "lxml")
    table = soup.find('tbody')
    rows = table.find_all('tr')

    dodano = 0
    for word_span in rows:
      word_container = word_span.find_all("span", class_ = "word")

      dobra_slova = "čćđžš"
      word = ""
      for c in word_container[0].text.lower():
        if c in dobra_slova:
          word += c
        elif unidecode(c) >= 'a' and unidecode(c) <= 'z':
          word += unidecode(c)
          
      contents1 = word_span.find_all("span", class_ = "Normala")
      contents2 = word_span.find_all("a", class_ = "word-link")
      contents3 = word_span.find_all("span", class_ = "Podnatuknica")

      words = []
      for content in contents1 + contents2 + contents3:
        words += self.nadi_rijeci(content.text)

      words = [x for x in words if x != '']
      dodano += len(words)
      
      self.rjecnik[word] = self.rjecnik.get(word, []) + words

    return dodano

  def spremi(self):
    with open('orginalni.json', 'w+', encoding = 'utf-8') as f:
      json.dump(self.rjecnik, f, ensure_ascii = False)
