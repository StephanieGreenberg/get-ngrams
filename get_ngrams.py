import nltk
import re
import csv

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk import ngrams

#open Myth of Male Power text
momp = open("momp.txt").read().lower()

#only look at alphanumeric characters, no punctuation
momp = re.sub(r'([^\s\w]|_)+', '', momp)

stop_words = set(stopwords.words('english'))

#tokenize the document
word_tokens = word_tokenize(momp)

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

#get 100 most common unigrams
unigram_count = Counter(ngrams(filtered_sentence, 1))
most_common_unigrams = unigram_count.most_common(100)

#get 100 most common bigrams
bigram_count = Counter(ngrams(filtered_sentence, 2))
most_common_bigrams = bigram_count.most_common(100)

#get 100 most common trigrams
trigram_count = Counter(ngrams(filtered_sentence, 3))
most_common_trigrams = trigram_count.most_common(100)

#write unigrams to file
with open('unigrams.csv', mode='w') as unigrams_file:
    file_writer = csv.writer(unigrams_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
    for unigram in most_common_unigrams:
        file_writer.writerow([unigram[0][0], unigram[1]])

#write bigrams to file
with open('bigrams.csv', mode='w') as bigrams_file:
    file_writer = csv.writer(bigrams_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
    for bigram in most_common_bigrams:
        file_writer.writerow([bigram[0][0] + " " + bigram[0][1], bigram[1]])

#write trigrams to file
with open('trigrams.csv', mode='w') as trigrams_file:
    file_writer = csv.writer(trigrams_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
    for trigram in most_common_trigrams:
        file_writer.writerow([trigram[0][0] + " " + trigram[0][1] + " " + trigram[0][2], trigram[1]])

