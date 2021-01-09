from selenium import webdriver
import bs4
import requests
import pyttsx3
from tkinter import *
import threading

#setting voice engine properties
engine=pyttsx3.init()
engine.setProperty('rate', 160)#the speed at which the engine speaks
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[20].id)#can change the id according to your own choice

#opening the site through which news is gathered
response = requests.get('https://inshorts.com/en/read')
soup = bs4.BeautifulSoup(response.text, 'html.parser')

titles = soup.findAll(class_='news-card')
news_title = []
news_article = []

for title in titles:
    #news headline
    if '<span itemprop="headline">' in str(title):
        title = str(title)
        x = title.find('<span itemprop="headline">')
        y = title.find('</span>', x)
        news_title.append(title[x + 26:y])

    #News article

    if '<div itemprop="articleBody">' in str(title):
        title = str(title)
        x = title.find('<div itemprop="articleBody">')
        y = title.find('</div>', x)
        news_article.append(title[x + 28:y])


# Speaking the headlines and articles

engine.say('hello there! Good morning. The following are the headlines for today! ')
engine.runAndWait()
for x in range(len(news_title)):

    engine.setProperty('voice', voices[20].id)
    engine.say(news_title[x])

    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 180)
    engine.say(news_article[x])
    engine.runAndWait()
