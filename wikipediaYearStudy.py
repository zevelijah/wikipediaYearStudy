import datetime
from random import randint
import webbrowser

def wikipediaYearPage():
    currentYear = datetime.datetime.now().year
    searchYearRaw = randint(-699, currentYear)
    if searchYearRaw <= 0:
        wikiLink = webbrowser.open(f'https://en.wikipedia.org/wiki/{abs(searchYearRaw-1)}_BC')
    else:
        wikiLink = webbrowser.open(f'https://en.wikipedia.org/wiki/AD_{abs(searchYearRaw)}')
    return wikiLink

print(wikipediaYearPage())