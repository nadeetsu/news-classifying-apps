import pandas as pd
import getpass

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,WebDriverException,StaleElementReferenceException
import time

def take_news_data(link):
    driver = webdriver.Firefox()
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
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    output   = stemmer.stem(data_news)
    return output