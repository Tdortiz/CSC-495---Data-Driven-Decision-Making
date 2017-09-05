"""
@author: tdortiz
"""

import os
from pathlib import Path
from textblob import TextBlob

# open the file
repo_dir = Path(__file__).resolve().parents[1]
data = open(os.path.join(repo_dir, "Hospitals-Economic/xx01"), encoding='utf-8').read()
bunch = TextBlob(data)
all_sentences = bunch.sentences

# Create key words
key_words            = []
key_words_economic   = ['tax', 'taxes', 'economic', 'economy', 'payroll', 'finance', 'price', 'cost', 'fine', 'cutback', 'money', 'wage', 'salary']
key_words_technical  = []
key_words_legal      = []
key_words_ethical    = []
key_words_procedural = []
key_words_political  = []

# add all key words together
key_words.extend(key_words_economic + key_words_technical + key_words_legal + key_words_ethical + key_words_procedural + key_words_political)

output = open(os.path.join(repo_dir, 'output/textblob.txt'), 'w')
sent_num = 0
for sentence in all_sentences:
    if(any(map(lambda word: word in sentence, key_words))):
        print(str(sent_num) + ":\t" + str(sentence) + "\n")
        sent_num += 1
        output.write(str(sent_num) + ":\t" + str(sentence) + "\n\n")
output.close()