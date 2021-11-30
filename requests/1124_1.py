#from io import StringIO
#import pandas as pd
import requests
from bs4 import BeautifulSoup
#import lxml
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
site = "https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"
#response = requests.post(site,params=None, headers=None, cookies=None, auth=None, timeout=None)
response = requests.get('https://tw.stock.yahoo.com/quote/2330')
soup = BeautifulSoup(response.text,'html.parser')
soup_title=soup.title#抓網頁title
soup_h1=soup.find('h1')#抓<h1></h1>
print(soup_h1)

#df = pd.read_csv(StringIO(response.text))
#print(response.text)