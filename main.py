import itertools
import json
import nltk
import re

from bs4 import BeautifulSoup

nltk.download('punkt')

with open('greatgatsby.html', 'r') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

reg = re.compile('chapter-*')
text = soup.find_all('p')
paragraphs = [nltk.sent_tokenize(l.text) for l in text]
sentences = list(itertools.chain(*paragraphs))

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