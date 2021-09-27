import itertools
import json
import re
import spacy

from spacy.language import Language
from bs4 import BeautifulSoup

@Language.component('prevent-sbd')
def prevent_sbd(doc):
    """ Ensure that SBD does not run on tokens inside quotation marks and brackets. """
    quote_open = False
    bracket_open = False
    can_sbd = True
    for token in doc:
        # Don't do sbd on these tokens
        if not can_sbd:
            token.is_sent_start = False

        # Not using .is_quote so that we don't mix-and-match different kinds of quotes (e.g. ' and ")
        # Especially useful since quotes don't seem to work 
        # well with .is_left_punct or .is_right_punct
        if token.text == '"':
            quote_open = False if quote_open else True
        elif token.is_bracket and token.is_left_punct:
            bracket_open = True
        elif token.is_bracket and token.is_right_punct:
            bracket_open = False

        can_sbd = not (quote_open or bracket_open)

    return doc

nlp = spacy.load('en_core_web_sm', disable=['ner', 'textcat'])
nlp.add_pipe('prevent-sbd', before='parser')

with open('greatgatsby.html', 'r') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

reg = re.compile('chapter-*')
text = soup.find_all('p')
paragraphs = [t.text for t in text]
docs = list(nlp.pipe(paragraphs))

i=0
sentences = []
p_indices = []
for doc in docs:
    l = []
    for sent in doc.sents:
        sentences.append(sent.text)
        l.append(i)
        i+=1
    p_indices.append(l)

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

with open('p_indices.json', 'w+') as f:
    json.dump(p_indices, f)
