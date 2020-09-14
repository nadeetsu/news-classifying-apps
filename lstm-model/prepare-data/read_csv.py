# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:17:22 2020

@author: nads
"""

import pandas as pd

input_file = 'clean_positif.csv'
output_file = 'tempok.csv'
#output_file = 'waktu.csv'

df = pd.read_csv('state.csv')
#df = pd.read_csv(output_file)
df
#export = df.drop(df.columns[[0]], axis=1).replace("\t","")
#
#export.to_csv('clean_data/totals.csv', index=False, header=True)

#import nltk
#nltk.download()
#from nltk.tokenize import sent_tokenize, word_tokenize
#
#data = "All work and no play makes jack a dull boy, all work and no play"
#print(word_tokenize(data))