from bs4 import BeautifulSoup
import urllib.request
import json
import requests

url = 'https://news.yahoo.co.jp/topics'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/67.0.3396.99 Safari/537.36 '

def getNews(word):
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    #main = soup.find('div', attrs={'class': 'topicsMod'})
    #topics = main.select("li > a")
    topics = soup.select("li")

    count = 0
    list = []

    for topic in topics:
        #if topic.contents[0].find(word) > -1:
        if word in topic.contents[0]:               
            list.append(topic.contents[0])
            list.append(topic.get('href'))
            count += 1
    if count == 0:
        list.append("「" + word + "」に関する記事が見つかりませんでした！！")
        #list.append(topics)
          
    result = '\n'.join(list)
    return result
