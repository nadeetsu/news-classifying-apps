# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:47:33 2020

@author: nads
"""

import pandas as pd
import re

#file intent
#file_name = 'positive.csv'
#file_name = 'negative.csv'
file_name = 'neutral.csv'

## detik
#df = pd.read_csv('intent/det/'+file_name)
## kompas
#df = pd.read_csv('intent/kps/'+file_name)
## tempo
#df = pd.read_csv('intent/tmp/'+file_name)
## liputan6
df = pd.read_csv('intent/liputan6/'+file_name)


cont = df[df.title != 'title']
cont = df[df.descs != 'detik']

removeSpacing= r'[ \t ]+$'
allowAlphabet = "[^a-zA-Z0-9]"
removeUnsual = r'[^\w]'
removeWords = r'Detik'

def clean_text(descs):
    descs = descs.lower()
    descs = re.sub(removeSpacing, '', descs)
    descs = re.sub(allowAlphabet, ' ', descs) 
    descs = re.sub(removeUnsual, ' ', descs) 
    descs = re.sub(removeWords, '', descs) 
    return descs

testing = cont.descs
desc_result = []

for t in testing:
    clean = clean_text(t)
    if(clean != ''):
        desc_result.append(clean)
        
#simpan file ke clean
#file = open("clean_intent/det/clean_"+file_name,"x")
#file = open("clean_intent/kps/clean_"+file_name,"x")
#file = open("clean_intent/tmp/clean_"+file_name,"x")
file = open("clean_intent/liputan6/clean_"+file_name,"x")

file.write('descs\n')
for x in desc_result: 
    x=x.replace(",","")
    file.write(x+"\n")
file.close()