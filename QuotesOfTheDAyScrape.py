print("QuotesOfTheDAyScrape\n")
from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.brainyquote.com/quote_of_the_day')
#print(res.text)

soup = BeautifulSoup(res.text,'lxml')
#print(soup)

image_box = soup.find('img',{'id' : 'qimage_100795'})
print(image_box['alt'])