"""
@author: tdortiz
"""

import os
from textblob import TextBlob

# open the file
script_dir = os.path.dirname(__file__) # absolute dir the script is in
rel_path = "Hospitals-Economic/xx01"
abs_path = os.path.join(script_dir, rel_path)
data = open(abs_path, encoding='utf-8').read()
bunch = TextBlob(data)
all_sentences = bunch.sentences

# Create key words
key_words = ['tax', 'taxes', 'economic', 'economy', 'payroll', 'finance', 'price', 'cost', 'fine', 'cutback', 'money', 'wage', 'salary']

output = open(os.path.join(script_dir, 'textblob.txt'), 'w')
sent_num = 0
for sentence in all_sentences:
    if(any(map(lambda word: word in sentence, key_words))):
        print(str(sent_num) + ":\t" + str(sentence) + "\n")
        sent_num += 1
        output.write(str(sent_num) + ":\t" + str(sentence) + "\n\n")
output.close()