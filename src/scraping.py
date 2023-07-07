from bs4 import BeautifulSoup
import requests

def simple_scrape(url):
    result = requests.get(url)
    article = BeautifulSoup(result.text, "html.parser")
    tag_a = article.find_all("a")
    hyp = [link.get("href") for link in tag_a]

    for link in hyp:
        print("https://id.wikipedia.org/" + str(link))

q = input("Your Wikipedia page: ")
simple_scrape(q)
