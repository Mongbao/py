from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

#重複抓資料太多次會被擋nonetype' object has no attribute 'find_all'，加入header測試(https://www.pythonheidong.com/blog/article/535189/25dd7e0e7004f4f8651c/)
try:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    resp = requests.get('https://www.books.com.tw/web/cebook_edit/?ptime=&pdevice=P&loc=menu_th_792_001',headers=headers)
    soup = BeautifulSoup(resp.text,'html.parser')

    catelog = soup.find(class_='mod_b type02_l001-1 clearfix')
    print(type(catelog))
    catelogList = catelog.find_all('a')
    #print (catelogList)
    catelogDict = dict()

    #取得所有連結
    for c in catelogList:
        title = c.text
        href = c.get('href')
        href = href.split('&')[0]
        catelogDict[title]=href
        #print(catelogDict[title])
    #print(catelogDict)
    df = pd.DataFrame(columns = ['類型‘,‘書名','作者','優惠價'])

    for title,url in catelogDict.items():
        time.sleep(1)
        resp1 = requests.get(url,headers=headers)
        soup1 = BeautifulSoup(resp1.text,'html.parser')

        books = soup1.find(class_='mod_a clearfix')
        items = books.find_all(class_='item')

        for i,item in enumerate(items):
            if i == 5:
                break
            #time.sleep(1)
            book_name= item.find('img').get('alt')
            #print(item.find_all('li')[0].text)
            #print(item.find_all('li')[1].text)

            if item.find_all('li')[1].text[0:2] == '作者':
                book_another = item.find_all('li')[1].find('a').text
            else:
                book_another = ""
    
            book_price = item.find_all('b')[-1].text
            print(book_another)

            df.loc[len(df)+1] = None
            df.iloc[-1]['類型'] = title
            df.iloc[-1]['書名'] = book_name
            df.iloc[-1]['作者'] = book_another
            df.iloc[-1]['優惠價'] = book_price

    df.to_csv('booksScraper.csv')
except AttributeError:
    df.to_csv('booksScraper.csv')