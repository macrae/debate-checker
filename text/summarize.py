import time
import urllib.request

import requests

from bs4 import BeautifulSoup

url = "https://www.politifact.com/truth-o-meter/statements/2019/jul/12/weston-pagano/fact-checking-attack-joe-biden-about-immigration-d/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# TODO: need a better way to filter for the paragraphs of interest
paragraphs = [p.text for p in soup.findAll("p") if len(p.text) > 25]


# TODO: implement this method
def paragraph_to_summary(paragraph: str, summary_len: int) -> str:
    """Takes a paragraph and summarizes it the given summary length.
    """
