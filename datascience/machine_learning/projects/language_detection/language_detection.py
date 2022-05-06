#!/usr/bin/env python
# coding: utf-8

# ![](https://media.istockphoto.com/vectors/many-arms-raised-of-diverse-and-multiethnic-people-holding-speech-vector-id1337786250?k=20&m=1337786250&s=612x612&w=0&h=zTFBr4VtORLSiWnRNCUTo0nbz4CEyHg8JW2w92E0tEU=)
# 
# <br>
# 
# # Portfolio Project: Language Detection
# 
# <br>
# 
# This project involves using Machine Learning to create a Language Detection Model to determine which language is which based on the data given.
# 
# <hr>

# In[409]:


from bs4 import BeautifulSoup
import requests

import re

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# In[2]:


import nltk
nltk.download('punkt')


# In[207]:


import xx_sent_ud_sm
nlp = xx_sent_ud_sm.load()


# In[410]:


from spacy.lang.zh import Chinese
nlp_chinese = Chinese()


# In[436]:


from sudachipy import Dictionary, SplitMode
tokenizer_obj = Dictionary().create()


# In[206]:


import spacy
nlp_greek = spacy.load("el_core_news_sm")


# ### Part 1: Web Scraping
# 
# We need to gather the data that will be used for our model; therefore, we will need to web scrape as much data as we can. The plan is to scrape at least 1,000 sentences per language to allow our model to be more accurate when we test it. 
# 
# The languages that will be used for the `.csv` is: English, Spanish, French, German, Italian, Dutch, Portuguese, Chinese (simplified), Japanese, Korean, Russian, Hebrew, Arabic, Greek, Hindi, Armenian, Georgian, Latin, and Swedish. Each language will have at least 1,000 sentences or phrases, and no more than 1,200. To get the sentences in each language, we will be using a NLTK tokenizer.
# 
# Because `nltk.tokenize` can only support English, Spanish, French, German, Italian, Dutch, Portuguese, Russian, and Swedish; `spacy` will be used for the rest of the languages. 
# 
# *Note: Chinese, Japanese, Greek, Hebrew, Armenian, Georgian, and Latin don't have enough data for the tokenizers to work properly. We will not be using them in our data, but I will continue to keep them is the `language_data.csv`, and will keep all the work I have done for them.
# Due to the nature of Chinese, we will be using data based on the characters/words rather than sentences. Also, for Chinese we will be using the [`jieba`](https://github.com/fxsjy/jieba) python dictionary, and for Japanese we will be using the [`sudachipy`](https://pypi.org/project/SudachiPy/0.2.1/) python dictionary.*

# In[23]:


english_sentences = []

x = 0
while x < 1100:
    for i in range(1):
        webpage_en = requests.get('https://www.coolgenerator.com/random-sentence-generator')
        soup_en = BeautifulSoup(webpage_en.content)
        for sentence in soup_en.select(".content > ul > li > p > b > span"):
            #print(sentence.text)
            tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            for s in tokenized_sentence:
                #print(s.strip())
                english_sentences.append(s.strip())
    x += 1
    
#print(english_sentences)
print(len(english_sentences))


# In[19]:


spanish_sentences = []

x = 0
while x < 1000:
    webpage_sp = requests.get('http://www.smartphrase.com/cgi-bin/randomphrase.cgi?spanish&serious&normal')
    soup_sp = BeautifulSoup(webpage_sp.content)
    #print(soup_it.select("td")[6])
    #print(soup_it.select("tr")[3].find_all('td'))

    for sentence in soup_sp.find_all(attrs = {'bgcolor': '#DCDCFF'}):
        if sentence.select("p"):
            new_sentence = sentence.text.replace(".", ". ").replace("?", "? ").replace("!", "! ")
            #print(new_sentence)
            tokenized_sentence = sent_tokenize(new_sentence)
            #print(tokenized_sentence[0].strip())
            spanish_sentences.append(tokenized_sentence[0].strip())
        
            #this was removing the punctuation
            #new_sentence = re.split(r"[.!?]+", sentence.text.strip())
            #print(new_sentence[0])
    x += 1
    
#print(spanish_sentences)
print(len(spanish_sentences))


# In[20]:


french_sentences = []

x = 0
while x < 1000:
    webpage_fr = requests.get('http://www.smartphrase.com/cgi-bin/randomphrase.cgi?french&serious&normal')
    soup_fr = BeautifulSoup(webpage_fr.content)
    #print(soup_it.select("td")[6])
    #print(soup_it.select("tr")[3].find_all('td'))

    for sentence in soup_fr.find_all(attrs = {'bgcolor': '#DCDCFF'}):
        if sentence.select("p"):
            new_sentence = sentence.text.replace(".", ". ").replace("?", "? ").replace("!", "! ")
            #print(new_sentence)
            tokenized_sentence = sent_tokenize(new_sentence)
            #print(tokenized_sentence[0].strip())
            french_sentences.append(tokenized_sentence[0].strip())
        
            #this was removing the punctuation
            #new_sentence = re.split(r"[.!?]+", sentence.text.strip())
            #print(new_sentence[0])
    x += 1
    
#print(french_sentences)
print(len(french_sentences))


# In[21]:


german_sentences = []

x = 0
while x < 1000:
    webpage_de = requests.get('http://www.smartphrase.com/cgi-bin/randomphrase.cgi?german&serious&normal')
    soup_de = BeautifulSoup(webpage_de.content)
    #print(soup_it.select("td")[6])
    #print(soup_it.select("tr")[3].find_all('td'))

    for sentence in soup_de.find_all(attrs = {'bgcolor': '#DCDCFF'}):
        if sentence.select("p"):
            new_sentence = sentence.text.replace(".", ". ").replace("?", "? ").replace("!", "! ")
            #print(new_sentence)
            tokenized_sentence = sent_tokenize(new_sentence)
            #print(tokenized_sentence[0].strip())
            german_sentences.append(tokenized_sentence[0].strip())
        
            #this was removing the punctuation
            #new_sentence = re.split(r"[.!?]+", sentence.text.strip())
            #print(new_sentence[0])
    x += 1
    
#print(german_sentences)
print(len(german_sentences))


# In[5]:


italian_sentences = []

x = 0
while x < 1000:
    webpage_it = requests.get('http://www.smartphrase.com/cgi-bin/randomphrase.cgi?italian&serious&normal&229&&&&&')
    soup_it = BeautifulSoup(webpage_it.content)
    #print(soup_it.select("td")[6])
    #print(soup_it.select("tr")[3].find_all('td'))

    for sentence in soup_it.find_all(attrs = {'bgcolor': '#DCDCFF'}):
        if sentence.select("p"):
            new_sentence = sentence.text.replace(".", ". ").replace("?", "? ").replace("!", "! ")
            #print(new_sentence)
            tokenized_sentence = sent_tokenize(new_sentence)
            #print(tokenized_sentence[0].strip())
            italian_sentences.append(tokenized_sentence[0].strip())
        
            #this was removing the punctuation
            #new_sentence = re.split(r"[.!?]+", sentence.text.strip())
            #print(new_sentence[0])
    x += 1
    
#print(italian_sentences)
print(len(italian_sentences))


# In[6]:


dutch_sentences = []

x = 0
while x < 1000:
    webpage_du = requests.get('http://www.smartphrase.com/cgi-bin/randomphrase.cgi?dutch&serious&normal')
    soup_du = BeautifulSoup(webpage_du.content)
    #print(soup_it.select("td")[6])
    #print(soup_it.select("tr")[3].find_all('td'))

    for sentence in soup_du.find_all(attrs = {'bgcolor': '#DCDCFF'}):
        if sentence.select("p"):
            new_sentence = sentence.text.replace(".", ". ").replace("?", "? ").replace("!", "! ")
            #print(new_sentence)
            tokenized_sentence = sent_tokenize(new_sentence)
            #print(tokenized_sentence[0].strip())
            dutch_sentences.append(tokenized_sentence[0].strip())
    x += 1
    
#print(dutch_sentences)
print(len(dutch_sentences))


# In[7]:


portuguese_sentences = []

x = 0
while x < 1000:
    webpage_pt = requests.get('http://www.smartphrase.com/cgi-bin/randomphrase.cgi?portuguese&humorous&normal')
    soup_pt = BeautifulSoup(webpage_pt.content)
    #print(soup_it.select("td")[6])
    #print(soup_it.select("tr")[3].find_all('td'))

    for sentence in soup_pt.find_all(attrs = {'bgcolor': '#DCDCFF'}):
        if sentence.select("p"):
            new_sentence = sentence.text.replace(".", ". ").replace("?", "? ").replace("!", "! ")
            #print(new_sentence)
            tokenized_sentence = sent_tokenize(new_sentence)
            #print(tokenized_sentence[0].strip())
            portuguese_sentences.append(tokenized_sentence[0].strip())
    x += 1
    
#print(portuguese_sentences)
print(len(portuguese_sentences))


# In[411]:


chinese_words = []

x = 0
while x < 1:
    for i in range(1):
        webpage_zh = requests.get('https://generator.lorem-ipsum.info/_chinese')
        soup_zh = BeautifulSoup(webpage_zh.content)

        for sentence in soup_zh.select("#txtDiv"):
            tokenized_sentence = nlp_chinese(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            for s in tokenized_sentence:
                #print(s)
                chinese_words.append(s)
                if len(chinese_words) == 1099:
                    break

    x += 1
    
print(len(chinese_words))


#--------------------------------------------------------------------------------------------------

#simplified chinese
#chinese_sentences = []

#x = 0
#while x < 11:
    #for i in range(1):
        #webpage_zh = requests.get('https://generator.lorem-ipsum.info/_chinese')
        #soup_zh = BeautifulSoup(webpage_zh.content)
        #print(soup_zh.select("#txtDiv"))

        #for sentence in soup_zh.select("#txtDiv"):
            #tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            #for s in tokenized_sentence:
                #s = s.split("。")
                #for i in s:
                    #print(i.strip())
                    #chinese_sentences.append(i.strip())
    #x += 1
    
#print(chinese_sentences)
#print(len(chinese_sentences))


#---------------------------------------


#practice = []
#tokenized_sentence = jieba.tokenize(u'我喜欢放学后学习数学')
#for s in tokenized_sentence:
    #print(s[0])
    #practice.append(s[0])
    
#print(practice)


# In[468]:


japanese_words = []

x = 0
while x < 1000:
    for i in range(1):
        webpage_jp = requests.get('https://generator.lorem-ipsum.info/_japanese2')
        soup_jp = BeautifulSoup(webpage_jp.content)
        #print(soup_jp.select("#txtDiv"))

        for sentence in soup_jp.select("#txtDiv"):
            tokenized_sentence = tokenizer_obj.tokenize(sentence.text)
            #print(tokenized_sentence)
            japanese_words.append(tokenized_sentence)
            
    x += 1
    
#print(japanese_sentences)
print(len(japanese_words))


#---------------------------------------------------------------------------------------------------


#japanese_sentences = []

#x = 0
#while x < 32:
    #for i in range(1):
        #webpage_jp = requests.get('https://generator.lorem-ipsum.info/_japanese2')
        #soup_jp = BeautifulSoup(webpage_jp.content)
        #print(soup_jp.select("#txtDiv"))

        #for sentence in soup_jp.select("#txtDiv"):
            #tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            #for s in tokenized_sentence:
                #s = s.split("。")
                #for i in s:
                    #print(i.strip())
                    #japanese_sentences.append(i.strip())
    #x += 1
    
#print(japanese_sentences)
#print(len(japanese_sentences))


# In[10]:


korean_sentences = []

x = 0
while x < 17:
    for i in range(1):
        webpage_ko = requests.get('https://generator.lorem-ipsum.info/_korean2')
        soup_ko = BeautifulSoup(webpage_ko.content)
        #print(soup_ko.select("#txtDiv"))

        for sentence in soup_ko.select("#txtDiv"):
            tokenized_sentence = nlp(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            for s in tokenized_sentence.sents:
                #print(str(s).strip())
                korean_sentences.append(s)
    x += 1
    
#print(korean_sentences)
#for s in korean_sentences:
    #print(s)

print(len(korean_sentences))


#---------------------------------------------------------------------------------------


#korean_sentences = []

#x = 0
#while x < 15:
    #for i in range(1):
        #webpage_ko = requests.get('https://generator.lorem-ipsum.info/_korean2')
        #soup_ko = BeautifulSoup(webpage_ko.content)
        #print(soup_ko.select("#txtDiv"))

        #for sentence in soup_ko.select("#txtDiv"):
            #tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            #for s in tokenized_sentence:
                #print(s)
                #korean_sentences.append(s.strip())
    #x += 1
    
#print(korean_sentences)
#print(len(korean_sentences))


# In[33]:


russian_sentences = []

x = 0
while x < 870:
    for i in range(1):
        webpage_ru = requests.get('https://www.coolgenerator.com/random-sentence-generator?lang=ru')
        soup_ru = BeautifulSoup(webpage_ru.content)
        for sentence in soup_ru.select(".content > ul > li > p > b > span"):
            #print(sentence.text)
            tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            for s in tokenized_sentence:
                #print(s.strip())
                russian_sentences.append(s.strip())
    x += 1
    
#print(russian_sentences)
print(len(russian_sentences))


# In[11]:


hebrew_sentences = []

x = 0
while x < 24:
    for i in range(1):
        webpage_he = requests.get('https://generator.lorem-ipsum.info/_hebrew')
        soup_he = BeautifulSoup(webpage_he.content)
        #print(soup_he.select("#txtDiv"))

        for sentence in soup_he.select("#txtDiv"):
            tokenized_sentence = nlp(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            for s in tokenized_sentence.sents:
                #print(s)
                hebrew_sentences.append(s)
    x += 1
    
#print(hebrew_sentences)
print(len(hebrew_sentences))


#-------------------------------------------------------------------------------------

#hebrew_sentences = []

#x = 0
#while x < 20:
    #for i in range(1):
        #webpage_he = requests.get('https://generator.lorem-ipsum.info/_hebrew')
        #soup_he = BeautifulSoup(webpage_he.content)
        #print(soup_he.select("#txtDiv"))

        #for sentence in soup_he.select("#txtDiv"):
            #tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            #for s in tokenized_sentence:
                #print(s)
                #hebrew_sentences.append(s)
    #x += 1
    
#print(hebrew_sentences)
#print(len(hebrew_sentences))


# In[12]:


arabic_sentences = []

x = 0
while x < 25:
    for i in range(1):
        webpage_arb = requests.get('https://generator.lorem-ipsum.info/_arabic')
        soup_arb = BeautifulSoup(webpage_arb.content)
        #print(soup_arb.select("#txtDiv"))

        for sentence in soup_arb.select("#txtDiv"):
            tokenized_sentence = nlp(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            for s in tokenized_sentence.sents:
                #print(s)
                arabic_sentences.append(s)
    x += 1
    
#print(arabic_sentences)
print(len(arabic_sentences))


#--------------------------------------------------------------------------------------


#arabic_sentences = []

#x = 0
#while x < 20:
    #for i in range(1):
        #webpage_arb = requests.get('https://generator.lorem-ipsum.info/_arabic')
        #soup_arb = BeautifulSoup(webpage_arb.content)
        #print(soup_arb.select("#txtDiv"))

        #for sentence in soup_arb.select("#txtDiv"):
            #tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            #for s in tokenized_sentence:
                #print(s)
                #arabic_sentences.append(s)
    #x += 1
    
#print(arabic_sentences)
#print(len(arabic_sentences))


# In[13]:


hindi_sentences = []

x = 0
while x < 485:
    for i in range(1):
        webpage_hi = requests.get('https://generator.lorem-ipsum.info/_hindi')
        soup_hi = BeautifulSoup(webpage_hi.content)
        #print(soup_hi.select("#txtDiv"))

        for sentence in soup_hi.select("#txtDiv"):
            tokenized_sentence = nlp(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            for s in tokenized_sentence.sents:
                #print(str(s).strip())
                hindi_sentences.append(s)
                    
    x += 1
    
#print(hindi_sentences)
print(len(hindi_sentences))


#---------------------------------------------------------------------------------------


#hindi_sentences = []

#x = 0
#while x < 100:
    #for i in range(1):
        #webpage_hi = requests.get('https://generator.lorem-ipsum.info/_hindi')
        #soup_hi = BeautifulSoup(webpage_hi.content)
        #print(soup_hi.select("#txtDiv"))

        #for sentence in soup_hi.select("#txtDiv"):
            #tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            #for s in tokenized_sentence:
                #s = s.split("\n\n")
                #for i in s:
                    #print(i.strip())
                    #hindi_sentences.append(i.strip())
    #x += 1
    
#print(hindi_sentences)
#print(len(hindi_sentences))


# In[129]:


greek_sentences = []

x = 0
while x < 18:
    for i in range(1):
        webpage_gr = requests.get('https://generator.lorem-ipsum.info/_greek')
        soup_gr = BeautifulSoup(webpage_gr.content)
        #print(soup_gr.select("#txtDiv"))

        for sentence in soup_gr.select("#txtDiv"):
            tokenized_sentence = nlp_greek(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            for s in tokenized_sentence.sents:
                #print(s)
                greek_sentences.append(s)
    x += 1
    
#print(greek_sentences)
print(len(greek_sentences))


# In[15]:


armenian_sentences = []

x = 0
while x < 700:
    for i in range(1):
        webpage_arm = requests.get('https://generator.lorem-ipsum.info/_armenian')
        soup_arm = BeautifulSoup(webpage_arm.content)
        #print(soup_arm.select("#txtDiv"))

        for sentence in soup_arm.select("#txtDiv"):
            tokenized_sentence = nlp(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            for s in tokenized_sentence.sents:
                #print(s)
                armenian_sentences.append(s)
    x += 1
    
#print(armenian_sentences)
print(len(armenian_sentences))


#--------------------------------------------------------------------------------------


#armenian_sentences = []

#x = 0
#while x < 20:
    #for i in range(1):
        #webpage_arm = requests.get('https://generator.lorem-ipsum.info/_armenian')
        #soup_arm = BeautifulSoup(webpage_arm.content)
        #print(soup_arm.select("#txtDiv"))

        #for sentence in soup_arm.select("#txtDiv"):
            #tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            #for s in tokenized_sentence:
                #print(s)
                #armenian_sentences.append(s)
    #x += 1
    
#print(armenian_sentences)
#print(len(armenian_sentences))


# In[16]:


georgian_sentences = []

x = 0
while x < 890:
    for i in range(1):
        webpage_kt = requests.get('https://generator.lorem-ipsum.info/_georgian')
        soup_kt = BeautifulSoup(webpage_kt.content)
        #print(soup_kt.select("#txtDiv"))

        for sentence in soup_kt.select("#txtDiv"):
            tokenized_sentence = nlp(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            for s in tokenized_sentence.sents:
                #print(s)
                georgian_sentences.append(s)
    x += 1
    
#print(georgian_sentences)
print(len(georgian_sentences))


#----------------------------------------------------------------------------------

#georgian_sentences = []

#x = 0
#while x < 20:
    #for i in range(1):
        #webpage_kt = requests.get('https://generator.lorem-ipsum.info/_georgian')
        #soup_kt = BeautifulSoup(webpage_kt.content)
        #print(soup_kt.select("#txtDiv"))

        #for sentence in soup_kt.select("#txtDiv"):
            #tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            #for s in tokenized_sentence:
                #print(s)
                #georgian_sentences.append(s)
    #x += 1
    
#print(georgian_sentences)
#print(len(georgian_sentences))


# In[17]:


latin_sentences = []

x = 0
while x < 18:
    for i in range(1):
        webpage_lat = requests.get('https://www.lipsum.com/feed/html')
        soup_lat = BeautifulSoup(webpage_lat.content)
        #print(soup_lat.select("#lipsum"))
        for sentence in soup_lat.select("#lipsum"):
            tokenized_sentence = nlp(sentence.text.strip())
            #print(tokenized_sentence)
            #print(len(tokenized_sentence))
            for s in tokenized_sentence.sents:
                #print(s)
                latin_sentences.append(s)
    x += 1
    
print(len(latin_sentences))
#print(latin_sentences)



#---------------------------------------------------------------------------


#latin_sentences = []

#x = 0
#while x < 18:
    #for i in range(1):
        #webpage_lat = requests.get('https://www.lipsum.com/feed/html')
        #soup_lat = BeautifulSoup(webpage_lat.content)
        #print(soup_lat.select("#lipsum"))
        #for sentence in soup_lat.select("#lipsum"):
            #tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            #for s in tokenized_sentence:
                #print(s)
                #latin_sentences.append(s)
    #x += 1
    
#print(len(latin_sentences))
#print(latin_sentences)


#----------------------------------------------------------------------------------------------------------
#This code works, the webpage just takes too long to load the data

#x = 0
#while x < 1000:
    #for i in range(1):
        #webpage_lat = requests.get('https://corpora.fi.muni.cz/cblm/generate.cgi?language=latin')
        #soup_lat = BeautifulSoup(webpage_lat.content)
        #print(soup_lat)
        #for sentence in soup_lat.select(".g"):
            #print(sentence.text.strip())
            #latin_sentences.append(sentence.text.strip())
    #x += 1
    
#print(latin_sentences)
#print(len(latin_sentences))


# In[18]:


swedish_sentences = []

x = 0
while x < 43:
    for i in range(1):
        webpage_sw = requests.get('http://xn--lkss-soa3h.vogelius.se/l%C3%A4ngre.php')
        soup_sw = BeautifulSoup(webpage_sw.content)
        #print(soup_sw.select(".lI"))
        for sentence in soup_sw.select('.lI'):
            tokenized_sentence = sent_tokenize(sentence.text.strip())
            #print(tokenized_sentence)
            for s in tokenized_sentence:
                #print(s)
                swedish_sentences.append(s)
    x += 1
        
print(len(swedish_sentences))


# Data was gathered from the following:
# - [Cool Generator (English, Russian)](https://www.coolgenerator.com/random-sentence-generator)
# - [SmartPhrase.com Online Phrasebook (Spanish, German, French, Italian, Dutch, Portuguese)](http://www.smartphrase.com/index.shtml)
# - [Professional lorem ipsum generator (Chinese, Japanese, Korean, Hebrew, Arabic, Greek, Hindi, Armenian, Georgian)](https://generator.lorem-ipsum.info/)
# - [Lorem Ipsum (Latin)](https://www.lipsum.com/feed/html)
# - [LÖKSÅS IPSUM (Swedish)](http://xn--lkss-soa3h.vogelius.se/l%C3%A4ngre.php)
# 
# *Note: The lorem ipsum generators follows the grammar & sentence structures of these languages, but it doesn't make any sense. Transliterations are in Greek, Armenian, Georgian*
# 
# <hr>

# ### Part 2: Create and Combine DataFrames
# 
# After getting the randomized sentences for each language, and putting them into separate language lists, we can now use the lists and create DataFrames from each of them. We will create a `text` column that will contain the phrases and sentences; and we also need to put a `language` column to differentiate which language is which because we will be combining all the DataFrames into one large DataFrame.

# In[34]:


english = pd.DataFrame(english_sentences, columns = ['text'])
#english.head()


# In[35]:


english['language'] = ['english'] * len(english) 
english.tail()


# In[36]:


spanish = pd.DataFrame(spanish_sentences, columns = ['text'])
#spanish.head()


# In[37]:


spanish['language'] = ['spanish'] * len(spanish)
spanish.tail()


# In[38]:


french = pd.DataFrame(french_sentences, columns = ['text'])
#french.head()


# In[39]:


french['language'] = ['french'] * len(french)
french.tail()


# In[40]:


german = pd.DataFrame(german_sentences, columns = ['text'])
#german.head()


# In[41]:


german['language'] = ['german'] * len(german)
german.tail()


# In[42]:


italian = pd.DataFrame(italian_sentences, columns = ['text'])
#italian.head()


# In[43]:


italian['language'] = ['italian'] * len(italian)
italian.tail()


# In[44]:


dutch = pd.DataFrame(dutch_sentences, columns = ['text'])
#dutch.head()


# In[45]:


dutch['language'] = ['dutch'] * len(dutch)
dutch.tail()


# In[46]:


portuguese = pd.DataFrame(portuguese_sentences, columns = ['text'])
#portuguese.head()


# In[47]:


portuguese['language'] = ['portuguese'] * len(portuguese)
portuguese.tail()


# In[412]:


chinese = pd.DataFrame(chinese_words, columns = ['text'])
#chinese.head()


# In[413]:


chinese = chinese.loc[chinese['text'] != '。']


# In[414]:


chinese['language'] = ['chinese'] * len(chinese)
chinese.tail()


# In[469]:


japanese = pd.DataFrame(list(zip(japanese_words)), columns = ['text'])
#japanese.head()


# In[470]:


japanese['language'] = ['japanese'] * len(japanese)
japanese.tail()


# In[52]:


korean = pd.DataFrame({'text': korean_sentences})
#korean.head()


# In[53]:


korean['language'] = ['korean'] * len(korean)
korean.tail()


# In[54]:


russian = pd.DataFrame(russian_sentences, columns = ['text'])
#russian.head()


# In[55]:


russian['language'] = ['russian'] * len(russian)
russian.tail()


# In[56]:


hebrew = pd.DataFrame(list(zip(hebrew_sentences)), columns = ['text'])
#hebrew.head()


# In[57]:


hebrew['language'] = ['hebrew'] * len(hebrew)
hebrew.tail()


# In[58]:


arabic = pd.DataFrame(list(zip(arabic_sentences)), columns = ['text'])
#arabic.head()


# In[59]:


arabic['language'] = ['arabic'] * len(arabic)
arabic.tail()


# In[60]:


hindi = pd.DataFrame(list(zip(hindi_sentences)), columns = ['text'])
#hindi.head()


# In[61]:


hindi['language'] = ['hindi'] * len(hindi)
hindi.tail()


# In[130]:


greek = pd.DataFrame(list(zip(greek_sentences)), columns = ['text'])
#greek.head()


# In[131]:


greek['language'] = ['greek'] * len(greek)
greek.tail()


# In[64]:


armenian = pd.DataFrame(list(zip(armenian_sentences)), columns = ['text'])
#armenian.head()


# In[65]:


armenian['language'] = ['armenian'] * len(armenian)
armenian.tail()


# In[66]:


georgian = pd.DataFrame(list(zip(georgian_sentences)), columns = ['text'])
#georgian.head()


# In[67]:


georgian['language'] = ['georgian'] * len(georgian)
georgian.tail()


# In[68]:


latin = pd.DataFrame(list(zip(latin_sentences)), columns = ['text'])
#latin.head()


# In[69]:


latin['language'] = ['latin'] * len(latin)
latin.tail()


# In[70]:


swedish = pd.DataFrame(swedish_sentences, columns = ['text'])
#swedish.head()


# In[71]:


swedish['language'] = ['swedish'] * len(swedish)
swedish.tail()


# #### Merging All the DataFrames

# Now that we have gathered all the languages and put them into each individual DataFrames, we're going to combine all into one single DataFrame.

# In[471]:


language_data = pd.concat([english, spanish, french, german, italian, dutch, portuguese, chinese, japanese, korean, russian, hebrew, arabic, hindi, greek, armenian, georgian, latin, swedish])


# In[336]:


#language_data.head(10000)
language_data.head()


# In[337]:


#language_data.tail(10000)
language_data.tail()


# <hr>
# 
# ### Part 3: Convert DataFrame to `.csv` File
# 
# We want to convert it to a `.csv` because it takes so long to run the code above every single time, we want a more permanent solution we can pull the data from. By doing this, the sentences won't randomize every time as well.
# 
# 
# From now on, we'll be using the data from the `.csv` file.

# In[472]:


language_data_csv = language_data.to_csv("language_data.csv", index = False)


# To make sure this has worked, we're going to call the `.csv` file that's been created.

# In[473]:


new_language_data = pd.read_csv('language_data.csv')
#new_language_data.head(10000)
new_language_data.head()


# In[340]:


#new_language_data.tail(10000)
new_language_data.tail()


# Now we'll want to check to see if there's any missing values; if there are, we need to remove them or the model won't work.

# In[474]:


new_language_data = new_language_data.dropna()


# In[475]:


new_language_data.isnull().sum()


# In[476]:


new_language_data['language'].value_counts()


# <hr>
# 
# ### Part 4: Creating the Model
# 
# Now that the data is been cleaned, we can now go ahead and split the data set into training and test sets. We will need to fit and transform the data into a format `scikit-learn` can use.

# In[477]:


X = new_language_data['text']
y = new_language_data['language']


# In[478]:


encoder = LabelEncoder()
y = encoder.fit_transform(y) #this will return the language rather than a number


# #### Bag of Words

# In[479]:


vectorizer = CountVectorizer()
x = vectorizer.fit_transform(X)


# In[480]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 50)


# In[481]:


model = MultinomialNB()
model.fit(x_train, y_train)


# In[482]:


model.score(x_test, y_test)


# #### Language Prediction

# Since the `.score` is rated as 94.44%, we should be able to get a pretty accurate result when we predict the language the is entered. We are going to test this model using 5 unknown languages.
# 
# *Note: These sentences were created by writing in English, then using Google Translate to get the sentences in these languages. Therefore the sentences might not be gramatically accurate.*

# In[486]:


#language_one = 'I like to eat potatoes for dinner.'
#language_two = 'Estudié durante cuatro horas ayer por la tarde.'
#language_three = "J'aime manger des oranges tous les jours à l'hôtel."
#language_four = 'Hast du letzte Nacht genug geschlafen?'
#language_five = 'Ti piace mangiare il pane con la marmellata.'
#language_six = 'Ik zag het vliegtuig in de nachtelijke hemel.'
#language_seven = 'Eu gosto de caminhar uma vez por mês.'
#language_eight = '我喜欢放学后学习数学'
#language_nine = '今日は自転車で通勤しました'
#language_ten = '내일 시험에 어려운 문제가 있을 것이다.'
#language_eleven = 'Я сегодня ездил на автобусе в магазин'
#language_twelve = 'כבר מאוחר מדי הגיע הזמן ללכת לישון'
#language_thirteen = 'ذهبت مع صديقي في وقت سابق لشراء المزيد من الملابس'
#language_fourteen = 'क्या आपने नई किताब के बारे में सुना है जो आ रही है'
#language_fifteen = 'Έχουμε σχέδια να ταξιδέψουμε στα βουνά τον επόμενο μήνα'
#language_sixteen = 'Ես սիրում եմ շոյել շանը'
#language_seventeen = 'მაგიდაზე არის ფურცელი, რომელზეც ჩანაწერებია'
#language_eighteen = 'Vide ne obliviscaris vigiliam domi relinquere'
#language_nineteen = 'Den här staden har så många berg, grönskan är vacker'


# In[487]:


language_one = "J'aime manger des oranges tous les jours à l'hôtel."
language_two = '내일 시험에 어려운 문제가 있을 것이다.'
language_three = 'Ik zag het vliegtuig in de nachtelijke hemel.'
language_four = 'Я сегодня ездил на автобусе в магазин'
language_five = 'Eu gosto de caminhar uma vez por mês.'
language_six = 'ذهبت مع صديقي في وقت سابق لشراء المزيد من الملابس'
language_seven = 'Den här staden har så många berg, grönskan är vacker'


# In[488]:


def predict(language):
    x = vectorizer.transform([language]).toarray()
    lang = model.predict(x)
    lang = encoder.inverse_transform(lang) #finds the language corresponding to the predicted value
    return lang[0]


# In[489]:


print(predict(language_one))


# In[490]:


print(predict(language_two))


# In[491]:


print(predict(language_three)) 


# In[492]:


print(predict(language_four))


# In[493]:


print(predict(language_five))


# In[494]:


print(predict(language_six))


# In[495]:


print(predict(language_seven))


# Based off our language detection model, it got all of our languages correct!

# In[ ]:




