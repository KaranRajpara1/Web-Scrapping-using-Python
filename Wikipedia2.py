from urllib.request import urlopen
import urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def Premier_League() :
    #url = "https://en.wikipedia.org/wiki/1999%E2%80%932000_FA_Premier_League"
    url = "https://en.wikipedia.org/wiki/2019%E2%80%9320_Premier_League"
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    right_table=soup.find('table', class_='wikitable sortable')

    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    # print(right_table)
    for row in right_table.findAll('tr'):
        cells=row.findAll('td')
        if len(cells)==4:
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))


    print("{:^30}|{:^30}|{:^30}|{:^30}".format('Team','Location','Stadium','Capacity'))
    print('-'*120)
    for a,b,c,d in zip(A,B,C,D) :
        print("{:^30}|{:^30}|{:^30}|{:^30}".format(a,b,c,d))
