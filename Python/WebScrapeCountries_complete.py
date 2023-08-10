import pygrab
import pandas as pd


def scrape(url):
    res = pygrab.get(url).text
    res = pd.read_html(res)[0]

    print(res)
