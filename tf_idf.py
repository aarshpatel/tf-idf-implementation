# Implementation of TF-IDF
from __future__ import division
import numpy as np

def term_frequency(word, document):
    """ The number of times the word appears in document normalized by the number of words in the document """
    return document.count(word) / len(document.split(" "))

