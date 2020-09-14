# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:03:49 2020

@author: nads
"""

import pandas as pd

input = 'clean_tempo.csv'
#out_positive = 'positive.csv'
#out_negative = 'negative.csv'
out_neutral = 'neutral.csv'
df = pd.read_csv('clean_data/clean_i/'+input)

# identifying missing values
miss_value = df[df['title'].isnull() | df['descs'].isnull()]

no_missing_value = df.dropna()
news = no_missing_value[no_missing_value.descs != ' Ø¥ÙÙ†ÙŽÙ‘Ø§Ù„Ø¯ÙÂ Ø¥Ù']

"""
terms for each intent
"""
# positive content
#terms = ['bantuan','damai', 'dukung','pelatihan','peningkatan','inspirasi','kerja sama', 'puji', 'terima kasih', 'motivasi', 'antisipasi','didapuk', 'duta','omset','sukses','sembuh','doa','berhasil','beasiswa','sertifikat','inspiratif','']

# negative content
#terms = ['bugil','ganja','paksa','aniaya','tega','hadang','gelantung','mesum',
#         'teror','meracuni','tewas', 'narkoba','tembak','bacok','cabul','nipu',
#         'merugikan','bajak','mencuri','komplotan','bersetubuh','erotis','psk'
#         ,'pembunuhan','rampok','pemerasan','pidana','rampas','iming','pelaku']

# neutral content
terms = ['bacaan', 'dicurigai','puasa', 'mengkritik', 'sholat', 'ibadah','menduga', 'saran', 
         'mengutarakan', 'imbau','bungkam','irit bicara','prediksi','diperkirakan',
         'mendadak','usul','ramal','dipastikan','mengaku','suspect','demo','buruh']

data_filter = news[news['descs'].str.contains('|'.join(terms))]

# csv
#export_csv = data_filter.to_csv (r'intent/tmp/'+out_positive, index = None, header=True) 
#export_csv = data_filter.to_csv (r'intent/tmp/'+out_negative, index = None, header=True)
export_csv = data_filter.to_csv (r'intent/tmp/'+out_neutral, index = None, header=True) 

#remove  detikcom