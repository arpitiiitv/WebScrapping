from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.cricbuzz.com/cricket-stats/icc-rankings/men/teams')

soup = BeautifulSoup(res.text,'lxml')
test_data=soup.find('div',{'class':'cb-col cb-col-100 cb-padding-left0'})
rank_box = test_data.find_all('div',{'class' : 'cb-col cb-col-100 cb-font-14 cb-brdr-thin-btm text-center'})

print("+---------  CRICKET    TEST   RANKING -----------+")
print("+------------------------------------------------+")
print("| Position  |Team              |Rating   |Point  |")

print("+------------------------------------------------+")
for r in rank_box:
    position=r.find('div',{'class' : 'cb-col cb-col-20 cb-lst-itm-sm '})
    team=r.find('div',{'class' : 'cb-col cb-col-50 cb-lst-itm-sm text-left'})
    rating=r.find('div',{'class' : 'cb-col cb-col-14 cb-lst-itm-sm'})
    point=r.find('div',{'class' : 'cb-col cb-col-14 cb-lst-itm-sm '})
    print("|",position.text," "*(8-len(position.text)),"|",team.text," "*(15-len(team.text)),"|",rating.text," "*(6-len(rating.text)),
    "|",point.text," "*(4-len(point.text)),"|")

print("+------------------------------------------------+")