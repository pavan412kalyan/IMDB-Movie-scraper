

## this code is for scrapng the list from the urls until the last page(pagination)
##url ="https://www.imdb.com/search/title/?title_type=feature&languages=hi&view=simple&count=250&start=12000"

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import uuid,sys,os


def  scrapelist(soup) :
    ids =[]
    taglist = soup.findAll('div',{"class" : "col-title" })
    for t in taglist :
        try :
            ids.append(t.find('a')['href'].split('/')[2])
            print(t.find('a')['href'].split('/')[2])
        except Exception as e:          
            print(e)
    your_list=ids
    df = DataFrame (your_list)
    unique_filename = str(uuid.uuid4())
    df.to_csv("pagesId/"+ unique_filename+".csv" ,index=False)        
    

def start_pagination(next_page) :
    imdb = "https://www.imdb.com"
    while next_page!="" :
            print(next_page)
            r = requests.get(headers={'User-Agent': 'Mozilla/5.0'},url=next_page)
            soup = BeautifulSoup(r.text, 'html.parser')
            # print(soup)
            try: 
                  next_page = imdb + soup.find('span',{'class': 'ipc-see-more__text'})['href']
            except Exception as e: 
                print(e)
                next_page=""
            print(next_page)
            try :
                scrapelist(soup)
                print(next_page)
            except Exception as e: 
                print(e)
                break


def start(pageurl) :
    imdb = "https://www.imdb.com"
    query= "?title_type=feature,tv_movie,tv_series,tv_episode,tv_special,tv_miniseries,documentary,video_game,short,video,tv_short&languages=te&view=simple&sort=moviemeter,asc&count=250"
    os.makedirs("pages", exist_ok=True)
    os.makedirs("pagesId", exist_ok=True)

    url=imdb+query
    #url="https://www.imdb.com/search/title/?genres=western&countries=ad&languages=icl&view=simple&count=250"
#    url="https://www.imdb.com/search/title/?title_type=feature&languages=te&view=simple&count=250"
    #url ="https://www.imdb.com/search/title/?title_type=feature&languages=hi&view=simple&count=250&start=12000"
#    url="https://www.imdb.com/search/title/?countries=in&view=simple&count=250&after=WzkyMjMzNzIwMzY4NTQ3NzU4MDcsInR0OTkwNzA4MiIsOTU1MDFd"
    next_page=pageurl
    print(next_page)
    start_pagination(next_page)
#
#if __name__ == "__main__": 
#   file=sys.argv[1:]
#   if len(file)==1:
#       start(file[0])
#   else :
#        print('enter arguments --> python https://www.imdb.com/search/title/?title_type=feature&languages=te&view=simple&count=250 ')
#        
start("https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count=250&view=simple")   