from bs4 import BeautifulSoup
import requests
import re

def simple_scrape(url):
    result = requests.get(url)
    article = BeautifulSoup(result.content, "html.parser")
    # tag_a = article.find_all("a")
    # hyp = [link.get("href") for link in tag_a]

    # for link in hyp:
    #     # print("https://en.wikipedia.org" + str(link))
    #     print(link)

    tag_a = article.find_all("a", title=re.compile(r'.'), href=re.compile(r'/wiki+'))
    for i in tag_a:
        print (i.text)

q = input("Your Wikipedia page: ")
simple_scrape(q)
