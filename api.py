from flask import Flask,render_template, request, make_response, json, url_for
import numpy as np
import json
import pandas as pd
import re
from flask_cors import CORS
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json
import tensorflow as tf
import getpass
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,WebDriverException,StaleElementReferenceException
import time
global graph, modelr
graph = tf.compat.v1.get_default_graph()

#   Define API for scrape
def take_news_data(link):
    driver = webdriver.Chrome()
    driver.get(link)
    news_content = ""
    if "detik" in link:
        try:            
            for t in driver.find_elements_by_class_name('detail__body'):
                for i in t.find_elements_by_tag_name('p'):
                    news_content = "{}{}".format(news_content,i.text)
        except:
            print("cannot fetch data") 
        driver.quit()
    elif "kompas" in link:
        try:
            for t in driver.find_elements_by_class_name('read__content'):
                for d in t.find_elements_by_tag_name('p'):
                    news_content = "{}{}".format(news_content,d.text)
        except:
            print("cannot fetch data")
        driver.quit()
    elif "tempo" in link:
        try:
            for t in driver.find_elements_by_id('isi'):
                for d in t.find_elements_by_tag_name('p'):
                    news_content = "{}{}".format(news_content,d.text)
        except:
            print("cannot fetch data")
        driver.quit()
    return news_content

def stemming_data(link):
    data_news = take_news_data(link)
    print(data_news)
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    output   = stemmer.stem(data_news)
    return output

app = Flask(__name__)
CORS(app)

#   Define model
model_path = './lstm-model/model/model.json'
model_weights_path = './lstm-model/model/model.h5'
dictionary_path = './lstm-model/model/dictionary.json'
MAX_NB_WORDS = 3500
MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 300

#   Load model
json_file = open(model_path, "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights(model_weights_path)
print("Model has loaded")

#   Make Prediction
loaded_model._make_predict_function()

loaded_model.compile(loss='categorical_crossentropy', 
    optimizer='adam', metrics=['accuracy'])

#   Load word index tokenizer
with open(dictionary_path, 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)

tokenizer = Tokenizer(num_words=MAX_NB_WORDS, 
    filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(dictionary)

#   Cleaning input
removeSpacing= r'[ \t ]+$'
allowAlphabet = "[^a-zA-Z0-9]"
removeUnsual = r'[^\w]'

def clean_text(text):
    text = text.lower()
    text = re.sub(removeSpacing, '', text)
    text = re.sub(allowAlphabet, ' ', text)
    text = re.sub(removeUnsual, ' ', text)
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classifiers')
def classifiers():
    return render_template('content.html')

@app.route('/predicts', methods=['POST'])
def predicts():
    data = clean_text(request.form['content'])
    content = [data]
    print(content)

    text_seq = tokenizer.texts_to_sequences(content)
    text_padded = pad_sequences(text_seq, maxlen=MAX_SEQUENCE_LENGTH)

    with graph.as_default():
        pred = loaded_model.predict(text_padded)

    
    labels = ['negative','neutral','positive']

    pred_result = labels[np.argmax(pred)]

    return render_template('result.html',pred_result=pred_result, content=request.form['content'])

@app.route('/classifylink')
def classifylink():
    return render_template('content-link.html')

@app.route('/predlink', methods=['POST'])
def predlink():
    data_link = request.form['contentLink']
    link_scrap = stemming_data(data_link)
    link_scrap = clean_text(link_scrap)
    content = [link_scrap]
    ans = ''.join(content)
    print(content)

    text_seq = tokenizer.texts_to_sequences(content)
    text_padded = pad_sequences(text_seq, maxlen=MAX_SEQUENCE_LENGTH)

    with graph.as_default():
        pred = loaded_model.predict(text_padded)

    labels = ['negative','neutral','positive']

    results = labels[np.argmax(pred)]

    return render_template('result-link.html', results=results, content=ans)


if __name__ == '__main__':
	init()
	app.run(debug=False,host='0.0.0.0')