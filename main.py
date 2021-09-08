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
sentences = list(itertools.chain(*[nltk.sent_tokenize(l.text) for l in text]))

alpha_tokens = sorted(sentences, key=lambda s: s if s[0].isalnum() else s[1:])
len_tokens = sorted(sentences, key=lambda s: len(s))

lines = []
i = 0
for t in sentences:
    obj =   {
                "line": t,
                "default_position": i,
                "len_position": len_tokens.index(t),
                "alpha_tokens": alpha_tokens.index(t)
            }
    lines.append(obj)
    i+=1

with open('lines.json','w+', encoding='utf-8') as f:
    json.dump(lines, f, ensure_ascii=False)


