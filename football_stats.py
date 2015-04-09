from bs4 import BeautifulSoup
import urllib2

page = urllib2.urlopen('http://www.cbssports.com/'\
                    'nfl/stats/playersort/nfl/year-2014'\
                    '-season-regular-category-touchdowns')
soup = BeautifulSoup(page)
links = soup.find_all('tr')
names = []
pos = []
teams = []
tds = []
for link in links:

    try:
        if link.td.has_attr('align'):
            names.append(link.td.a.get_text())
            pos.append(link.td.find_next_siblings()\
                       [0].get_text())
            teams.append(link.td.find_next_siblings()\
                       [1].get_text())
            tds.append(link.td.find_next_siblings()\
                       [5].get_text())
    except AttributeError:
        continue

for i in range(20):
    print names[i],pos[i],teams[i],tds[i]
