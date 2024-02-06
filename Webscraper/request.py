import requests
from bs4 import BeautifulSoup

def scrape_page(web_url,linktag):
    response = requests.get(web_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraph_list = []
    paragraphs = soup.find_all(f"{linktag}")
    for i in paragraphs:
        paragraph_list.append(i)
    return paragraph_list