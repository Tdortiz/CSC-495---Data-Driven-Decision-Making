import os
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')

# open the file
repo_dir = Path(__file__).resolve().parents[1]
with open(os.path.join(repo_dir, "input/Hospital-Ranking/hospital-ranking.TXT"), encoding='utf-8') as data:
    words = word_tokenize(data.read())

words = word_tokenize(intake)
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(words)
idf = vectorizer.idf_
print (dict(zip(vectorizer.get_feature_names(), idf)))
#print(intake)