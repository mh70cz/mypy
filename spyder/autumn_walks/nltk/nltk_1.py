# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:39:09 2019

@author: mh70
"""
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')



import nltk
sentence = "Ve snaze o podporu znalostní ekonomiky, odchod od ekonomiky montoven a konec levné práce se vláda rozhodla dodatečně zdanit dva nejpokročilejší sektory naší ekonomiky, finanční služby a telco."
tokens = nltk.word_tokenize(sentence)

tokens
tagged = nltk.pos_tag(tokens)

tagged