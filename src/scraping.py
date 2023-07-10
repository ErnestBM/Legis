from bs4 import BeautifulSoup
import requests
import re

def simple_scrape(url):
    result = requests.get(url)
    article = BeautifulSoup(result.content, "html.parser")
    related_with = []
    for hyp in article.find_all('a'):
        href_links = hyp.get('href')
        if href_links and href_links.startswith('/wiki/'):
            related_with.append('https://en.wikipedia.org' + str(href_links))
    
    for line in related_with:
        print(line)

q = input("Your Wikipedia page: ")
simple_scrape(q)
