from bs4 import BeautifulSoup
import requests

def relationship(hyperlink):
    related_with = []
    return related_with
    
def wiki_surf(source: str, destination: str):
    art_log = []
    while (source != destination):
        wiki_surf(source, destination)
        art_log.append(destination)
    return art_log

p = input('Source URL: ')
q = input('Destination URL: ')
wiki_surf(p, q)