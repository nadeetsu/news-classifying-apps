import json
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json

#define
model_path = './model/model.json'
model_weights_path = './model/model.h5'
dictionary_path = './model/dictionary.json'

MAX_NB_WORDS = 3500
MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 300

#load model
json_file = open(model_path, "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(model_weights_path)
print('succes load model from disk')

loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', 
                     metrics=['accuracy'])

#   load word index tokenizer
with open(dictionary_path, 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)
    
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, 
                      filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(dictionary)

def predict_classes(new_desc):
    predict_value=[]
    #    word embedding & Word Embedding
    text_seq = tokenizer.texts_to_sequences(new_desc)
    text_padded = pad_sequences(text_seq, maxlen=MAX_SEQUENCE_LENGTH)
    print('\nWord Embedding: ')
    print(text_padded)
    
    #    count probability value
    pred = loaded_model.predict(text_padded)
    labels = ['negative','neutral','positive']
    classes = labels[np.argmax(pred)]
    for row in pred:
        for elem in row: 
            predict_value.append(elem)
            
    combined = np.vstack((labels, predict_value)).T
    print('\nProbablity value: ')
    print(combined)
    
    print('\nPredicted: ' + classes)
    return classes

def contents(conts):
    conts = input('\nKonten: ')
    conts = [conts]
    predict_classes(conts)
    
contents('Test')