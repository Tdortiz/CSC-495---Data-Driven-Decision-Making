"""
@author: tdortiz
"""

import os
from pathlib import Path
from textblob import TextBlob

# open the file
repo_dir = Path(__file__).resolve().parents[1]
data = open(os.path.join(repo_dir, "input/Hospital-Ranking/hospital-ranking.TXT"), encoding='utf-8').read()
bunch = TextBlob(data)
all_sentences = bunch.sentences

# Create key words
key_words            = set()
key_words_economic   = {'$', 'dollar', 'tax', 'taxes', 'job', 'jobs', 'economic', 'economy', 'financial', 'growth', 'finance', 'affordable', 'cheap', 'inexpensive', 'cost-effective', 'cost-efficient', 'sustainable', 'fiscal', 'payroll', 'finance', 'price', 'cost', 'fine', 'cutback', 'money', 'wage', 'salary'}
key_words_technical  = set()
key_words_legal      = {'hospitals','patients','health','legal','documents','medical','court','children','reserved','publication','newspaper','doctors','rights','government','news','language','copyright','services'}
key_words_ethical    = set()
key_words_procedural = {'procedure', 'procedural', 'policy', 'scheme', 'measure', 'process', 'action', 'operation', 'ways', 'rules', 'mechanism', 'proceeding', 'practice', 'progress', 'step', 'fast', 'efficiency'}
key_words_political  = set()

# add all key words together
key_words |= key_words_economic | key_words_technical | key_words_legal | key_words_ethical | key_words_procedural | key_words_political

output = open(os.path.join(repo_dir, 'output/' + os.path.splitext(__file__)[0] + '_output.txt'), 'w', encoding='utf-8')
sent_num = 0
for sentence in all_sentences:
    if(any(map(lambda word: word in sentence, key_words))):
        print(str(sent_num) + ":\t" + str(sentence) + "\n")
        sent_num += 1
        output.write(str(sent_num) + ":\t" + str(sentence) + "\n\n")
output.close()
