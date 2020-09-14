# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:01:08 2020

@author: nads
"""

import pandas as pd
# satrawi/wordlist indonesian
input = 'clean_detik.csv'
#out_positive = 'positive.csv'
#out_negative = 'negative.csv'
out_neutral = 'neutral.csv'
df = pd.read_csv('clean_data/clean_i/'+input)

# identifying missing values
miss_value = df[df['date'].isnull() | df['title'].isnull() | df['descs'].isnull()]

no_missing_value = df.dropna()
news = no_missing_value[no_missing_value.descs != ' Ø¥ÙÙ†ÙŽÙ‘Ø§Ù„Ø¯ÙÂ Ø¥Ù']


# positive content
#terms = ['bantuan','damai', 'pelatihan','peningkatan','inspirasi','kerja sama', 'tauladan', 'menyukseskan',
#         'puji', 'motivasi', 'antisipasi','didapuk', 'duta','penghargaan','sukses', 'pencerahan',
#         'sembuh','doa','berhasil','beasiswa','sertifikat','inspiratif','imbau', 'membulatkan tekad',
#         'apresiasi', 'menang', 'memenangkan', 'pemenang', 'memuji', 'doakan', 'bagus','bibit unggul',
#         'memperbagus', 'indah', 'peluang', 'edukatif', 'edukasi', 'dukung', 'donor', 'donatur',
#         'efektif', 'ekonomis', 'fasih', 'favorit', 'giat', 'gigih', 'gemilang', 'gapai', 'harapan', 
#         'hebat', 'hibah', 'hidayah', 'ikhtiar','informatif', 'inisiatif', 'optimal', 'bekerja keras',
#         'pantang meneyerah', 'inovasi', 'inovatif', 'sosialisasi', 'kagum', 'semangat', 'maksimalkan',
#         'silaturahmi','pererat', 'alhamdulillah', 'antusias', 'bantu', 'hore', 'inovator', 'kreativitas',
#         'kreatif', 'kolaborasi', 'relawan', 'sportivitas', 'tangguh', 'solidaritas', 'optimis', 'salut', 
#         'ulet', 'terpukau', 'pukau', 'persaudaraan', 'pencegahan', 'tingkatkan', 'tekun', 'keberhasilan',
#         'kebersamaan', 'bersama', 'diminati', 'dilestarikan', 'diberdayakan','dianugerahi', 'bahu-membahu', 'rangkul']

# negative content
#terms = ['bugil','ganja','paksa','aniaya','tega','hadang','gelantungan','mesum', 'koruptor',
#        'teror','meracuni','tewas', 'narkoba','tembak','bacok','cabul','penipuan', 'kongkalikong',
#        'merugikan','dibajak','mencuri','komplotan','bersetubuh','erotis','psk','bunuh', 'maniak',
#        'rampok','pemerasan','pidana','rampas','iming','pelaku', 'kekerasan', 'penistaan', 'memalsukan',
#        'ricuh', 'leceh', 'pelecehan', 'perkosa', 'pemaksaan', 'nista', 'mabuk', 'memalak', 'membombardir',
#        'malak', 'dendam', 'sakit hati', 'cekcok', 'porno', 'pornografi','ekstasi', 'pecandu',
#        'komplot', 'berkomplot', 'bully', 'ejek', 'mengejek', 'diejek', 'prostitusi', 'konflik',
#        'pencuri' , 'culik', 'menculik', 'modus', 'kedok', 'berkedok', 'teroris', 'sesat', 'kasar',
#        'tesangka', 'pemalsuan', 'duel', 'pukul', 'memukul', 'penusukan', 'sodomi', 'ugal-ugalan', 
#        'sabotase', 'fitnah', 'serang', 'menyerang', 'intimidasi', 'arogan', 'korupsi', 'penggelapan',
#        'menggelapkan', 'koruptor', 'zalim', 'kejam', 'bodong', 'curang', 'ancam', 'anarkis', 'bantai',
#        'preman', 'bantai', 'judi', 'biadab', 'buron', 'dengki', 'hasut', 'jarah', 'jegal', 'kalap', 'kriminal',
#        'mafia', 'siksa', 'menyiksa', 'sindikat', 'todong', 'menodong', 'copet', 'jambret', 'maling','pelacur', 'kacau',
#        'bandit', 'menghajar', 'mengumpat', 'seteru', 'tersangka', 'menuntut', 'adu domba', 'akal bulus', 'acuh tak acuh']

# neutral content
terms = ['bacaan', 'dicurigai','puasa', 'mengkritik', 'sholat', 'ibadah','menduga', 'saran', 'meluruskan',
         'mengutarakan', 'bungkam','irit bicara','prediksi','diperkirakan', 'memperkirakan', 'melerai',
         'mendadak','usul','ramal','dipastikan','mengaku','suspect','demo','buruh', 'curiga', 'rebut',
         'mencurigakan', 'kecurigaan', 'diduga', 'dugaan', 'terduga', 'duga', 'tuduh', 'nuduh', 'mengira',
         'menuduh', 'tuding', 'menuding', 'menyayangkan', 'kecewa', 'kemungkinan', 'opini', 'halang',
         'argumen', 'sangka', 'menyangka', 'mengklaim', 'konfirmasi', 'toleransi', 'klarifikasi',
         'kaji', 'meninggal', 'gagal', 'cenderung', 'kritik', 'terkejut', 'disayangkan', 'menyayangkan',
         'revitalisasi','iktikad', 'kalah', 'tunda', 'mengalah', 'mundur', 'mitos', 'misteri', 'konon', 'usut', 'kaget', 'sakit']

data_filter = news[news['descs'].str.contains('|'.join(terms))]

#export_csv = data_filter.to_csv (r'intent/det/'+out_positive, index = None, header=True) 
#export_csv = data_filter.to_csv (r'intent/det/'+out_negative, index = None, header=True)
export_csv = data_filter.to_csv (r'intent/det/'+out_neutral, index = None, header=True) 
