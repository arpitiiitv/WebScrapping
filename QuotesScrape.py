from bs4 import BeautifulSoup
import requests

res = requests.get('http://quotes.toscrape.com/')
#print(res.content)
#proper ordered printing
#print(res.text)
#lxml  -> parser library
soup = BeautifulSoup(res.text , 'lxml')
#print(soup)

quote = soup.find_all('div',{'class' : 'quote'})
with open('Quotes.txt','w') as ff:
    for q in quote:
        msg = q.find('span',{'class' : 'text'})
        print(msg.text)
        ff.write(msg.text)
        author = q.find('small',{'class' : 'author'})
        print(author.text)
        ff.write("\n")
        ff.write(author.text)
        print()
        ff.write("\n\n")


