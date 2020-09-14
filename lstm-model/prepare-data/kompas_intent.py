# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:06:22 2020

@author: nads
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:01:08 2020

@author: nads
"""

import pandas as pd

input = 'clean_kompas.csv'
#out_positive = 'positive.csv'
#out_negative = 'negative.csv'
out_neutral = 'neutral.csv'
df = pd.read_csv('clean_data/clean_i/'+input)

# identifying missing values
miss_value = df[df['title'].isnull() |df['descs'].isnull()]

no_missing_value = df.dropna()
news = no_missing_value[no_missing_value.descs != ' Ø¥ÙÙ†ÙŽÙ‘Ø§Ù„Ø¯ÙÂ Ø¥Ù']

"""
terms for each intent
"""
# positive content
#terms=['prestasi','penghargaan','pelatihan','memotivasi','kerja sama', 'manfaat','juara'
#       'peningkatan','berbakat','motivasi diri','antisipasi','pencegahan','menginspirasi',
#       'panutan', 'memberikan sumbangan','mendapat dukungan','berikan sumbangan','berinovasi',
#       'menjuarai','cegah','kolaborasi']

# negative content
#terms = ['bugil','ganja','paksa','aniaya','tega','hadang','tersangka','pornografi',
#         'teror','minuman keras','tewas', 'narkoba','tembak','bacok','cabul',
#         'penipuan','pencuri','komplotan','penyelundupan','mengancam','kecaman',
#         'pembunuhan','perampok','pemerasan','pidana','merampas','pelaku']

# neutral content
terms = ['bacaan', 'curiga','mengkritik', 'sholat', 'ibadah','duga', 'saran', 
         'menanggapi', 'imbau','bungkam','angkat bicara','prediksi','diperkirakan',
         'pertanyakan','protes','pasrah','usut',
         'mendadak','usul','ramal','menyayangkan','mengaku','suspect','demo','buruh']

data_filter = news[news['descs'].str.contains('|'.join(terms))]

#export_csv = data_filter.to_csv (r'intent/kps/'+out_positive, index = None, header=True) 
#export_csv = data_filter.to_csv (r'intent/kps/'+out_negative, index = None, header=True)
export_csv = data_filter.to_csv (r'intent/kps/'+out_neutral, index = None, header=True) 
