import requests
import json
import subprocess
import os
import glob
from bestin.porter2 import stem
import requests
import json
import re
#import tesserocr
#from PIL import Image
#import urllib2 as urllib
import io
import requests

class content_analyzer:
    def __init__(self):
#        test_path = "/home/valeriyasin/Documents/test_doc"
        self.headers = {'app_id': '7fd7d9b5', 'app_key': 'a792493bd95822c3e8f00c3665f5f4a2'}
        self.keywords = {'donation' : 0.7, 'charity' : 0.6, 'elderly' : 0.6, 'gather' : 0.1,                         'love' : 0.1, 'support' : 0.2, 'fundraising' : 0.4, 'sport' : 0.2, 'run' :0.2,
                         'art' :0.2, 'friends' :0.1, 'healthcare' :0.3, \
                         'education' : 0.1, 'teaching' : 0.3, 'learning' : 0.1, 'together' :0.2, 'development' : 0.2, \
                         'worldwide' : 0.1, 'globalization' : 0.1, 'voulnteer' : 0.6, 'peace' : 0.3,\
                         'participation' : 0.1, 'training': 0.1}
        self.key_phrases = {'blood donation' : 0.8, 'raise money':  0.4,  'raise funds' : 0.4, 'charity marathon' : 0.3,                           'donate blood' : 0.8, 'give support' : 0.2, 'save life' : 0.8, 'greate job' : 0.2,                             'charity runners' : 0.3}

    def process_keywords(self):
        for key in list(self.keywords):
            self.keywords[stem(key)] = self.keywords[key]
            del self.keywords[key]
        for key in list(self.key_phrases):
            key_words = key.split()
            new_key = []
            for key_word in key_words:
                new_key.append(stem(key_word))
            new_key_phrase = " ".join(new_key)
            self.key_phrases[new_key_phrase] = self.key_phrases[key]
            del self.key_phrases[key]



    # def train_model(self, file_path):
    #     setup_java()
    #     os.system("java -Xmx526M /home/valeriya/Programms/kea-5.0_full/TestKea train")


    def get_sentiment(self, text_in, language='English'):
        headers = {
            'x-api-key': '9CAfxmC4WB10tnS9RY9oG92Io0M4trVp7HpTUEjR',
            'Content-Type': 'application/json',
        }
        data = {"textIn": text_in,  "language": language}
        r = requests.post('https://jmlk74oovf.execute-api.eu-west-1.amazonaws.com/dev/sentiment?wait=true', headers=headers, data=json.dumps(data))
        content = r.json()
        return content['results']['prediction']


    def setup_java(self):
        os.system("export KEAHOME=/home/valeriyasin/Programms/kea-5.0_full")
        os.system("export CLASSPATH=$CLASSPATH:$KEAHOME")
        os.system("export CLASSPATH=$CLASSPATH:$KEAHOME/lib/commons-logging.jar")
        os.system("export CLASSPATH=$CLASSPATH:$KEAHOME/lib/icu4j_3_4.jar")
        os.system("export CLASSPATH=$CLASSPATH:$KEAHOME/lib/iri.jar")
        os.system("export CLASSPATH=$CLASSPATH:$KEAHOME/lib/jena.jar")
        os.system("export CLASSPATH=$CLASSPATH:$KEAHOME/lib/snowball.jar")
        os.system("export CLASSPATH=$CLASSPATH:$KEAHOME/lib/weka.jar")
        os.system("export CLASSPATH=$CLASSPATH:$KEAHOME/lib/xercesImpl.jar")
        os.system("export CLASSPATH=$CLASSPATH:$KEAHOME/lib/kea-5.0.jar")

    # def extract_keywords(self, text_path):
    #     extracted_keywords = []
    #     for file in glob.glob(test_path + "/*.key"):
    #         os.system("rm " + file)
    #     os.system("java -Xmx526M /home/valeriyasin/Programms/kea-5.0_full/TestKea test " + text_path)
    #     for file in glob.glob(test_path + "/*.key"):
    #         f = open(file)
    #         for line in f:
    #             extracted_keywords.append(line)
    #         f.close()
    #     return extracted_keywords

    def process_text(self, text):
        score = 0
        self.process_keywords()
        if self.get_sentiment(text) == 'negative':
            return 0.
        words = text.split()
        for word in words:
            word = re.sub('[!@#$]1234567890?.{}()', '', word)
            if stem(word).lower() in self.keywords:
                score += self.keywords[stem(word).lower()]
        return score

    def process_picture(self, url):
        real_url = 'https://api.kairos.com/v2/media?source=' + url
        headers = {'app_id': '7fd7d9b5', 'app_key': 'a792493bd95822c3e8f00c3665f5f4a2'}
        score = 0
        threshold = 0
        r = requests.post(real_url,headers=headers)
#         print(r)
        res = json.loads(r.text)
        people = res['frames'][0]['people']
        if len(people) > 4:
            threshold = len(people) * 50
            for person in people:
                emotions = person['emotions']
                person_score = 0
                person_score += emotios['joy'] - emotions['anger']
                score += person_score
        if score > threshold:
            score = float(score) / 100 / people.size
        fd = urlopen(url)
        image_file = io.BytesIO(fd.read())
        image = Image.open(image_file)
        text = tesserocr.image_to_text(image).strip()
        if text != None and text != "":
            score+= self.process_text(text)
        return score
