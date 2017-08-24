import sys
import io
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

stop_words = list(stopwords.words('english'))
stop_words.extend(('(', ')', ':', '``', 'it', ',', '.', '\'s', '', '--', '\'\'', 'For', 'As', 'physicians'))

# open the file
data = open('/home/thomas/github/CSC-495-Data-Driven-Decision-Making/Hospitals-Economic/xx01', encoding='utf-8').read()

# print(data) # just a test
words = word_tokenize(data)
words_selected = []
for w in words:
    if w not in stop_words:
        words_selected.append(w)

# print(words_selected)

spread = nltk.FreqDist(words_selected)
spread.plot(50, cumulative=True)
for word, frequency in spread.most_common(100):
    print(u'{} - {}'.format(word,frequency))