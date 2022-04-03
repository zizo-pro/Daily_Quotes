import twitter
import requests
from translate import Translator
from time import sleep

from os import system

de_lang = Translator("de")


url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    'x-rapidapi-key': "2ef4b333cemsh77bafae28ad3294p1b98ccjsnd4c0f3dc0f5a",
    'x-rapidapi-host': "quotes15.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

quote = response.text
q = quote.find("content")
f = quote[q:]
n = f.find("\",")
tweet = f[10:n]

translation_de = de_lang.translate(tweet)
new_tweet = f"EN: {tweet}\n\nDE: {translation_de}"
api = twitter.Api(consumer_key="pZJ43RsRELKN2EQu41LWrUUnj",
                  consumer_secret="QXxBc166p8tpm04mVV5kSLsHuohBdbBhZdcDo4NZnDKjXyKzD1",
                  access_token_key="1509999113554862087-YPFsehxsgXSlkI9cuxk0bI7fgPdwE1",
                  access_token_secret="gUtxTKpkb7X2LbMwZ949U6tMGzl22m8Q2OWgHY0TVOHaZ")
try:
  api.PostUpdate(status=new_tweet)
  sleep(20)
  system("python d:/projects/PYTHON/Daily_Quotes/main.py")
except:
  # sleep(20)
  system("python d:/projects/PYTHON/Daily_Quotes/main.py")