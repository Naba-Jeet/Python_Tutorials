import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source,'xml')

for url in soup.find_all('loc'):
    print(url.text)
    