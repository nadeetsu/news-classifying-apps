# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:12:04 2020

@author: nads
"""

import json
import re
import numpy as np
import pandas as pd
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json

#define
model_path = './model/model.json'
model_weights_path = './model/model.h5'
dictionary_path = './model/dictionary.json'
file_testing = './testing/data_test.csv'
output_testing = './testing/out/output_prediction.csv'

MAX_NB_WORDS = 3500
MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 300

#   read file testing
df = pd.read_csv(file_testing)

removeSpacing= r'[ \t ]+$'
allowAlphabet = "[^a-zA-Z0-9]"
removeUnsual = r'[^\w]'

def clean_text(text):
    text = text.lower()
    text = re.sub(removeSpacing, '', text)
    text = re.sub(allowAlphabet, ' ', text)
    text = re.sub(removeUnsual, ' ', text)
    return text

descs = df.descs

clean_descs = []
for t in descs:
    clean = clean_text(t)
    if(clean != ''):
        clean_descs.append(clean)
    
#   load model
json_file = open(model_path, "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights(model_weights_path)
print('Loaded model from disk')

loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#   load word index tokenizer
with open(dictionary_path, 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)
    
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(dictionary)

#   predict classes
def predict_classes(new_content):
    text_seq = tokenizer.texts_to_sequences(new_content)
    text_padded = pad_sequences(text_seq, maxlen=MAX_SEQUENCE_LENGTH)
    pred = loaded_model.predict(text_padded)
    labels = ['negative', 'neutral','positive']
    classes = labels[np.argmax(pred)]
    return classes

classes_predict=[]  
for row in clean_descs:
    predict = predict_classes([row])
    classes_predict.append(predict)
    
final_data = list(zip(df.descs, df.classes, classes_predict))

#   validating data whether valid or not
file = open( output_testing,"x", errors="ignore")
file.write('Konten,Prediksi Manual,Prediksi Model,Simpulan\n')
for row in final_data:
    texts=row[0].replace(",","")
    classes = row[1]
    classes_predict = row[2]
    if classes == classes_predict:
        validation = 'Sesuai'
    else:
        validation = 'Tidak Sesuai'

    file.write(texts+","+row[1]+","+row[2]+","+validation+"\n")
    
file.close()