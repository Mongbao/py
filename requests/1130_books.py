from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

resp = requests.get('https://www.books.com.tw/web/cebook_edit/?ptime=&pdevice=P&loc=menu_th_792_001')
soup = BeautifulSoup(str(resp.text),'html.parser')

catelog = soup.find(class_='mod_b type02_l001-1 clearfix')
catelogList = catelog.find_all('a')
catelogDict = dict()
#取得所有連結
for c in catelogList:
    title = c.text
    href = c.get('href')
    href = href.split('&')[0]
    catelogDict[title]=href
    #print(catelogDict[title])
#print(catelogDict)
#df = pd.DataFrame(columns = ['類型‘,‘書名','作者','優惠價'])

for title,url in catelogDict.items():
    #time.sleep(10)
    resp1 = requests.get(url)
    soup1 = BeautifulSoup(str(resp1.text),'html.parser')

    books = soup1.find(class_='mod_a clearfix')
    items = books.find_all(class_='item')

    for i,item in enumerate(items):
        if i == 20:
            break
        #time.sleep(10)
        book_name = item.find('img').get('alt')
        print(item)
"""
        if item.find_all('li')[0].text[0,2] == '作者':
            book_another = item.find_all('li')[0].find('a').text
        else:
            book_another = ""
    
        book_price = item.find_all('b')[-1].text
        print(book_name)

        df.loc[len(df)+1] = None
        df.iloc[-1]['類型'] = title
        df.iloc[-1]['書名'] = book_name
        df.iloc[-1]['作者'] = boke_another
        df.iloc[-1]['優惠價'] = book_price

df.to_CSV('booksScraper.csv')

"""