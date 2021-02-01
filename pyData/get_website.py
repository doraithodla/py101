from bs4 import BeautifulSoup
import requests


def get(URL):
    """
    returns the website data html content
    """
    return requests.get(url=URL).content


def extract_links(URL, content):
    """
    extracts all hyperlinks from the html recieved and returns a list of them
    :param content: html of the webpage
    :return: list of URLS
    """
    soup = BeautifulSoup(content, "lxml")
    links = []
    for link in soup.findAll('a'):
        # print(link)
        if link.get('href').startswith("/"):
            links.append((link.get("title"), URL + link.get('href')))
            continue
        links.append((link.get("title"), link.get('href')))
    return links

# URL = "http://www.ashish.ch"
# print(extract_links(URL, get(URL)))
