# Implementation of TF-IDF
from __future__ import division
import math

def term_frequency(word, document):
    """ The number of times the word appears in document normalized by the number of words in the document """
    return document.count(word) / len(document.split(" "))

def idf(word, word_list):
    """ Computes the inverse document frequency for a given word and a corpus """
    N = len(word_list)
    num_documents_containing_word = len([True for document in word_list if word in document])
    return math.log(N / num_documents_containing_word + 1) # + 1 accounts for if the word doesn't occur in any of the documents

def tf_idf(word, document, word_list):
    return term_frequency(word, document) * idf(word, word_list)


