from bs4 import BeautifulSoup
import requests
import re
    
def wiki_surf(source: str, destination: str):
    source_relationship = simple_scrape(source)
    for hyp in source_relationship:
        if str(destination) in source_relationship:
            print('Destination URL ' + str(destination) + ' is reached.') #base case
            break
        else: 
            wiki_surf(hyp, destination)
            break

def simple_scrape(url):
    result = requests.get(url)
    article = BeautifulSoup(result.content, "html.parser")
    related_with = []
    for hyp in article.find_all('a'):
        href_links = hyp.get('href')
        if href_links and href_links.startswith('/wiki/'):
            related_with.append('https://en.wikipedia.org' + str(href_links))
    return related_with

def main():
    p = input('Source URL: ')
    q = input('Destination URL: ')
    wiki_surf(p, q)

main()