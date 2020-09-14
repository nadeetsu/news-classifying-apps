# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:01:08 2020

@author: nads
"""

import pandas as pd

input = 'liputan6_nodup.csv'
out_positive = 'positive.csv'
#out_negative = 'negative.csv'
#out_neutral = 'neutral.csv'
df = pd.read_csv('clean_data/no_duplicate/'+input)

# identifying missing values
miss_value = df[df['title'].isnull() | df['desc'].isnull()]

no_missing_value = df.dropna()
news = no_missing_value[no_missing_value.desc != ' Ø¥ÙÙ†ÙŽÙ‘Ø§Ù„Ø¯ÙÂ Ø¥Ù']


# positive content
terms = ['bantuan','damai', 'pelatihan','peningkatan','inspirasi','kerja sama', 
         'puji', 'motivasi', 'antisipasi','didapuk', 'duta','penghargaan','sukses',
         'sembuh','doa','berhasil','beasiswa','sertifikat','inspiratif','imbauan', 'apresiasi']

# negative content
#terms = ['bugil','ganja','paksa','aniaya','tega','hadang','gelantungan','mesum','teror','meracuni','tewas', 'narkoba','tembak','bacok','cabul','penipuan','merugikan','dibajak','mencuri','komplotan','bersetubuh','erotis','psk','bunuh','rampok','pemerasan','pidana','rampas','iming','pelaku']

# neutral content
#terms = ['bacaan', 'dicurigai','puasa', 'mengkritik', 'sholat', 'ibadah','menduga', 'saran', 
#         'mengutarakan', 'imbau','bungkam','irit bicara','prediksi','diperkirakan',
#         'mendadak','usul','ramal','dipastikan','mengaku','suspect','demo','buruh']

data_filter = news[news['desc'].str.contains('|'.join(terms))]

export_csv = data_filter.to_csv (r'intent/liputan6/'+out_positive, index = None, header=True) 
#export_csv = data_filter.to_csv (r'intent/liputan6/'+out_negative, index = None, header=True)
#export_csv = data_filter.to_csv (r'intent/liputan6/'+out_neutral, index = None, header=True) 
