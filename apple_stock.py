from bs4 import BeautifulSoup
import urllib2
import pprint

page = urllib2.urlopen('http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices')
soup = BeautifulSoup(page)
links = soup.find_all('td',attrs={'class':'yfnc_tabledata1'})
closes = {}
for link in links:
    try:
        if link.has_attr('nowrap') and not link.has_attr('colspan'):
            closes[link.text] = link.find_next_siblings(
                )[3].text
    except IndexError:
        continue
pprint.pprint closes
