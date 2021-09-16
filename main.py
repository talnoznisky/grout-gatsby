import itertools
import json
import re
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from bs4 import BeautifulSoup

punkt_param = PunktParameters()
punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc'])
sentence_splitter = PunktSentenceTokenizer(punkt_param)

with open('greatgatsby.html', 'r') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

reg = re.compile('chapter-*')
text = soup.find_all('p')
paragraphs = [sentence_splitter.tokenize(l.text.replace('?"', '? "').replace('!"', '! "').replace('."', '. "')) for l in text]
sentences = list(itertools.chain(*paragraphs))

sentences = [text.replace('? "', '?"').replace('! "', '!"').replace('. "', '."') for text in sentences]

alpha_tokens = sorted(sentences, key=lambda s: s if s[0].isalnum() else s[1:])
len_tokens = sorted(sentences, key=lambda s: len(s))

lines = []
i = 0
for i,t in enumerate(sentences):
    obj =   {
                "default": t,
                "length": len_tokens[i],
                "alpha": alpha_tokens[i]
            }
    lines.append(obj)
    i+=1

with open('lines.json','w+', encoding='utf-8') as f:
    json.dump(lines, f, ensure_ascii=False)


i = 0
p_indices = []
for p in paragraphs:
    l = []
    for k in range(len(p)):
        l.append(i)
        i+=1
    p_indices.append(l)


with open('p_indices.json', 'w+') as f:
    json.dump(p_indices, f)