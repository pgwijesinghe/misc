import string
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

noe = 30
casename = []
parties = []
index = [""]

index.extend([str(int(j)) for j in list(np.linspace(10, int(noe-10), int((noe-10)/10)))])

for idx in index:
    url_env = "http://kenyalaw.org/caselaw/cases/advanced_search/page/" + idx + "/?totalcourt=54" # environment court
    url_high1 = "http://kenyalaw.org/caselaw/cases/advanced_search/page/" + idx + "/?totalcourt=18" # high court 1
    url_high2 = "http://kenyalaw.org/caselaw/cases/advanced_search/page/" + idx + "/?totalcourt=19" # high courts 2
    response = requests.get(url_high1)
    sp = bs(response.text, 'html.parser')
    for element in sp.findAll('div', attrs={"class":"post"}):
        casename.append(element.find('h2').text.strip())
        parties.append(element.findAll('p', attrs={"class":"bg"})[2].text.strip()[8:])

df = pd.DataFrame({'Case': casename, 'Parties':parties})
df.to_csv("highcourts1.csv", index=False)

