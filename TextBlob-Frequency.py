"""
@author: tdortiz
"""

import os
import sys
import io
import nltk
import string
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

stop_words = list(stopwords.words('english')) + list(string.punctuation)
stop_words_economic = ['it', '\'s', '--', '\'\'', 'For', 'As', 'physicians', 'Alex', 'NNY']
stop_words_technical = []
stop_words_legal = []
stop_words_ethical = []
stop_words_procedural = []
stop_words_political = []
         
# add all stop words together
stop_words.extend(stop_words_economic + stop_words_technical + stop_words_legal + stop_words_ethical + stop_words_procedural + stop_words_political)

# open the file
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Hospitals-Economic/xx01"
abs_path = os.path.join(script_dir, rel_path)
data = open(abs_path, encoding='utf-8').read()

# print(data) # just a test
words = word_tokenize(data)
words_selected = []
for w in words:
    if w not in stop_words:
        words_selected.append(w)

# Plot the graph
spread = nltk.FreqDist(words_selected)
#spread.plot(50, cumulative=True)

# Print the word - frequency
freq_words = []
print("\tWORD - FREQUENCY")
for word, frequency in spread.most_common(100):
    print(u'{} - {}'.format(word, frequency))
    freq_words.append(word)

bunch = TextBlob(data)
all_sentences = bunch.sentences
key_words = ['tax', 'taxes', 'economic', 'economy', 'payroll', 'finance', 'price', 'cost', 'fine', 'cutback', 'bill']
freq_words.extend(key_words)

output = open(os.path.join(script_dir, 'textblob-freq.txt'), 'w')
sent_num = 0
for sentence in all_sentences:
    if(any(map(lambda word: word in sentence, freq_words))):
        print(str(sent_num) + ":\t" + str(sentence) + "\n")
        sent_num += 1
        output.write(str(sent_num) + ":\t" + str(sentence) + "\n\n")
output.close()