#https://ithelp.ithome.com.tw/articles/10202493
from bs4 import BeautifulSoup
import requests
#import json
#import numpy as np
#import pandas as pd

site = "https://www.ptt.cc/bbs/MobileComm/index.html"
response = requests.get(site)

soup = BeautifulSoup(response.text,"html.parser")
sel=soup.select("div.title a")

#print (sel)
for s in sel:
    print(s["href"], s.text) 