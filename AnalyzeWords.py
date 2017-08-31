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

stop_words = list(stopwords.words('english')) + list(string.punctuation)
stop_words_economic = ['it', '\'s', '--', '\'\'', 'For', 'As', 'physicians', 'Alex', 'NNY']
stop_words_technical = []
stop_words_legal = []
stop_words_ethical = []
stop_words_procedural = []
stop_words_political = []
         
# add all stop words together
stop_words.extend(stop_words_economic + stop_words_technical + stop_words_legal + stop_words_ethical + stop_words_procedural + stop_words_political)

print("punctuation = " + string.punctuation)
print("len(stop_words) = " + str(len(stop_words)))

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
spread.plot(50, cumulative=True)

# Print the word - frequency
for word, frequency in spread.most_common(100):
    print(u'{} - {}'.format(word, frequency))
