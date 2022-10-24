import sys
import requests
from bs4 import BeautifulSoup
import re

url_regex = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

try:
    while True:
        inp = input('Enter a url: ')
        if re.match(url_regex, inp):
            print('A valid url!')
            html_doc = requests.get(
                "https://www.gutenberg.org/files/11/11-h/11-h.htm").text
            my_soup = soup = BeautifulSoup(html_doc, 'html.parser')
            print(my_soup.prettify())
        else:
            print('You entered an invalid url!')
except (EOFError, KeyboardInterrupt):
    print()
    sys.exit(0)


"""
html_doc = requests.get("https://www.gutenberg.org/files/11/11-h/11-h.htm").text

my_soup = soup = BeautifulSoup(html_doc, 'html.parser')

def prettified(soup):
    print(soup.prettify())


def sample_func():
    return "deneme"
"""
