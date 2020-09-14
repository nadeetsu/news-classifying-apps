# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:32:58 2020

@author: nads
"""

import pandas as pd

#   import dataframe news
#file_corpus = 'detik.csv'
#file_corpus = 'kompas.csv'
file_corpus = 'liputan6.csv'
#file_corpus = 'tempo.csv'

df = pd.read_csv('source_datas/'+file_corpus)

df.drop_duplicates(subset="title", keep=False, inplace=True)

#   write data after clean duplicate
#out_clean = 'tempo_nodup.csv'
#out_clean = 'detik_nodup.csv'
#out_clean = 'kompas_nodup.csv'
out_clean = 'liputan6_nodup.csv'

df.to_csv('clean_data/no_duplicate/' + out_clean, index=False)