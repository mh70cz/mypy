# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:39:09 2019

@author: mh70
"""
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')



import nltk
sentence_ = "Ve snaze o podporu znalostní ekonomiky, odchod od ekonomiky montoven a konec levné práce se vláda rozhodla dodatečně zdanit dva nejpokročilejší sektory naší ekonomiky, finanční služby a telco."
sentence = "Bring us food, or be food yourself."
tokens = nltk.word_tokenize(sentence)

tokens
tagged = nltk.pos_tag(tokens)

article = """Ve stavbě letadel byli pak relativně úspěšní bratři Eugen a Hugo Čihákovi, mimo jiné bratranci Kašpara. Jejich nejpovedenější stroj se zrodil koncem roku 1912, nesl jméno Rapid a ne úplnou náhodou svými tvary připomínal francouzské stroje Morane-Saulnier. Rapid se vlastně stal i nejúspěšnější leteckou konstrukcí do roku 1914 u nás.
"""

tokens_sen = nltk.sent_tokenize(article)
