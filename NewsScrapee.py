from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.indiatoday.in/")
#print(res.text)

soup = BeautifulSoup(res.text,'lxml')
#print(soup)

news_box = soup.find('ul',{'class' : 'itg-listing'})
all_news = news_box.find_all('a')
for news in all_news:
    print()
    print(news.text)
    print()