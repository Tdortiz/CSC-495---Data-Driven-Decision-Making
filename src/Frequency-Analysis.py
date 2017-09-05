"""
@author: tdortiz
"""

import os
import sys
import io
import nltk
import string
from pathlib import Path
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

repo_dir = Path(__file__).resolve().parents[1]

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
data = open(os.path.join(repo_dir, "Hospitals-Economic/xx01"), encoding='utf-8').read()

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
