from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.cricbuzz.com/cricket-stats/icc-rankings/men/teams')

soup = BeautifulSoup(res.text,'lxml')

oneday_data=soup.find('div',{'class':'cb-col cb-col-100 cb-plyr-tbody'})

rank_box = oneday_data.find_all('div',{'class' : 'cb-col cb-col-100 cb-font-14 cb-brdr-thin-btm text-center'})

print("+------------  CRICKET T - 20   RANKING -----------+")
print("+---------------------------------------------------+")
print("| Position  |Team                 |Rating   |Point  |")

print("+---------------------------------------------------+")
# test and oneday team 32
total_team=32
for r in rank_box:
    total_team=total_team-1
    if total_team<0 :
        position=r.find('div',{'class' : 'cb-col cb-col-20 cb-lst-itm-sm '})
        team=r.find('div',{'class' : 'cb-col cb-col-50 cb-lst-itm-sm text-left'})
        rating=r.find('div',{'class' : 'cb-col cb-col-14 cb-lst-itm-sm'})
        point=r.find('div',{'class' : 'cb-col cb-col-14 cb-lst-itm-sm '})
        print("|",position.text," "*(8-len(position.text)),"|",team.text," "*(18-len(team.text)),"|",rating.text," "*(6-len(rating.text)),
        "|",point.text," "*(4-len(point.text)),"|")
        
print("+---------------------------------------------------+")