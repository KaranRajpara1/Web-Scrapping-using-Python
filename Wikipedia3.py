from urllib.request import urlopen
import urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def covid_record() :
    url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India"
    html = urlopen(url, context=ctx).read()

    soup = BeautifulSoup(html, "html.parser")

    right_table=soup.find('table', class_='wikitable plainrowheaders sortable')


    Cases=[]
    Deaths=[]
    Recoveries=[]
    Active=[]
    State=[]
    for row in right_table.findAll('tr'):
        cells=row.findAll('td')
        #print(len(cells))
        if len(cells)==4:
            Cases.append(cells[0].find(text=True).strip())
            Deaths.append(cells[1].find(text=True).strip())
            Recoveries.append(cells[2].find(text=True).strip())
            Active.append(cells[3].find(text=True).strip())

    for row in right_table.find_all('th') :
        State.append(row.find(text=True).strip())

    #print(len(State[11:]))
    State = State[11:] #Because list of state contain first 10 elements as headings of table



    print("{:^40}|{:^40}|{:^40}|{:^40}|{:^40}".format('State','Cases','Deaths','Recoveries','Active'))
    print('-'*180)
    for a,b,c,d,e in zip(State,Cases,Deaths,Recoveries,Active) :
        a=a.strip()
        b=b.strip()
        c=c.strip()
        d=d.strip()
        e=e.strip()
        print("{:^40}|{:^40}|{:^40}|{:^40}|{:^40}".format(a,b,c,d,e))
