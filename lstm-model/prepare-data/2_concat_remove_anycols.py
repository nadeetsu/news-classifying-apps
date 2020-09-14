# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:44:45 2020

@author: nads
"""

import pandas as pd

# import and read csv
#input_file = 'tempo_nodup.csv'
#input_file = 'kompas_nodup.csv'
input_file = 'detik_nodup.csv'

#output_file = 'clean_tempo.csv'
#output_file = 'clean_kompas.csv'
output_file = 'clean_detik.csv'

df = pd.read_csv("clean_data/no_duplicate/"+input_file)

# concat several columns for further classification
df['descs'] = df[df.columns[3:]].apply(
    lambda x: ' '.join(x.dropna().astype(str)),
    axis=1
)

#   drop any unsued column
##  tempo
#export = df.drop(df.columns[2:83], axis=1).replace("\t","")
##  detik
export = df.drop(df.columns[2:114], axis=1).replace("\t","")
##  kompas
#export = df.drop(df.columns[2:114], axis=1).replace("\t","")

export.to_csv('clean_data/clean_i/'+output_file, index=False, header=True)