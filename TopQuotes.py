print("Top Quotes \n")
from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.brainyquote.com/quote_of_the_day')
#print(res.text)

soup = BeautifulSoup(res.text,'lxml')
#print(soup)

image_box = soup.find_all('div',{'class' : 'row'})
myData =image_box[1]

x=myData.find_all('a',{'title' : 'view quote'})
for q in x:
    print(q.text)
    print()
    